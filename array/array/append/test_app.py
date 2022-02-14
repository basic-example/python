import array


def test_case():

    arr = array.array("i", [1, 2, 3])
    arr.append(4)

    assert arr[3] == 4
