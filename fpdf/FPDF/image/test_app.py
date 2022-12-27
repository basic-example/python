from io import BytesIO

from fpdf import FPDF
from PIL import Image, ImageDraw


def test_case():

    image = Image.new("RGB", (300, 50))
    draw = ImageDraw.Draw(image)
    draw.text((0, 0), "300X50")

    byte_io = BytesIO()
    image.save(byte_io, "PNG")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica")

    pdf.image(byte_io, x=75, y=100, w=25, h=25)
    pdf.output("result.pdf")
