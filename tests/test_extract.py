import pytest
import requests
import concurrent.futures
import threading

def test_largest_area_extract_json(running_server_instance, largest_area_parcel):
    extract_url = running_server_instance + "/extract/reduced/json/" + largest_area_parcel
    res = requests.get(extract_url)
    assert res.status_code == 200
    assert 'GetExtractByIdResponse' in res.json().keys()

def test_largest_area_extract_pdf(running_server_instance, largest_area_parcel):
    extract_url = running_server_instance + "/extract/reduced/pdf/" + largest_area_parcel
    res = requests.get(extract_url)
    assert res.status_code == 200

def test_parcel_without_plr_json(running_server_instance, egrid_without_plr):
    extract_url = running_server_instance + "/extract/reduced/json/" + egrid_without_plr
    res = requests.get(extract_url)
    assert res.status_code == 200
    assert len(res.json()['GetExtractByIdResponse']['extract']['ConcernedTheme']) == 0

def test_complex_extract_json(running_server_instance, complex_area_parcel):
    extract_url = running_server_instance + "/extract/reduced/json/" + complex_area_parcel
    res = requests.get(extract_url)
    assert res.status_code == 200
    assert 'GetExtractByIdResponse' in res.json().keys()

def test_complex_extract_pdf(running_server_instance, complex_area_parcel):
    extract_url = running_server_instance + "/extract/reduced/pdf/" + complex_area_parcel
    res = requests.get(extract_url)
    assert res.status_code == 200

@pytest.mark.xfail(reason="Extract FULL funktioniert nicht vollständig (s. #2479).")
def test_full_extract_pdf(running_server_instance, egrid_with_some_plr):
    extract_url = running_server_instance + "/extract/full/pdf/" + egrid_with_some_plr
    res = requests.get(extract_url)
    assert res.status_code == 200

def test_large_geometry_error_extract_pdf(running_server_instance, egrid_large_geometries_error):
    # Gewisse Auszüge übergeben mapfish_print ein riesiges JSON wegen der Geometrie
    # Wenn das JSON zu gross ist, stürzt mapfish_print ab (#6930)
    extract_url = running_server_instance + "/extract/reduced/pdf/" + egrid_large_geometries_error
    extract_url_getspec = extract_url + "?getspec=true"
    res = requests.get(extract_url)
    res_getspec = requests.get(extract_url_getspec)
    assert res.status_code == 200
    assert len(res_getspec.text)/1024/1024 < 1

def test_invalid_egrid(running_server_instance):
    extract_url = running_server_instance + "/extract/reduced/json/666"
    res = requests.get(extract_url)
    assert res.status_code == 204

def test_random_egrids(running_server_instance, random_egrids):
    for egrid in random_egrids:
        extract_url_json = running_server_instance + "/extract/reduced/json/" + egrid
        extract_url_pdf = running_server_instance + "/extract/reduced/pdf/" + egrid
        res_json = requests.get(extract_url_json)
        res_pdf = requests.get(extract_url_pdf)
        assert res_json.status_code == 200
        assert res_pdf.status_code == 200
