import logging

from src.exceptions import(AIProviderError,ValidationError)
from src.services.translator_service import translate_text

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logger = logging.getLogger(__name__)

def main():
    logger.info("Application started")

    try:
        text = input("Enter text to translate: ")
        target_language = input(" Enter target language: ")

        translation = translate_text(
            text=text,
            target_language=target_language
            )

        logger.info("Translation completed")

        print("\nTransaltion")
        print("-" * 30)
        print(translation)
    
    except Exception:
        logger.exception("Unexpected application error")
        print("Unexpected Error: ", "Something went wrong")



if __name__ == "__main__":
    main()
     