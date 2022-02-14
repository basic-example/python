import array


def test_case():

    assert array.array("b", []).itemsize == 1
    assert array.array("u", []).itemsize == 2
    assert array.array("h", []).itemsize == 2
    assert array.array("i", []).itemsize == 4
    assert array.array("f", []).itemsize == 4
    assert array.array("d", []).itemsize == 8
    assert array.array("q", []).itemsize == 8
