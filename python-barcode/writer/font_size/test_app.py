from barcode import EAN13


def test_case():
    with open("image1.svg", "wb") as f:
        # remove barcode number
        EAN13(str(8901072002478)).write(f, {"font_size": 0})

    with open("image2.svg", "wb") as f:
        EAN13(str(8901072002478)).write(f, {"font_size": 15})
