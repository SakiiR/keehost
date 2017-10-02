# -*- coding: utf-8 -*-

import coloredlogs
from sys import stdout
import logging


def init_logger(app):

    ''' Init the logger with the eve app given
        in parameters

        >>> # With Eve App
        >>> from flask import current_app as app
        >>> app.logger.info("test")
        test
        >>> import logging
        >>> logging.getLogger('eve').info("test")
        test

        :param app the eve app
    '''

    coloredlogs.install(level='DEBUG', logger=app.logger)
    app.logger.setLevel(logging.DEBUG)
