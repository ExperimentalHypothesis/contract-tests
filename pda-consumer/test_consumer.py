import pytest
from pact import Consumer, Provider
import requests
import os

print("in module test_consumer")

@pytest.fixture(scope="module")
def pact():
    consumer = Consumer('PDA')
    provider = Provider('OOR')
    pact_dir = ".././pacts"  # THIS WILL BE IN THE BROER SOMEHOW
    os.makedirs(pact_dir, exist_ok=True)
    pact = consumer.has_pact_with(provider, host_name='localhost', port=1234, pact_dir=pact_dir)
    pact.start_service()
    yield pact
    pact.stop_service()

def test_get_order(pact):
    expected = {
        'id': 1,
        'items': [
            {'name': 'burgera', 'quantity': 2, 'value': 100.0}
        ]
    }

    (pact
     .given('order with ID 1 exists')
     .upon_receiving('a request for order 1')
     .with_request(method='GET', path='/orders/1')
     .will_respond_with(200, body=expected))

    with pact:
        result = requests.get('http://localhost:1234/orders/1')
        assert result.json() == expected
