from abc import ABC, abstractmethod

from utils import Language


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
