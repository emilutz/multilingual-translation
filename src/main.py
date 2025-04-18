import logging
import logging.config
from pathlib import Path

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
@click.option(
    "--input-file", "-i",
    type=click.Path(file_okay=True, dir_okay=False, path_type=Path),
    help="Path to the input text file."
)
@click.option(
    "--output-file", "-o",
    type=click.Path(file_okay=True, dir_okay=False, writable=True, path_type=Path),
    help="Path to the output text file."
)
def main(translator_name, source_language, target_language, input_file, output_file):
    """Simple translation program.
    
    It reads text from `input_file` and writes the translation to `output_file`.
    """
    translator = create_translator(
        name=translator_name, source_language=source_language, target_language=target_language
    )

    with open(input_file, "r") as file_in, open(output_file, "w") as file_out:
        for line in file_in:
            line = line.strip("\n")
            translated_line = "" if line == "" else translator.translate(line)

            file_out.write(translated_line)
            file_out.write("\n")


if __name__ == "__main__":
    main()
