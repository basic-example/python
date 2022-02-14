import pytest


def test_case():
    data = {1, 2, 3, 4}
    data.pop()

    assert data == {2, 3, 4} == {2, 4, 3}

    with pytest.raises(Exception) as exception:
        data.pop()
        data.pop()
        data.pop()
        data.pop()

    assert exception.type == KeyError
    assert "pop from an empty set" in str(exception.value)
