from src.api import generate_text
from src.exceptions import ValidationError
from src.utils import clean_text


def translate_text(text:str,target_language:str) -> str:
    text = clean_text(text)
    target_language = clean_text(target_language)

    if not text:
        raise ValidationError("Text can not be empty")
    if not target_language:
        raise ValidationError("Target language can not be empty")

    prompt = f"""
    You are a professional Translator.

    Translae the following text into {target_language}.

    Rules:
    - Preserve the original meaning.
    - Do not add information.
    - Do not remove important information.
    - Use natural language.
    - Return only the translation.

    Text:
    {text}
    """

    return generate_text(prompt)