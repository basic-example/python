import string


def test_case():
    # string.punctuation = !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    assert string.punctuation == "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
