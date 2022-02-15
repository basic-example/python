def test_case():
    assert "1234".isdecimal() == True
    assert "1.0".isdecimal() == False
    assert "abcd".isdecimal() == False
    assert "안녕".isdecimal() == False
    assert " ".isdecimal() == False
