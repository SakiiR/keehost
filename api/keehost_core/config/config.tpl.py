# Eve Configuration File

# Mongo Configuration
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'keehost'
MONGO_URI = "mongodb://{host}:{port}/{dbname}".format(host=MONGO_HOST,
                                                      port=MONGO_PORT,
                                                      dbname=MONGO_DBNAME)

# The adress to bind to
APP_HOST = "0.0.0.0"

# The port on which listen
APP_PORT = 1337

# Must be a totally generated random token ! server to server token
GENERIC_TOKEN = ''

# Enable SOFT DELETE
SOFT_DELETE = True

ITEM_METHODS = ['PATCH', 'DELETE', 'GET']
RESOURCE_METHODS = ['POST', 'DELETE', 'GET']

EXTENDED_MEDIA_INFO = ['content_type', 'name', 'length']

LIST_OF_ACCOUNTS = {
    'type': 'list',
    'default': [],
    'schema': {
        'type': 'objectid',
        'data_relation': {
            'resource': 'accounts',
            'field': '_id',
        },
    }
}

# Resources definition
DOMAIN = {
    'accounts': {
        'allowed_roles': ['superadmin'],
        'schema': {
            'firstname': {
                'type': 'string',
                'required': True,
            },
            'lastname': {
                'type': 'string',
                'required': True
            },
            'username': {
                'type': 'string',
                'required': True,
                'unique': True
            },
            'token': {
                'type': 'string',
                'required': True,
                'nullable': True,
                'default': None
            },
            'email': {
                'type': 'string',
                'required': True,
                'unique': True
            },
            'password': {
                'type': 'string',
                'required': True
            },
            'roles': {
                'type': 'list',
                'required': True
            }
        }
    },

    'groups': {
        'allowed_roles': ['normal'],
        'schema': {
            'name': {
                'type': 'string',
                'required': True
            },
            'w_reads': LIST_OF_ACCOUNTS,
            'w_writes': LIST_OF_ACCOUNTS,
            'icon': {
                'type': 'media',
                'required': False,
                'nullable': True,
                'default': None
            }
        }
    },

    'entries': {
        'allowed_roles': ['normal'],
        'w_reads': LIST_OF_ACCOUNTS,
        'w_writes': LIST_OF_ACCOUNTS,
        'schema': {
            'name': {
                'type': 'string',
                'required': True
            },
            'value': {
                'type': 'string',
                'required': True
            },
            'key': {
                'type': 'string',
                'required': True
            },
            'url': {
                'type': 'string',
                'required': False
            },
            'icon': {
                'type': 'media',
                'required': False,
                'nullable': True,
                'default': None
            },
            'group': {
                'type': 'objectid',
                'required': True,
                'data_relation': {
                    'resource': 'groups',
                    'embeddable': True
                }
            },
        }
    },
}
