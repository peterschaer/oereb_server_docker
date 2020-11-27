import requests
import xml.etree.ElementTree as ET
import pytest

#############
# GETEGRID XY
#############
def test_getegrid_valid_xy_single_json(running_server_instance):
    url = running_server_instance + "/getegrid/json/?XY=2600000,1200000"
    res = requests.get(url)
    res_json = res.json()
    assert res.status_code == 200
    assert len(res_json['GetEGRIDResponse']) == 1

def test_getegrid_invalid_xy_single_json(running_server_instance):
    url = running_server_instance + "/getegrid/json/?XY=0,0"
    res = requests.get(url)
    assert res.status_code == 204

def test_getegrid_valid_xy_multiple_json(running_server_instance):
    url = running_server_instance + "/getegrid/json/?XY=2599175.1,1199196.2"
    res = requests.get(url)
    res_json = res.json()
    assert res.status_code == 200
    assert len(res_json['GetEGRIDResponse']) == 2

def test_getegrid_valid_xy_single_xml(running_server_instance):
    url = running_server_instance + "/getegrid/xml/?XY=2600000,1200000"
    res = requests.get(url)
    xml_root = ET.fromstring(res.text)
    assert res.status_code == 200
    assert len(xml_root.findall("{http://schemas.geo.admin.ch/V_D/OeREB/1.0/Extract}egrid")) == 1

def test_getegrid_invalid_xy_single_xml(running_server_instance):
    url = running_server_instance + "/getegrid/xml/?XY=0,0"
    res = requests.get(url)
    assert res.status_code == 204

def test_getegrid_valid_xy_multiple_xml(running_server_instance):
    url = running_server_instance + "/getegrid/xml/?XY=2599175.1,1199196.2"
    res = requests.get(url)
    xml_root = ET.fromstring(res.text)
    assert res.status_code == 200
    assert len(xml_root.findall("{http://schemas.geo.admin.ch/V_D/OeREB/1.0/Extract}egrid")) == 2

###############
# GETEGRID GNSS
###############
def test_getegrid_valid_gnss_single_json(running_server_instance):
    url = running_server_instance + "/getegrid/json/?GNSS=46.95108,7.43863"
    res = requests.get(url)
    res_json = res.json()
    assert res.status_code == 200
    assert len(res_json['GetEGRIDResponse']) == 1

def test_getegrid_invalid_gnss_single_json(running_server_instance):
    url = running_server_instance + "/getegrid/json/?GNSS=0,0"
    res = requests.get(url)
    assert res.status_code == 204

def test_getegrid_valid_gnss_multiple_json(running_server_instance):
    url = running_server_instance + "/getegrid/json/?GNSS=46.94387,7.42781"
    res = requests.get(url)
    res_json = res.json()
    assert res.status_code == 200
    assert len(res_json['GetEGRIDResponse']) == 2

def test_getegrid_valid_gnss_single_xml(running_server_instance):
    url = running_server_instance + "/getegrid/xml/?GNSS=46.95108,7.43863"
    res = requests.get(url)
    xml_root = ET.fromstring(res.text)
    assert res.status_code == 200
    assert len(xml_root.findall("{http://schemas.geo.admin.ch/V_D/OeREB/1.0/Extract}egrid")) == 1

def test_getegrid_invalid_gnss_single_xml(running_server_instance):
    url = running_server_instance + "/getegrid/xml/?GNSS=0,0"
    res = requests.get(url)
    assert res.status_code == 204

def test_getegrid_valid_gnss_multiple_xml(running_server_instance):
    url = running_server_instance + "/getegrid/xml/?GNSS=46.94387,7.42781"
    res = requests.get(url)
    xml_root = ET.fromstring(res.text)
    assert res.status_code == 200
    assert len(xml_root.findall("{http://schemas.geo.admin.ch/V_D/OeREB/1.0/Extract}egrid")) == 2

##################
# GETEGRID IDENTDN
##################
def test_getegrid_valid_identdn_json(running_server_instance):
    url = running_server_instance + "/getegrid/json/BE0200000043/698"
    res = requests.get(url)
    res_json = res.json()
    assert res.status_code == 200
    assert len(res_json['GetEGRIDResponse']) == 1

def test_getegrid_invalid_identdn_json(running_server_instance):
    url = running_server_instance + "/getegrid/json/0/0"
    res = requests.get(url)
    assert res.status_code == 204

def test_getegrid_valid_identdn_xml(running_server_instance):
    url = running_server_instance + "/getegrid/xml/BE0200000043/698"
    res = requests.get(url)
    xml_root = ET.fromstring(res.text)
    assert res.status_code == 200
    assert len(xml_root.findall("{http://schemas.geo.admin.ch/V_D/OeREB/1.0/Extract}egrid")) == 1

def test_getegrid_invalid_identdn_xml(running_server_instance):
    url = running_server_instance + "/getegrid/xml/0/0"
    res = requests.get(url)
    assert res.status_code == 204

##################
# GETEGRID ADDRESS
##################
def test_getegrid_valid_address_json(running_server_instance):
    url = running_server_instance + "/getegrid/json/3011/Reiterstrasse/11"
    res = requests.get(url)
    res_json = res.json()
    assert res.status_code == 200
    assert len(res_json['GetEGRIDResponse']) == 1

def test_getegrid_invalid_address_json(running_server_instance):
    url = running_server_instance + "/getegrid/json/666/somestreet/666"
    res = requests.get(url)
    assert res.status_code == 204

def test_getegrid_valid_address_xml(running_server_instance):
    url = running_server_instance + "/getegrid/xml/3011/Reiterstrasse/11"
    res = requests.get(url)
    xml_root = ET.fromstring(res.text)
    assert res.status_code == 200
    assert len(xml_root.findall("{http://schemas.geo.admin.ch/V_D/OeREB/1.0/Extract}egrid")) == 1

def test_getegrid_invalid_address_xml(running_server_instance):
    url = running_server_instance + "/getegrid/json/666/somestreet/666"
    res = requests.get(url)
    assert res.status_code == 204    