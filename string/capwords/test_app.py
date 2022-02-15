import string


def test_case():
    assert string.capwords("abc bcd cde", sep="b") == "AbC bCd cde"
    assert string.capwords("abc bcd cde", sep="c") == "Abc bcD cDe"
