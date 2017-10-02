#!/usr/bin/env python
# -*- coding: utf-8 -*-

from keehost_core.logger import init_logger
from keehost_core.app import app


class UWSGIApp(object):

    ''' WSGI app Wrapper '''

    def __call__(self, *args, **kwargs):

        init_logger(app)
        return app(*args, **kwargs)

uwsgiapp = UWSGIApp()
