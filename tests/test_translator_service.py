from unittest.mock import patch

import pytest

from src.exceptions import ValidationError
from src.services.translator_service import (
    translate_text,
)


def test_empty_text():

    with pytest.raises(ValidationError):
        translate_text(
            "",
            "Arabic",
        )


def test_empty_target_language():

    with pytest.raises(ValidationError):
        translate_text(
            "Hello",
            "",
        )


def test_whitespace_text():

    with pytest.raises(ValidationError):
        translate_text(
            "   ",
            "Arabic",
        )


def test_whitespace_target_language():

    with pytest.raises(ValidationError):
        translate_text(
            "Hello",
            "   ",
        )


@patch(
    "src.services.translator_service.generate_text"
)
def test_translate_text(mock_generate_text):

    mock_generate_text.return_value = "مرحبا"

    result = translate_text(
        text="Hello",
        target_language="Arabic",
    )

    assert result == "مرحبا"

    mock_generate_text.assert_called_once()