import array


def test_case():

    arr = array.array("i", [1, 2, 3, 2, 2])
    arr.remove(2)

    assert arr == array.array("i", [1, 3, 2, 2])
