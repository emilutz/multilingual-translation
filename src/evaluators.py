import sacrebleu
from bert_score import score
from nltk.translate.bleu_score import sentence_bleu

from constants import Language


def bleu_score(ground_truth: str, prediction: str) -> float:
    """Evaluation function based on the Bleu score.

    Args:
        ground_truth: The label sentence [y].
        prediction: The predicted translation [y'].

    Returns:
        The metric score in the interval [0..1].
    """
    reference = [ground_truth.strip().split(" ")]
    candidate = prediction.strip().split(" ")

    return sentence_bleu(reference, candidate)


def chrf_score(ground_truth: str, prediction: str) -> float:
    """Evaluation function based on the Chrf score.

    Args:
        ground_truth: The label sentence [y].
        prediction: The predicted translation [y'].

    Returns:
        The metric score in the interval [0..100].
    """
    reference = [ground_truth.strip()]
    hypothesis = prediction.strip()

    return sacrebleu.corpus_chrf(hypothesis, reference).score


def bert_f1_score(ground_truth: str, prediction: str, lang: Language) -> float:
    """Evaluation function based on the f1-score of Bert's cosine similarity over embeddings.

    Args:
        ground_truth: The label sentence [y].
        prediction: The predicted translation [y'].

    Returns:
        The metric score in the interval [0..1].
    """
    references = [ground_truth.strip()]
    candidates = [prediction.strip()]

    _, _, f1 = score(candidates, references, lang=lang.value)
    return f1[0].numpy()
