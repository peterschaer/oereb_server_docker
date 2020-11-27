import pytest
import requests
import xml.etree.ElementTree as ET

def test_capabilities_json(running_server_instance, config, number_of_municipalities):
    url = running_server_instance + "/capabilities/json"
    res = requests.get(url)
    res_json = res.json()
    number_of_topics_config = len(config['pyramid_oereb']['plrs'])
    number_of_topics_json = len(res_json['GetCapabilitiesResponse']['topic'])
    number_of_municipalities_json = len(res_json['GetCapabilitiesResponse']['municipality'])
    assert res.status_code == 200
    assert number_of_topics_json == number_of_topics_config
    assert number_of_municipalities_json == number_of_municipalities
    assert res_json['GetCapabilitiesResponse']['crs'][0].lower() == "epsg:2056"

def test_capabilities_xml_explicit(running_server_instance, config, number_of_municipalities):
    url = running_server_instance + "/capabilities/xml"
    res = requests.get(url)
    xml_root = ET.fromstring(res.text)
    number_of_topics_config = len(config['pyramid_oereb']['plrs'])
    number_of_topics_xml = len(xml_root.findall("{http://schemas.geo.admin.ch/V_D/OeREB/1.0/Extract}topic"))
    number_of_municipalities_xml = len(xml_root.findall("{http://schemas.geo.admin.ch/V_D/OeREB/1.0/Extract}municipality"))
    assert res.status_code == 200
    assert number_of_topics_xml == number_of_topics_config
    assert number_of_municipalities_xml == number_of_municipalities
    assert xml_root.findall("{http://schemas.geo.admin.ch/V_D/OeREB/1.0/Extract}crs")[0].text.lower() == "epsg:2056"

def test_capabilities_xml_implicit(running_server_instance, config, number_of_municipalities):
    url = running_server_instance + "/capabilities"
    res = requests.get(url)
    xml_root = ET.fromstring(res.text)
    number_of_topics_config = len(config['pyramid_oereb']['plrs'])
    number_of_topics_xml = len(xml_root.findall("{http://schemas.geo.admin.ch/V_D/OeREB/1.0/Extract}topic"))
    number_of_municipalities_xml = len(xml_root.findall("{http://schemas.geo.admin.ch/V_D/OeREB/1.0/Extract}municipality"))
    assert res.status_code == 200
    assert number_of_topics_xml == number_of_topics_config
    assert number_of_municipalities_xml == number_of_municipalities
    assert xml_root.findall("{http://schemas.geo.admin.ch/V_D/OeREB/1.0/Extract}crs")[0].text.lower() == "epsg:2056"