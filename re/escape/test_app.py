import re


def test_case():
    before = r"!#$%&'()*+,-./:;<=>?@[\]^_`{|}~/"
    after = r"!\#\$%\&'\(\)\*\+,\-\./:;<=>\?@\[\\\]\^_`\{\|\}\~/"
    assert re.escape(before) == after
