from fpdf import FPDF


def test_case():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    pdf.cell(30, 10, txt="30x10", border=1)
    pdf.cell(15, 5, txt="15x5", border=1)
    pdf.cell(30, 15, txt="30x15", border=1)
    pdf.output("result.pdf")
