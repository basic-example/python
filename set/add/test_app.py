def test_case():
    data = {
        1,
    }
    data.add(2)
    data.add(3)
    data.add(4)

    assert data == {1, 2, 3, 4} == {2, 1, 3, 4}
