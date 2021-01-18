FROM python:3.6.12-slim-buster

WORKDIR /usr/src
RUN mkdir oereb_server
WORKDIR /usr/src/oereb_server

COPY ./dev-requirements.txt .
COPY development.mako .
COPY run_oereb_server.py .
COPY production.mako .
COPY pyramid_oereb_standard.mako .
COPY requirements.txt .
COPY setup.py .
COPY ./oereb_server/. ./oereb_server/.

RUN apt update && \
    DEV_PACKAGES="build-essential libgeos-dev" && \
    DEBIAN_FRONTEND=noninteractive apt install --yes --no-install-recommends \
        libgeos-c1v5 gosu tini ${DEV_PACKAGES} && \
    pip install --disable-pip-version-check --no-cache-dir --requirement requirements.txt && \
    apt remove --purge --autoremove --yes ${DEV_PACKAGES} binutils && \
    apt-get clean && \
    rm --force --recursive /var/lib/apt/lists/*

RUN python setup.py develop

ENTRYPOINT ["python", "run_oereb_server.py"]