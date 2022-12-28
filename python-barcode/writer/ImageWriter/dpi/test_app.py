from barcode import EAN13
from barcode.writer import ImageWriter


def test_case():
    with open("image1.png", "wb") as f:
        EAN13(str("8901072002478"), writer=ImageWriter()).write(f, {"dpi": 300})
    with open("image2.png", "wb") as f:
        EAN13(str("8901072002478"), writer=ImageWriter()).write(f, {"dpi": 600})
