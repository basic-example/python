from functools import partial


def add(a, b):
    return a + b


add_with_3 = partial(add, 3)
add_with_4 = partial(add, 4)


def test_case():
    assert add_with_3(2) == 5
    assert add_with_3(3) == 6
    assert add_with_4(3) == 7
