import re


def test_case():
    assert re.findall("[a-z]+", "1ab2cd3e") == ["ab", "cd", "e"]
    assert re.findall(r"(\w+)=(\d+)", "width=20 height=40") == [
        ("width", "20"),
        ("height", "40"),
    ]
