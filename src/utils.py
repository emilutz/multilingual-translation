from enum import Enum

import click


class Language(Enum):
    ENGLISH = "en"
    SPANISH = "es"
    FRENCH = "fr"
    GERMAN = "de"
    CHINESE = "zh"


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
