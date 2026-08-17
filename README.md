#AI Translator

A Python AI-powered translation application built with the OpenAI API.

##Features

- Translate text into a target language

- Input validation

- Custom application exceptions

- OpenAI integration

- Request timeout

- Retry handling

- Logging

- Unit testing

- Mocking external API calls

- Environment-based configuration

##Architecture

```text
User
 │
 ▼
main.py
 │
 ▼
translator_service.py
 │
 ▼
api.py
 │
 ▼
OpenAI


##Running the Project

Make sure you are in the project root:

```bash

python -m src.main

##Run all tests:

python -m pytest

python -m pytest -v

python -m pytest -v tests/test_translator_service.py

python -m pytest -v tests/test_translator_service.py::test_empty_text

