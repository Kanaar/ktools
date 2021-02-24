# tests/test_text_preprocessing.py
from ktools.text_preprocessing import remove_punctuation, lemmatize_text

def test_remove_punctuation():
    test_text = "Some, string with: punctuation..."
    result_text = "Some string with punctuation"
    assert remove_punctuation(test_text) == result_text

def test_lemmatize_text():
    test_text = "Some, string with: punctuation..."
    assert type(remove_punctuation(test_text)) == str



