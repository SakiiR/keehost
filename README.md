# KeeHost

A Self Hosted Password Manager API

## Introduction

KeeHost is a self hostable API, it works with Python EVE and store your password in one place. Forget the multi client synchronization, everything is encrypted in the cloud.

## Configuration

Just run `configure.sh` then edit configuration files in the `config/` directory

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
