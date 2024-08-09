# Contract Testing with Pact using FastAPI Services

## Overview
This repository demonstrates how to implement contract testing using Pact for FastAPI services. The OOR service acts as the provider, while the PDA service acts as the consumer. 


## Setup Instructions
### 1. Clone the Repository
```bash
git clone
cd
pip install -r requirements.txt
```

### 2. Run services
```
python oor-producer/oor.py
python pda-consumer/pda.py
```

### 3. Run tests
```
pytest pda-consumer/test_consumer.py # this needs to be run first
pytest oor-producer/test_producer.py
```

## Workflow diagram
[Consumer Test] -> [Generate Pact File] -> [Provider Test] -> [Verify Provider Against Pact]

-------

## TODO
The setup does not include generating and verifying pacts using GitLab CI/CD pipelines. Use Pact Broker for that. Here the required workflow

[Consumer Team CI/CD Pipeline]

1. Run consumer tests to generate pact file.
2. Publish pact file to Pact Broker.

[Pact Broker]

3. Store and version control pact files.

[Provider Team CI/CD Pipeline]

4. Fetch latest pacts from Pact Broker.
5. Run provider verification tests against fetched pacts.
