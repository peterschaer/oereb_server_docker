###
# app configuration
# https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/environment.html
###

[app:main]
use = egg:oereb_server

pyramid.reload_templates = false
pyramid.debug_authorization = false
pyramid.debug_notfound = false
pyramid.debug_routematch = false
pyramid.default_locale_name = en
pyramid_oereb.cfg.file = pyramid_oereb_standard.yml
pyramid_oereb.cfg.section = pyramid_oereb

###
# wsgi server configuration
###

[server:main]
use = egg:waitress#main
listen = *:6543

###
# logging configuration
# https://docs.pylonsproject.org/projects/pyramid/en/latest/narr/logging.html
###

[loggers]
keys = root, oereb_server, json

[handlers]
keys = console, sqlalchemylogger

[formatters]
keys = generic

[logger_root]
level = WARN
handlers = console

[logger_oereb_server]
level = WARN
handlers =
qualname = oereb_server

[logger_json]
level = INFO
handlers = console, sqlalchemylogger
qualname = JSON
propagate = 0

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[handler_sqlalchemylogger]
class = c2cwsgiutils.sqlalchemylogger.handlers.SQLAlchemyHandler
args = ({'url':'postgresql://${POSTGRES_LOGGER_USER}:${POSTGRES_LOGGER_PASS}@${POSTGRES_LOGGER_HOST}:${POSTGRES_LOGGER_PORT}/${POSTGRES_LOGGER_DATABASE}','tablename':'${POSTGRES_LOGGER_TABLE}','tableargs': {'schema':'${POSTGRES_LOGGER_SCHEMA}'}},'healthcheck')
level = NOTSET
formatter = generic
propagate = 0

[formatter_generic]
format = %(asctime)s %(levelname)-5.5s [%(name)s:%(lineno)s][%(threadName)s] %(message)s
