FROM python:3-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/

ENV TZ=Europe/Paris
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN set -ex \
        && buildDeps=' \
            curl \
            gcc \
            libbz2-dev \
            libc6-dev \
            libncurses-dev \
            libreadline-dev \
            libsqlite3-dev \
            libssl-dev \
            make \
            xz-utils \
            zlib1g-dev \
        ' \
        && apt-get update && apt-get install -y $buildDeps libxml2-dev libxslt-dev --no-install-recommends && rm -rf /var/lib/apt/lists/* \
        && pip install --upgrade pip \
        && pip install uwsgi \
        && pip install -r requirements.txt \
        && apt-get purge -y --auto-remove $buildDeps

COPY . /usr/src/app
VOLUME /usr/src/app/config/
EXPOSE 1338
CMD ["uwsgi", "--http-socket", "0.0.0.0:1338", "--wsgi-file", "/usr/src/app/wsgi.py", "--callable", "uwsgiapp", "--master", "--processes", "4", "--threads", "2"]
