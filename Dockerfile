FROM alpine:3.12.1

WORKDIR /usr/src

RUN apk add --no-cache bash git build-base python3 python3-dev geos geos-dev libffi libffi-dev libxml2 libxml2-dev libxslt libxslt-dev postgresql-dev libc-dev gcc tini su-exec

RUN python3 -m ensurepip

RUN pip3 install wheel setuptools

RUN git clone https://github.com/peterschaer/oereb_server_docker.git

WORKDIR /usr/src/oereb_server_docker

RUN pip3 install --no-cache-dir --requirement requirements.txt

RUN python3 setup.py develop

ENTRYPOINT ["python3", "oereb_server.py"]