import base64
from io import BytesIO

from PIL import Image


def test_case():
    data = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAA1JREFUGFdjYGBg+A8AAQQBAHAgZQsAAAAASUVORK5CYII="  # png
    im = Image.open(BytesIO(base64.b64decode(data)))
    width, height = im.size

    assert width == 1
    assert height == 1
