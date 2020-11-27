import requests
import xml.etree.ElementTree as ET
import pytest

def test_versions_json(running_server_instance):
    url = running_server_instance + "/versions/json"
    res = requests.get(url)
    res_json = res.json()
    number_of_versions_json = len(res_json['GetVersionsResponse']['supportedVersion'])
    assert res.status_code == 200
    assert number_of_versions_json == 1

def test_versions_xml_explicit(running_server_instance):
    url = running_server_instance + "/versions/xml"
    res = requests.get(url)
    xml_root = ET.fromstring(res.text)
    number_of_versions_xml = len(xml_root.findall("{http://schemas.geo.admin.ch/V_D/OeREB/1.0/Versioning}supportedVersion"))
    assert res.status_code == 200
    assert number_of_versions_xml == 1

def test_versions_xml_implicit(running_server_instance):
    url = running_server_instance + "/versions"
    res = requests.get(url)
    xml_root = ET.fromstring(res.text)
    number_of_versions_xml = len(xml_root.findall("{http://schemas.geo.admin.ch/V_D/OeREB/1.0/Versioning}supportedVersion"))
    assert res.status_code == 200
    assert number_of_versions_xml == 1
