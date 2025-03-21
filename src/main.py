import logging
import logging.config

import click

from utils import Language, LanguageParamType
from translators.hf_translator import HuggingFaceTranslator


logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)


@click.command()
@click.option("--text", prompt="Input text", help="Input text to translate.")
@click.option("--translator_name", help="The translator type to use.")
@click.option(
    "--source_language",
    type=LanguageParamType(),
    default=Language.ENGLISH,
    help="The language of the input text."
)
@click.option(
    "--target_language",
    type=LanguageParamType(),
    help="The language of the output text."
)
def main(text, translator_name, source_language, target_language):
    """Simple translation program.
    
    It translates `text` from `source_language` to `target_language` using `trans_name`.
    """
    logger.info(text)


if __name__ == "__main__":
    main()
