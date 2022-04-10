import base64
from io import BytesIO

from PIL import Image


def test_case():
    data = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAA1JREFUGFdjYGBg+A8AAQQBAHAgZQsAAAAASUVORK5CYII="  # png
    im = Image.open(BytesIO(base64.b64decode(data)))
    im = im.resize((200, 100))

    assert (200, 100) == im.size

    im = im.rotate(90)

    assert (200, 100) == im.size

    im = im.rotate(90, expand=True)

    assert (100, 200) == im.size
