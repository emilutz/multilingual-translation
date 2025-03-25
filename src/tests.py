import os
import logging
import logging.config
from pathlib import Path

import pandas as pd
import pytest

from constants import Language
from evaluators import bert_f1_score, bleu_score, chrf_score
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

    df["bleu_score"] = df.apply(
        lambda row: bleu_score(row["translated_value"], row["predicted_value"]), axis=1
    )
    df["chrf_score"] = df.apply(
        lambda row: chrf_score(row["translated_value"], row["predicted_value"]), axis=1
    )
    df["bert_f1_score"] = df.apply(
        lambda row: bert_f1_score(
            row["translated_value"], row["predicted_value"], lang=Language.HUNGARIAN
        ), axis=1
    )

    logger.info(f"Performance for {Translator.__name__}:")
    logger.info(f"\tbleu score:    {df['bleu_score'].mean():.03f}")
    logger.info(f"\tchrf score:    {df['chrf_score'].mean():.03f}")
    logger.info(f"\tbert f1-score: {df['bert_f1_score'].mean():.03f}")

    eval_results_dir = os.environ.get("EVAL_RESULTS_DIR", None)

    if eval_results_dir is not None:
        eval_results_dir = Path(eval_results_dir)
        eval_results_dir.mkdir(parents=True, exist_ok=True)
        df.to_csv(eval_results_dir / f"eval_{Translator.__name__}.csv")
