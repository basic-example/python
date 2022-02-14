def test_case():
    data = {1, 2, 3, 4}
    data.intersection_update({3, 4, 5})

    assert data == {3, 4}
