import textwrap


def test_case():
    assert textwrap.wrap("1234567 everyone abc defghijklmnopqrs", 13) == [
        "1234567",
        "everyone abc ",
        "defghijklmnop",
        "qrs",
    ]
