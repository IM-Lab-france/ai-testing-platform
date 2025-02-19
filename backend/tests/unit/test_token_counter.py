from src.utils.token_counter import count_tokens

def test_count_tokens_short_text():
    text = "Hello, world!"
    assert count_tokens(text) > 0

def test_count_tokens_long_text():
    text = "This is a longer text that should be tokenized into multiple tokens."
    assert count_tokens(text) > 5

def test_count_tokens_empty_text():
    text = ""
    assert count_tokens(text) == 0

def test_count_tokens_special_characters():
    text = "!@#$%^&*()"
    assert count_tokens(text) > 0