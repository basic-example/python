import array


def test_case():

    arr = array.array("i", [1, 2, 3])
    arr.pop(1)

    assert arr == array.array("i", [1, 3])
