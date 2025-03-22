import click

from constants import Language
from translators.base_translator import BaseTranslator
from translators.google_translator import GoogleTranslator
from translators.hf_translator import HuggingFaceTranslator


class LanguageParamType(click.ParamType):
    """Custom Click parameter type for Language enum."""
    name = "language"
    
    def convert(self, value, param, ctx):
        """Convert string input to Language enum value."""
        if isinstance(value, Language):
            return value
            
        try:
            # Try to find by value (en, es, fr, etc.)
            for lang in Language:
                if lang.value == value:
                    return lang
                    
            # Also try to find by name (ENGLISH, SPANISH, etc.)
            return Language[value.upper()]
        except (KeyError, ValueError):
            valid_values = [f"{lang.name}({lang.value})" for lang in Language]
            self.fail(
                f"'{value}' is not a valid language. Choose from: {', '.join(valid_values)}",
                param, ctx
            )


def create_translator(name: str, **kwargs) -> BaseTranslator:
    match name:
        case "hf":
            return HuggingFaceTranslator(**kwargs)
        case "google":
            return GoogleTranslator(**kwargs)
        case _:
            raise NotImplementedError(f"Translator '{name}' is not implemented")
