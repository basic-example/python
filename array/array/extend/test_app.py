import array


def test_case():

    arr = array.array("i", [1, 2, 3])
    arr.extend([3, 4, 5])

    assert arr == array.array("i", [1, 2, 3, 3, 4, 5])
