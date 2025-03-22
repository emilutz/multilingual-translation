from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

from translators.base_translator import BaseTranslator
from constants import Language


class HuggingFaceTranslator(BaseTranslator):
    """Text translator based on a Hugging Face LLM."""

    def __init__(
            self,
            source_language: Language,
            target_language: Language,
            model_name: str = "facebook/m2m100_418M",
        ):
        """Initialize the translator.
        
        Args:
            source_language: The language to translate from.
            target_language: The language to translate into.
        """
        super().__init__(source_language, target_language)

        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.tokenizer.src_lang = self.src_lang

        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

    def translate(self, text: str) -> str:
        """Translate the provided `text`.
        
        Perform translation through token encoding, conversion and decoding.
        
        Args:
            text: The text to translate.
            
        Returns:
            The translated text.
        """
        # create tokens from the input string
        encoded = self.tokenizer(text, return_tensors="pt")

        # convert the tokens from the source language to the target language
        token_id = self.tokenizer.get_lang_id(self.target_lang)
        generated_tokens = self.model.generate(**encoded, forced_bos_token_id=token_id)

        # decode the converted tokens back to a string format
        decoded = self.tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        return decoded[0]
