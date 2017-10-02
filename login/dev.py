#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from keehost_login import app, wait_for_keehost_core, fixtures
from keehost_login.config import (API_PORT, API_HOST)


def main():

    """ Main process """

    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
        wait_for_keehost_core()
        fixtures()
    app.run(debug=True, port=API_PORT, host=API_HOST)


if __name__ == "__main__":
    main()
