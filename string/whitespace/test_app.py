import string


def test_case():
    # \t : Horizontal Tab
    # \n : Line Feed
    # \r : Carriage Return
    # \v or \x0b : Line Tabulation
    # \f or \x0c : Form Feed
    assert string.whitespace == " \t\n\r\x0b\x0c"
