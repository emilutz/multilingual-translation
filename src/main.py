import logging
import logging.config

import click

from constants import Language
from utils import LanguageParamType, create_translator


logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)


@click.command()
@click.option("--text", prompt="Input text", help="Input text to translate.")
@click.option("--translator_name", "--tn", help="The translator type to use.")
@click.option(
    "--source_language", "--src",
    type=LanguageParamType(),
    default=Language.ENGLISH,
    help="The language of the input text."
)
@click.option(
    "--target_language", "--target",
    type=LanguageParamType(),
    help="The language of the output text."
)
def main(text, translator_name, source_language, target_language):
    """Simple translation program.
    
    It translates `text` from `source_language` to `target_language` using `trans_name`.
    """
    translator = create_translator(
        name=translator_name, source_language=source_language, target_language=target_language
    )

    translated_text = translator.translate(text)
    logger.info(translated_text)


if __name__ == "__main__":
    main()
