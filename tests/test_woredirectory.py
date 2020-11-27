import requests
import pytest

@pytest.mark.xfail(condition="config.getoption('--env')=='dev'", reason="wo_redirector funktioniert auf localhost nicht (fehlender Apache)")
def test_valid_egrid_de(running_server_instance, egrid_with_some_plr):
    url = running_server_instance + "/wo_redirect?egrid=%s&lang=de" % (egrid_with_some_plr)
    res = requests.get(url)
    assert res.status_code == 200
    assert res.history[0].status_code == 302
    assert res.headers['Content-Type'] == "application/pdf"

@pytest.mark.xfail(condition="config.getoption('--env')=='dev'", reason="wo_redirector funktioniert auf localhost nicht (fehlender Apache)")
def test_valid_egrid_fr(running_server_instance, egrid_with_some_plr):
    url = running_server_instance + "/wo_redirect?egrid=%s&lang=fr" % (egrid_with_some_plr)
    res = requests.get(url)
    assert res.status_code == 200
    assert res.history[0].status_code == 302
    assert res.headers['Content-Type'] == "application/pdf"

@pytest.mark.xfail(condition="config.getoption('--env')=='dev'", reason="wo_redirector funktioniert auf localhost nicht (fehlender Apache)")
def test_invalid_egrid_de(running_server_instance):
    url = running_server_instance + "/wo_redirect?egrid=666&lang=de"
    res = requests.get(url)
    assert res.status_code == 204

@pytest.mark.xfail(condition="config.getoption('--env')=='dev'", reason="wo_redirector funktioniert auf localhost nicht (fehlender Apache)")
def test_version_correct(running_server_instance, version):
    url = running_server_instance + "/wo_redirect?version=xxx"
    res = requests.get(url)
    assert res.status_code == 200
    assert res.json()['version'] == version