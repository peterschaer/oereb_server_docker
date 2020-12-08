FROM alpine:3.12.1

WORKDIR /usr/src
RUN mkdir oereb_server
WORKDIR /usr/src/oereb_server

COPY ./dev-requirements.txt .
COPY development.ini .
COPY run_oereb_server.py .
COPY production.ini .
COPY pyramid_oereb_standard.mako .
COPY requirements.txt .
COPY setup.py .
COPY ./oereb_server/. ./oereb_server/.

RUN apk add --no-cache build-base python3 python3-dev geos geos-dev libffi libffi-dev libxml2 libxml2-dev libxslt libxslt-dev postgresql-dev libc-dev gcc tini su-exec
RUN python3 -m ensurepip
RUN pip3 install wheel setuptools
RUN pip3 install --no-cache-dir --requirement requirements.txt
RUN python3 setup.py develop

ENTRYPOINT ["python3", "run_oereb_server.py"]