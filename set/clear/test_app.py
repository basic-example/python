def test_case():
    data = {1, 2, 3, 4}
    data.clear()
    data.clear()

    assert data == set()
