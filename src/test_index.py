import pytest
from index import is_meow

def test_valid_cat_sounds():
    assert is_meow("meow") is True
    assert is_meow("MEOW") is True
    assert is_meow("nyaa") is True
    assert is_meow("miau") is True

def test_invalid_cat_sounds():
    assert is_meow("woof") is False
    assert is_meow("bark") is False
    assert is_meow("hello") is False

def test_empty_or_invalid_inputs():
    assert is_meow("") is False
    assert is_meow(" ") is False
    assert is_meow(None) is False 