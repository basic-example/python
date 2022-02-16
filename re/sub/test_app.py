import re


def test_case():
    before = "010-1234-5678,010-2345-3456"
    after = "***-****-****,***-****-****"

    assert re.sub("[0-9]{3}-[0-9]{4}-[0-9]{4}", "***-****-****", before) == after
