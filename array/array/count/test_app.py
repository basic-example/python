import array


def test_case():

    assert array.array("i", [1, 2, 3, 2, 3, 2, 2, 2]).count(2) == 5
