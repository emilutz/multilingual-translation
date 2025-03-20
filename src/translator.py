from enum import Enum

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer


class Language(Enum):
    ENGLISH = "en"
    SPANISH = "es"
    FRENCH = "fr"
    GERMAN = "de"
    CHINESE = "zh"


def translate_test(text: str, source_language: Language, target_language: Language) -> str:
    source_lang = source_language.value
    target_lang = target_language.value

    model_name = "facebook/m2m100_418M"  # Smaller model that supports 100+ languages
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    tokenizer.src_lang = source_lang
    encoded = tokenizer(text, return_tensors="pt")
    generated_tokens = model.generate(
        **encoded,
        forced_bos_token_id=tokenizer.get_lang_id(target_lang)
    )
    return tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
