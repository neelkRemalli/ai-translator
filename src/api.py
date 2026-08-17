import logging
import time 

from openai import OpenAI 

from src.config import Settings 
from src.exceptions import AIProviderError


logger = logging.getLogger(__name__)

client = OpenAI(
    base_url=Settings.BASE_URL,
    api_key=Settings.API_KEY
    )


def generate_text(prompt:str) -> str:
    for attempt in range(1,Settings.MAX_RETRIES + 1):
        try:
            logger.info(
                "Sending request to OpenAI (Attempt %s)",attempt,
            )
            response = client.responses.create(
             model=Settings.MODEL_NAME,
             input=prompt,
             timeout=Settings.REQUEST_TIMEOUT,
            )
            logger.info(
                "Response received from OpenAi"
             )
            
            return response.output_text

        except Exception as error:
            logger.warning(
                "OpenAI request failed on attempt %s: %s",attempt,error,
            )
            
            if attempt == Settings.MAX_RETRIES:
                logger.error(
                    "All OpenAI attempts failed"
                )
                raise AIProviderError(
                    "Failed to communicate with AI provider"
                ) from error

            time.sleep(2)




           
