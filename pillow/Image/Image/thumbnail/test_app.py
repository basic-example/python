import base64
from io import BytesIO

from PIL import Image


def test_case():
    data = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAA1JREFUGFdjYGBg+A8AAQQBAHAgZQsAAAAASUVORK5CYII="  # png
    im = Image.open(BytesIO(base64.b64decode(data)))
    im.thumbnail((10, 10))

    assert (1, 1) == im.size

    im = im.resize((100, 100))
    im.thumbnail((10, 20))

    assert (10, 10) == im.size

    im = im.resize((100, 100))
    im.thumbnail((30, 20))

    assert (20, 20) == im.size

    im = im.resize((200, 100))
    im.thumbnail((10, 20))

    assert (10, 5) == im.size
