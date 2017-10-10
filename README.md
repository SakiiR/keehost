# KeeHost

A Self Hosted Password Manager API

## Introduction

KeeHost is a self hostable API, it works with Python EVE and store your password in one place. Forget the multi client synchronization, everything is encrypted in the cloud.

## Configuration

Just run `configure.sh` then edit configuration files in the `config/` directory

## Usage

Keehost is a REST API each resources are available via his name as endpoint :

1. */accounts* (List of accessible account)
2. */groups* (A group is gathering one or more entries)
3. */entries* (An entry is a stored encrypted password)


For example, to list accounts:

```sh
curl -X GET 'http://host:port/accounts'
```

to create a group :
```sh
curl -X POST 'http://host:port/groups' -d '{"name": "foo", "icon": null}' -H 'Content-Type: application/json'
```

to get a group:
```sh
curl -X GET 'http://host:port/groups/:id'
```

to delete a group :
```sh
curl -X DELETE 'http://host:port/groups/:id' -H 'If-Match: etag'
```

to update a group :
```sh
curl -X PATCH 'http://host:port/groups/:id' -H 'If-Match: etag' -d '{"name": "foo_updated"}' -H 'Content-Type: application/json'
```

For more example/documentation see the [Python-Eve documentation](http://python-eve.org)

## Deployment

You can deploy the API thanks to the `docker-compose.yml` but don't forget to configure the application correctly !

```python
MONGO_HOST = 'mongo'
KEEHOST_URL = 'http://keehost_api:1337'
```

After the deployment, an nginx will be running on port *80* exposed on host port *8080* (e.g see docker-compose.yml).

This nginx server is used as proxy pass to redirect all the request on the good service.

Example:

```sh
$ curl 'http://localhost:8080/auth/login'

$ curl 'http://localhost:8080/api/entries'
```
