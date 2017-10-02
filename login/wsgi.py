#!/usr/bin/env python
# -*- coding: utf-8 -*-

from keehost_login import app, wait_for_keehost_core, fixtures
from keehost_login.config import (API_PORT, API_HOST)

class UWSGIApp(object):

    ''' WSGI app Wrapper '''

    def __call__(self, *args, **kwargs):

        wait_for_keehost_core()
        fixtures()
        return app(*args, **kwargs)

uwsgiapp = UWSGIApp()
