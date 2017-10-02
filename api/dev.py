#!/usr/bin/env python

import logging
from sys import stdout
from keehost_core import app
from keehost_core.config import APP_HOST, APP_PORT

def main():

    """ Main Process """

    app.run(host=APP_HOST, port=APP_PORT, debug=True)


if __name__ == "__main__":
    main()
