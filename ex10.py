import pytest


def test_short_phrase():
    phrase = input("Please enter a phrase shorter than 15 characters: ")
    assert len(phrase) < 15, "Phrase contains 15 or more characters"


test_short_phrase()
