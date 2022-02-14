import pytest


def test_case():
    data = {1, 2, 3, 4}
    data.remove(3)

    assert data == {1, 2, 4} == {2, 1, 4}

    with pytest.raises(Exception) as exception:
        data.remove(5)

    assert exception.type == KeyError
    assert "5" in str(exception.value)
