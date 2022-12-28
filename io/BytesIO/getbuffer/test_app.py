import io


def test_case():
    bytes = io.BytesIO(b"hello world")
    buffer = bytes.getbuffer()
    buffer[2:5] = b"LLO"

    assert bytes.getvalue() == b"heLLO world"
