import re
from abc import ABC, abstractmethod
from copy import copy

from constants import Language


class BaseTranslator(ABC):
    """Abstract base class for text translators.

    Attributes:
        src_lang: The language to translate from.
        target_lang: The language to translate into.
    """

    def __init__(self, source_language: Language, target_language: Language):
        """Initialize for the translator.
        
        Args:
            source_language: The language to translate from.
            target_language: The language to translate into.
        """
        self.src_lang: str = source_language.value
        self.target_lang: str = target_language.value

    @abstractmethod
    def translate(self, text: str) -> str:
        """Translate the provided `text`.

        This method must be implemented by all subclasses.

        Args:
            text: The text to translate.
            
        Returns:
            The translated text.
        """
        pass


class PlaceholderPreserver:
    """Context manager for preventing bracketed words from translation.

    Attributes:
        text: The original text to translate.
        brackets: The list of words to preserve.
    """

    def __init__(self, text: str):
        """Initialize the placeholder preserver.

        Args:
            text: The original text to translate.
        """
        pattern = r"\[([^\]]+)\]"
        self.text = copy(text)
        self.brackets = re.findall(pattern, self.text)

    def __enter__(self):
        """Replace all placeholders with a numbered string constant."""
        for i, word in enumerate(self.brackets):
            placeholder = f"_phldr_{i}_"
            self.text = self.text.replace(f'[{word}]', placeholder)

        return self.text

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Do nothing special."""
        pass

    def fill_back_placeholders(self, ph_text: str) -> str:
        """Retrieve the original placeholders back after translation.

        Args:
            ph_text: The translated text, but with `PLACEHOLDER_{i}` constants.

        Returns:
            The translated text where the original placeholders in-place.
        """
        text = copy(ph_text)

        for i, word in enumerate(self.brackets):
            placeholder = f"_phldr_{i}_"
            text = text.replace(placeholder, f"[{word}]")

        return text
