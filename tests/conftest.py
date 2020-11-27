import pytest
import codecs
import yaml
import psycopg2

@pytest.fixture(scope="module")
def config():
    with codecs.open(r"E:\Daten\repos\oereb_server\pyramid_oereb_standard.yml", "r", "utf-8") as cf:
        return yaml.load(cf, Loader=yaml.FullLoader)

@pytest.fixture(scope="module")
def version():
    with codecs.open(r"E:\Daten\repos\oereb_server\oereb_server\__init__.py") as vf:
        for line in vf.read().splitlines():
            if line.startswith('__version__'):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
        else:
            raise RuntimeError("Unable to find version string.")


@pytest.fixture(scope="module")
def app_schema_name(config):
    return config['pyramid_oereb']['app_schema']['name']

@pytest.fixture(scope="module")
def db_connection_string(config):
    return config['pyramid_oereb']['app_schema']['db_connection']

@pytest.fixture(scope="module")
def largest_area_parcel(db_connection_string, app_schema_name):
    with psycopg2.connect(db_connection_string) as conn:
        with conn.cursor() as cur:
            sql = "SELECT egrid FROM %s.real_estate order by land_registry_area desc limit 1" % (app_schema_name)
            cur.execute(sql)
            return cur.fetchone()[0]

@pytest.fixture(scope="module")
def complex_area_parcel(db_connection_string, app_schema_name):
    with psycopg2.connect(db_connection_string) as conn:
        with conn.cursor() as cur:
            sql = 'SELECT egrid FROM %s.real_estate order by st_npoints("limit") desc limit 1' % (app_schema_name)
            cur.execute(sql)
            return cur.fetchone()[0]

@pytest.fixture(scope="module")
def running_server_instance(environment):
    server = "http://localhost:6543"
    if environment == 'test':
        server = 'https://www.oereb-test.apps.be.ch'
    elif environment == 'prod':
        server = 'https://www.oereb.apps.be.ch'
    elif environment == 'prod1':
        server = 'http://a4pa-www-oerebpyramid001.infra.be.ch'
    elif environment == 'prod2':
        server = 'http://a4pa-www-oerebpyramid002.infra.be.ch'
    return server

@pytest.fixture(scope="module")
def egrid_without_plr():
    return "CH401435854634"

@pytest.fixture(scope="module")
def egrid_with_some_plr():
    return "CH613515467670"

@pytest.fixture(scope="module")
def egrid_large_geometries_error():
    return "CH173515254641"    

@pytest.fixture(scope="module")
def number_of_municipalities(db_connection_string, app_schema_name):
    with psycopg2.connect(db_connection_string) as conn:
        with conn.cursor() as cur:
            sql = 'select count(*) from %s.municipality' % (app_schema_name)
            cur.execute(sql)
            return cur.fetchone()[0]

@pytest.fixture(scope="module")
def random_egrids(db_connection_string, app_schema_name):
    with psycopg2.connect(db_connection_string) as conn:
        with conn.cursor() as cur:
            sql = 'SELECT egrid from %s.real_estate ORDER BY RANDOM() LIMIT 10' % (app_schema_name)
            cur.execute(sql)
            return [egrid[0] for egrid in cur.fetchall()]

def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="dev", help="Eines von dev, test, prod", choices=['dev', 'test', 'prod', 'prod1', 'prod2'])

@pytest.fixture(scope="module")
def environment(pytestconfig):
    return pytestconfig.getoption("--env")

@pytest.fixture(scope="module")
def egrids_for_concurrent_error():
    return ('CH594607413563', 'CH804335484602')