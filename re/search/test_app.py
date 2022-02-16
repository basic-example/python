import re

# re.search : /pattern/
# re.match : /^pattern/
# re.fullmatch : /^pattern$/


def test_case():
    assert re.search("aaa", "aaa") != None
    assert re.search("aaa", "aaa bbb") != None
    assert re.search("aaa", "bbb aaa") != None
