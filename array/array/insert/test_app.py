import array


def test_case():

    arr = array.array("i", [1, 2, 3])
    arr.insert(1, 3)

    assert arr == array.array("i", [1, 3, 2, 3])
