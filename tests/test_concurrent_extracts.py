import pytest
import requests
import concurrent.futures
import threading

thread_local = threading.local()

# Testet, ob bei parallelen Requests keine Vermischungen stattfinden (s. #6725)
@pytest.mark.xfail(condition="config.getoption('--env')!='dev'", reason="Concurrent Fehler aus #6725 nur auf dev behoben.")
def test_concurrent_requests(running_server_instance, egrids_for_concurrent_error):
    slow_egrid, fast_egrid = egrids_for_concurrent_error
    slow_extract_url = running_server_instance + "/extract/reduced/json/" + slow_egrid
    fast_extract_url = running_server_instance + "/extract/reduced/json/" + fast_egrid

    res_slow = requests.get(slow_extract_url)
    res_fast = requests.get(fast_extract_url)

    plr_count_slow = len(res_slow.json()['GetExtractByIdResponse']['extract']['RealEstate']['RestrictionOnLandownership'])
    plr_count_fast = len(res_fast.json()['GetExtractByIdResponse']['extract']['RealEstate']['RestrictionOnLandownership'])

    sequential_result = {
        slow_egrid: plr_count_slow,
        fast_egrid: plr_count_fast
    }

    concurrent_result = {}

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for result in executor.map(count_plr_in_json_extract, [slow_extract_url, fast_extract_url]):
            egrid, number_of_plrs = result
            concurrent_result[egrid] = number_of_plrs
    
    print(concurrent_result)
    print(sequential_result)

    assert sequential_result[slow_egrid] == concurrent_result[slow_egrid]
    assert sequential_result[fast_egrid] == concurrent_result[fast_egrid]

def count_plr_in_json_extract(url):
    result = requests.get(url)
    json = result.json()
    number_of_plrs = len(json['GetExtractByIdResponse']['extract']['RealEstate']['RestrictionOnLandownership'])
    egrid = json['GetExtractByIdResponse']['extract']['RealEstate']['EGRID']
    return (egrid, number_of_plrs)

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session