# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPOk
import json
from oereb_server import __version__

@view_config(route_name='version')
def version(request):
    version_json = json.dumps({"version": __version__})
    return HTTPOk(body=version_json, content_type='application/json', charset='UTF-8')