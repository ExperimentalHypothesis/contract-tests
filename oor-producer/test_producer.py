from pact import Verifier

def test_provider():
    print("testing provider")
    verifier = Verifier(provider='OOR', provider_base_url='http://localhost:8000')
    pact_file = '.././pacts/pda-oor.json'
    output, logs = verifier.verify_pacts(pact_file)
    assert output == 0, f"Provider verification failed: {logs}"
