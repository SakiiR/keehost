import bcrypt
import random
import requests
from .config import (KEEHOST_URL, KEEHOST_APIKEY, SUPERADMIN, TOKEN_LENGTH, TOKEN_CHARSET)
from flask import (Flask, request, jsonify)

app = Flask(__name__)


@app.route('/')
def root():

    """ Login service root route """

    return jsonify({})


def valid_field(field):

    """ Check if a field is valid """

    return field and len(field) > 0


def get_user(username=None, token=None):

    """ Retrieve user by username """

    users = []
    if username is not None:
        users = requests.get(KEEHOST_URL + '/accounts?where={"username": "%s"}' % username, headers={'Authorization': KEEHOST_APIKEY}).json().get('_items')
    else:
        if token is not None:
            users = requests.get(KEEHOST_URL + '/accounts?where={"token": "%s"}' % token, headers={'Authorization': KEEHOST_APIKEY}).json().get('_items')
    if len(users) == 1:
        return users[0]
    return None


def generate_token(n=TOKEN_LENGTH, charset=TOKEN_CHARSET):

    """ Generate a new random token of n length chars """

    return ''.join(random.choice(charset) for _ in range(n))


@app.route('/authenticate', methods=['POST'])
@app.route('/login', methods=['POST'])
def authenticate():

    """ When a user try to authenticate to the API """

    data = request.json
    if data:
        username, password = data.get('username'), data.get('password')
        if valid_field(username) and valid_field(password):
            user = get_user(username=username)
            if user is not None:
                remote_password = user.get('password')
                if remote_password.encode('utf-8') == bcrypt.hashpw(password.encode('utf-8'), remote_password.encode('utf-8')):
                    token = generate_token()
                    r = requests.patch(KEEHOST_URL + '/accounts/%s' % user.get('_id'),
                                       json={'token': token},
                                       headers={'Authorization': KEEHOST_APIKEY,
                                                'If-Match': user.get('_etag')})
                    return jsonify({'success': True,
                                    'message': 'Successfully connected ! here is your secret token',
                                    'token': token})
    return jsonify({'success': False, 'message': 'Failed ! Bad username or/and bad password'})


@app.route('/deauthenticate')
@app.route('/logout')
def deauthenticate():

    """ When a user try to deauthenticate to the API """
    token = request.headers.get('Authorization', '')
    if len(token) == TOKEN_LENGTH:
        user = get_user(token=token)
        if user is not None:
            r = requests.patch(KEEHOST_URL + '/accounts/%s' % user.get('_id'),
                              json={'token': None},
                              headers={'Authorization': KEEHOST_APIKEY, 'If-Match': user.get('_etag')})
            return jsonify({'success': True, 'message': 'Success token invalidated !'})
    return jsonify({'success': False, 'message': 'Failed ! Bad token'})

