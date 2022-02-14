def test_case():
    data = {1, 2, 3, 4}
    data.symmetric_difference_update({3, 4, 5})

    assert data == {1, 2, 5}
