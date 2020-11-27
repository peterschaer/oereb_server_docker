# -*- coding: utf-8 -*-
from oereb_server import __version__
import oereb_server
import setuptools

setuptools.setup(
    name='oereb_server',
    packages=setuptools.find_packages(),
    version=__version__,
    include_package_data=True,
    install_requires=['plaster_pastedeploy', 'pyramid', 'pyramid_jinja2', 'pyramid_debugtoolbar', 'waitress', 'pyramid_oereb[recommend]==1.8.0'],
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
