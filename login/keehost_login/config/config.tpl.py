import bcrypt
# Keehost Login Service Configuration

API_HOST = "0.0.0.0"
API_PORT = 1338

# Token configuration
TOKEN_LENGTH = 64
TOKEN_CHARSET = ("abcdefghijklmnopqrstuvwxyz"
                 "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                 "0123456789")

# Superadmin configuration
SUPERADMIN_USERNAME = "superadmin"
SUPERADMIN_PASSWORD = ""
SUPERADMIN_PASSWORD = bcrypt.hashpw(SUPERADMIN_PASSWORD.encode('utf-8'), bcrypt.gensalt()) # Please, change the password
SUPERADMIN = {
    'firstname': 'Super',
    'lastname': 'Admin',
    'username': SUPERADMIN_USERNAME,
    'token': None,
    'email': 'super.admin@keehost.com',
    'password': SUPERADMIN_PASSWORD.decode('utf-8'),
    'roles': ['superadmin', 'normal']
}

# Keehost core configuration
KEEHOST_URL = "http://keehost_api:1337"  # Without trailing '/'
KEEHOST_APIKEY = "toto"  # The same as in the keehost core confgiuration
