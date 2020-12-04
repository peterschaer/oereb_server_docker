# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from pyramid.httpexceptions import HTTPNotFound
from pyramid.httpexceptions import HTTPOk

def get_parameter_value(possible_parameter_names, request):

    value = None

    for possible_parameter_name in possible_parameter_names:
        if request.GET.__contains__(possible_parameter_name):
            value = request.GET.get(possible_parameter_name)

    return value

@view_config(route_name='wo_redirect')
def wo_redirect(request):
    egrid = get_parameter_value(['egrid', 'EGRID', 'Egrid'], request)
    language = get_parameter_value(['lang','LANG','Lang'], request)
    base_url = 'https://www.oereb.apps.be.ch'
    if 'a4pu' in request.host_url:
        base_url = 'https://www.oereb-test.apps.be.ch'
    if egrid is not None and language is not None:
        extract_query_string = '/extract/reduced/pdf/%s?LANG=%s' % (egrid, language)
        extract_url = base_url + extract_query_string
        return HTTPFound(location=extract_url)
    else:
        return HTTPNotFound()
