# -*- coding: utf-8 -*-
from pyramid.view import view_config
from pyramid.httpexceptions import HTTPOk
from pyramid_oereb.contrib.stats.decorators import log_response
import json
from oereb_server import __version__

@view_config(route_name='version', decorator=log_response)
def version(request):
    version_json = json.dumps({"version": __version__})
    return HTTPOk(body=version_json, content_type='application/json', charset='UTF-8')