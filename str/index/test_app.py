import pytest


def test_case():
    assert "python abcdef".index("python") == 0
    assert "python abcdef".index("python", 0, -1) == 0
    assert "abcdef python".index("python", 7) == 7
    assert "abcdef python".index("python", 7, 13) == 7

    with pytest.raises(Exception) as exception:
        "python abcdef".index("python", 1, -1)

    assert "substring not found" in str(exception.value)
