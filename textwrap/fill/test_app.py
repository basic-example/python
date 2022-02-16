import textwrap


def test_case():
    assert (
        textwrap.fill("1234567 everyone abc defghijklmnopqrs", 13)
        == "1234567\neveryone abc \ndefghijklmnop\nqrs"
    )
