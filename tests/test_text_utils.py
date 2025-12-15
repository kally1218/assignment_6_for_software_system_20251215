from src.text_utils import to_uppercase, length

def test_to_uppercase():
    assert to_uppercase("hello") == "HELLO"

def test_length():
    assert length("abcd") == 4
