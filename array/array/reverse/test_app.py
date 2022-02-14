import array


def test_case():

    arr = array.array("i", [1, 2, 3])
    arr.reverse()

    assert arr == array.array("i", [3, 2, 1])
