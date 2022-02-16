import re


def test_case():
    assert re.split("[a-z]+", "1ab2cd3e") == ["1", "2", "3", ""]
    assert re.split(r"\\", "a\\b\\c") == ["a", "b", "c"]
