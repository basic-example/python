def test_case():
    assert "python abcdef".find("python") == 0
    assert "python abcdef".find("abcdef", 7) == 7
    assert "python abcdef".find("abcdef", 7, -1) == -1
    assert "abcdef python".find("python") == 7
    assert "abcdef python".find("python", 8) == -1
    assert "abcdef python".find("python", 7, 13) == 7
    assert "abcdef python".find("PYTHON") == -1
