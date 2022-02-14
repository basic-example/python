def test_case():
    assert "hello world~! hi~! everyone~!".count("~!") == 3
    assert "hello world~! hi~! everyone~!".count("~!", 0, 20) == 2
    assert "hello world~! hi~! everyone~!".count("~!", 13) == 2
