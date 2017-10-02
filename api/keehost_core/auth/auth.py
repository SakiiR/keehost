from eve.auth import TokenAuth
from flask import current_app as app


class RolesAuth(TokenAuth):

    """ Docstring for RolesAuth. """

    def check_auth(self, token, allowed_roles, resource, method):

        """ When a user try to access a specified resource """

        GENERIC_TOKEN = app.config['GENERIC_TOKEN']
        if token == GENERIC_TOKEN:  # Server2Server Auth
            return True
        accounts = app.data.driver.db['accounts']
        lookup = {'token': token}
        if allowed_roles:
            lookup['roles'] = {'$in': allowed_roles}
        account = accounts.find_one(lookup)
        if account and '_id' in account:
            self.set_request_auth_value(account['_id'])
        return account
