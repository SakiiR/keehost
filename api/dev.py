#!/usr/bin/env python

import logging
import os
from sys import stdout
from keehost_core import app, init_logger
from keehost_core.config import APP_HOST, APP_PORT

def main():

    """ Main Process """

    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        init_logger(app)
    app.run(host=APP_HOST, port=APP_PORT, debug=True)


if __name__ == "__main__":
    main()
