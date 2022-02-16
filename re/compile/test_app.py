import re


def test_case():
    assert re.compile(r"world").search("hello world") != None
    assert re.compile(r"world$").search("hello world") != None
    assert re.compile(r"^world").search("hello world") == None
