import base64
from io import BytesIO

from PIL import Image


def test_case():
    data = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAA1JREFUGFdjYGBg+A8AAQQBAHAgZQsAAAAASUVORK5CYII="  # png
    im = Image.open(BytesIO(base64.b64decode(data)))
    im = im.resize((200, 100))

    assert (200, 100) == im.size

    im = im.transpose(method=Image.Transpose.ROTATE_90)

    assert (100, 200) == im.size
