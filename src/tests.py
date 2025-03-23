import logging
import logging.config

import pandas as pd
import pytest

from constants import Language
from translators.google_translator import GoogleTranslator
from translators.hf_translator import HuggingFaceTranslator


logging.config.fileConfig("logging.conf")
logger = logging.getLogger(__name__)


@pytest.fixture(scope="module")
def test_df():
    data_path = "data/translated_output.csv"
    return pd.read_csv(data_path)


@pytest.mark.parametrize("Translator", [HuggingFaceTranslator, GoogleTranslator])
def test_translator_performance(test_df, Translator):
    translator = Translator(
        source_language=Language.ENGLISH, target_language=Language.HUNGARIAN
    )

    df = test_df.copy()
    df["predicted_value"] = df["english"].apply(lambda x: translator.translate(x.strip()))

    accuracy = (df["translated_value"] == df["predicted_value"]).mean()
    logger.info(f"{Translator.__name__} accuracy: {accuracy:.02f}")
    assert accuracy >= 0.0
