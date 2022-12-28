from barcode import EAN13
from barcode.writer import ImageWriter


def test_case():
    with open("image.png", "wb") as f:
        EAN13(str("8901072002478"), writer=ImageWriter()).write(
            f,
            {"format": "png"},
        )
    with open("image.jpg", "wb") as f:
        EAN13(str("8901072002478"), writer=ImageWriter()).write(
            f,
            {"format": "jpeg"},
        )
