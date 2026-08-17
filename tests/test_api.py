from unittest.mock import Mock, patch

import pytest

from src.api import generate_text
from src.exceptions import AIProviderError


@patch("src.api.client.responses.create")
def test_generate_text_success(mock_create):

    response = Mock()
    response.output_text = "مرحبا"

    mock_create.return_value = response

    result = generate_text(
        "Translate Hello into Arabic."
    )

    assert result == "مرحبا"

    mock_create.assert_called_once()


@patch("src.api.time.sleep")
@patch("src.api.client.responses.create")
def test_generate_text_retries_then_succeeds(
    mock_create,
    mock_sleep,
):

    response = Mock()
    response.output_text = "مرحبا"

    mock_create.side_effect = [
        Exception("Temporary failure"),
        Exception("Temporary failure"),
        response,
    ]

    result = generate_text(
        "Translate Hello into Arabic."
    )

    assert result == "مرحبا"

    assert mock_create.call_count == 3
    assert mock_sleep.call_count == 2


@patch("src.api.time.sleep")
@patch("src.api.client.responses.create")
def test_generate_text_fails_after_retries(
    mock_create,
    mock_sleep,
):

    mock_create.side_effect = Exception(
        "API unavailable"
    )

    with pytest.raises(AIProviderError):
        generate_text(
            "Translate Hello into Arabic."
        )

    assert mock_create.call_count == 3
    assert mock_sleep.call_count == 2