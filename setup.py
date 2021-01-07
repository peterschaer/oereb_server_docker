# -*- coding: utf-8 -*-
import setuptools
import os
import codecs

def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), 'r') as fp:
        return fp.read()

def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith('__version__'):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")

setuptools.setup(
    name='oereb_server',
    packages=setuptools.find_packages(),
    version = get_version("oereb_server/__init__.py"),
    include_package_data=True,
    install_requires=['Paste', 'Mako', 'c2cwsgiutils', 'pyramid_oereb[recommend]==1.8.0'],
    author='Peter Schär, Amt für Geoinformation des Kantons Bern',
    author_email='peter.schaer@be.ch',
    description='Implementierung von pyramid_oereb für den ÖREB-Kataster des Kantons Bern.',
    url='https://www.be.ch/oerebk',
    zip_safe=False,
    entry_points={
        'paste.app_factory': [
            'main = oereb_server:main',
        ],
    },
)
