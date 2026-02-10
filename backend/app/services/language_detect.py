from langdetect import detect, LangDetectException


def detect_language(text: str) -> str:
    """Detect if text is Norwegian or English. Returns 'no' or 'en'."""
    try:
        lang = detect(text)
        # langdetect returns 'no' for Norwegian, 'en' for English
        if lang in ("no", "nb", "nn"):
            return "no"
        return "en"
    except LangDetectException:
        return "no"  # Default to Norwegian
