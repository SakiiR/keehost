import time
import requests
from .config import (KEEHOST_URL, KEEHOST_APIKEY)

def wait_for_keehost_core():

    """ Wait for the keehost core to be up and running """

    t = 1 
    while True:
        try:
            print("Trying to connect to Keehost Core API (%s).." % KEEHOST_URL)
            r = requests.get(KEEHOST_URL + '/accounts', headers={'Authorization': KEEHOST_APIKEY})
            if r.status_code == 200:
                return True
            print("Invalid token supplied ..")
            exit(0)
        except requests.RequestException as e:
            print("Failed to connect to Keehost Core API (%s) .. Waiting %d" % (KEEHOST_URL, t))
            t += 2
        time.sleep(t)
    return True



