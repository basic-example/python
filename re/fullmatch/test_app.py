import re

# re.search : /pattern/
# re.match : /^pattern/
# re.fullmatch : /^pattern$/


def test_case():
    assert re.fullmatch("aaa", "aaa") != None
    assert re.fullmatch("aaa", "aaa bbb") == None
    assert re.fullmatch("aaa", "bbb aaa") == None
