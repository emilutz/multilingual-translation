import asyncio

from googletrans import Translator, models

from translators.base_translator import BaseTranslator
from constants import Language


class GoogleTranslator(BaseTranslator):
    """Text translator based on the Google Translate Engine."""

    def __init__(
            self,
            source_language: Language,
            target_language: Language,
            service_urls: list | None = None,
        ):
        """Initialize the translator.
        
        Args:
            source_language: The language to translate from.
            target_language: The language to translate into.
        """
        super().__init__(source_language, target_language)

        if service_urls is None:
            self.service_urls = ["translate.googleapis.com"]
        else:
            self.service_urls = service_urls

    def translate(self, text: str) -> str:
        """Translate the provided `text`.
        
        Perform translation through an asynchorouns request.
        
        Args:
            text: The text to translate.
            
        Returns:
            The translated text.
        """
        result = asyncio.run(self._request_text_translation(text))
        return result.text

    async def _request_text_translation(self, text: str) -> models.Translated:
        """Send async request to translate `text`.
        
        Args:
            text: The text to translate.
            
        Returns:
            The response object.
        """
        async with Translator(service_urls=self.service_urls) as translator:
            return await translator.translate(text, src=self.src_lang, dest=self.target_lang)
