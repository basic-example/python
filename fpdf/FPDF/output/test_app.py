from fpdf import FPDF


def test_case():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    pdf.cell(30, 10, txt="30x10", border=1)
    pdf.output("result.pdf")  # save to file
    result = pdf.output()  # save to memory
    assert type(result) == bytearray
