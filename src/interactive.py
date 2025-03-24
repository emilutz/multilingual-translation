import logging
import logging.config

import click

from constants import Language
from utils import LanguageParamType, create_translator


logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)


@click.command()
@click.option(
    "--translator-name", "--tn",
    default="hf",
    help="The translator type to use."
)
@click.option(
    "--source-language", "--source",
    type=LanguageParamType(),
    default=Language.ENGLISH,
    help="The language of the input text."
)
@click.option(
    "--target-language", "--target",
    type=LanguageParamType(),
    help="The language of the output text."
)
def main(translator_name, source_language, target_language):
    """Simple translation program.
    
    It translates input text interactively from `source_language` to `target_language`
    using `translator_name`.
    """
    translator = create_translator(
        name=translator_name, source_language=source_language, target_language=target_language
    )

    logger.info("Input a sentence to be translated or 'quit'/'exit' to stop the program.")

    while True:
        input_text = input(f"({source_language.value})> ")

        if input_text.lower() in ["quit", "exit"]:
            logger.info("Stopping execution.")
            break

        translated_text = translator.translate(input_text)
        logger.info(f"({target_language.value}): {translated_text}\n")


if __name__ == "__main__":
    main()
