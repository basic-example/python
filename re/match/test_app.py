import re

# re.search : /pattern/
# re.match : /^pattern/
# re.fullmatch : /^pattern$/


def test_case():
    assert re.match("aaa", "aaa") != None
    assert re.match("aaa", "aaa bbb") != None
    assert re.match("aaa", "bbb aaa") == None
