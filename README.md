# AI Translator

A Python AI-powered translation application built with the OpenAI API.

## Features

* Translate text into a target language
* Input validation
* Custom application exceptions
* OpenAI integration
* Request timeout
* Retry handling
* Logging
* Unit testing
* Mocking external API calls
* Environment-based configuration

## Architecture

The application follows a simple layered architecture:

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
```

### Component Responsibilities

* `main.py` — Handles user interaction
* `translator_service.py` — Contains translation business logic
* `api.py` — Communicates with the OpenAI API
* `config.py` — Manages application configuration
* `exceptions.py` — Defines application-specific errors
* `tests/` — Contains automated tests

## Project Structure

```text
ai-translator/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── api.py
│   ├── exceptions.py
│   ├── utils.py
│   │
│   └── services/
│       ├── __init__.py
│       └── translator_service.py
│
├── tests/
│   ├── test_api.py
│   └── test_translator_service.py
│
├── .env
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

Install the project dependencies:

```bash
pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_api_key_here
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
```

Never commit `.env` to Git.

## Running the Project

Make sure you are in the project root:

```bash
pwd
```

Then run:

```bash
python -m src.main
```

## Testing

### Run all tests

```bash
python -m pytest
```

### Run all tests with detailed output

```bash
python -m pytest -v
```

### Run the translator service tests

```bash
python -m pytest -v tests/test_translator_service.py
```

### Run one specific test

```bash
python -m pytest -v tests/test_translator_service.py::test_empty_text
```

## Example

```text
Enter text to translate: Hello, how are you?
Enter target language: Arabic

Translation
------------------------------
مرحبا، كيف حالك؟
```

## Engineering Practices

This project demonstrates:

* Separation of concerns
* Layered architecture
* Environment-based configuration
* Custom exceptions
* Error handling
* Logging
* Retry handling
* Request timeout
* Unit testing
* Mocking external API calls
* Secure API key management

## Project Status

**Project 1 — AI Translator**

Status: Completed
