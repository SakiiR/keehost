import requests
from .config import SUPERADMIN, KEEHOST_URL, KEEHOST_APIKEY


def create_super_admin():

    """ Create a base super user based on the configuration """

    r = requests.post(KEEHOST_URL + '/accounts',
                      json=SUPERADMIN,
                      headers={'Authorization': KEEHOST_APIKEY})
    if r.status_code == 422:
        print("Super admin already exists")
    elif r.status_code == 201:
        print("Super admin created !")
    else:
        print("Uknown error when creating super admin: %s" % r.json())


def fixtures():

    """ Fixtures entry point """

    create_super_admin()
