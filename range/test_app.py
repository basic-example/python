def test_case():
    arr = range(11)

    assert list(arr) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert isinstance(arr, range)
