from fpdf import FPDF


def test_case():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    pdf.cell(30, 10, txt="30x10", border=1)
    pdf.cell(30, 10, txt="30x10", border=0)
    pdf.cell(30, 10, txt="30x10", border="L")
    pdf.cell(30, 10, txt="30x10", border="T")
    pdf.cell(30, 10, txt="30x10", border="B")
    pdf.cell(30, 10, txt="30x10", border="R")
    pdf.output("result.pdf")
