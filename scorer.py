from __future__ import annotations

import re
from typing import Iterable

def _normalize(text: str) -> str:
    """Lowercase, strip, and remove non-alphanumeric characters except spaces."""
    if not text:
        return ""

    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", "", text)

    return " ".join(text.split())
    
def _contains_phrase(response: str, phrase: str) -> bool:
    """Check if the normalized text contains the normalized phrase."""
    response = _normalize(response)
    phrase = _normalize(phrase)

    if not phrase:
        return False

    if phrase in response:
        return True
    
    phrase_words = phrase.split()
    response_words = response.split()

    return all(word in response_words for word in phrase_words)

def judge(question: str, expects: str, answer: str, results) -> bool:
    """Judge if the answer contains the expected phrase after normalization."""
    if not expects or not answer:
        return False
    
    expected_phrases = [phrase.strip() for phrase in re.split(r"[,;]", expects) if phrase.strip()]
    if not expected_phrases:
        return False

    for phrase in expected_phrases:
        if _contains_phrase(answer, phrase):
            return True
    
    if results:
        retrieved_text = " ".join(getattr(result, "text", "") for result in results)
        for phrase in expected_phrases:
            if _contains_phrase(retrieved_text, phrase):
                return True

    return False