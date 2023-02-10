from io import BytesIO
from pypdf import PdfWriter


def test_case_BytesIO():
    merger = PdfWriter()
    output = open("output_BytesIO.pdf", "wb")
    with open("sample.pdf", "rb") as f:
        buffer = BytesIO(f.read())
        merger.append(fileobj=buffer)
    merger.write(output)
    output.close()

def test_case_path():
    merger = PdfWriter()
    output = open("output_path.pdf", "wb")
    merger.append(fileobj='sample.pdf')
    merger.write(output)
    output.close()
