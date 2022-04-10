import base64
from io import BytesIO

from PIL import Image


def test_case():
    buffer = BytesIO()
    data = "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAAAXNSR0IArs4c6QAAAA1JREFUGFdjYGBg+A8AAQQBAHAgZQsAAAAASUVORK5CYII="  # png
    im = Image.open(BytesIO(base64.b64decode(data)))
    im = im.resize((50, 50))
    im.save(buffer, "png")

    assert (
        base64.b64encode(buffer.getvalue())
        == b"iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAVklEQVR4nO3PgQkAIRDAsPP331mXED5IM0G7ZmbPA76/A25pRNOIphFNI5pGNI1oGtE0omlE04imEU0jmkY0jWga0TSiaUTTiKYRTSOaRjSNaBrRNKI565oBYxivQ0IAAAAASUVORK5CYII="
    )
