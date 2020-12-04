# -*- coding: utf-8 -*-
from pyramid.config import Configurator

__version__ = '2.2.0'

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')
    config.include('pyramid_oereb')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('wo_redirect', '/wo_redirect')
    config.add_route('version', '/version')
    config.add_route('home', '/')
    config.scan()
    return config.make_wsgi_app()
