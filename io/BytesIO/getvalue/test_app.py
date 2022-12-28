import io


def test_case():
    assert io.BytesIO().getvalue() == b""
    assert io.BytesIO(b"hello world").getvalue() == b"hello world"
