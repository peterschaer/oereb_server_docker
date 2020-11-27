import requests
import pytest

#@pytest.mark.xfail(condition="config.getoption('--env')!='dev'", reason="Pyramid-Defaultseite wird in test/prod noch angezeigt (s. #5664)")
def test_server_root(running_server_instance):
    res = requests.get(running_server_instance)
    assert res.status_code == 404

def test_invalid_url(running_server_instance):
    res = requests.get(running_server_instance + "/irgendwas/irgendwo")
    assert res.status_code == 404

def test_config_valid(config):
    schema_name = config['pyramid_oereb']['app_schema']['name']
    assert schema_name == "pyramid_oereb_main"