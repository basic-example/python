def test_case():
    data = {1, 2, 3, 4}
    data.discard(3)

    assert data == {1, 2, 4} == {2, 1, 4}

    data.discard(5)

    assert data == {1, 2, 4} == {2, 1, 4}
