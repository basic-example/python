from fpdf import FPDF


def test_case():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica")
    pdf.cell(30, 10, txt="30x10", border=1)
    pdf.ln(10)
    pdf.cell(30, 10, txt="30x10", border=1)
    pdf.cell(30, 10, txt="30x10", border=1)
    pdf.ln(15)
    pdf.cell(30, 10, txt="30x10", border=1)
    pdf.cell(30, 10, txt="30x10", border=1)
    pdf.ln(20)
    pdf.cell(30, 10, txt="30x10", border=1)
    pdf.cell(30, 10, txt="30x10", border=1)
    pdf.output("result.pdf")
