from fpdf import FPDF


def test_case():
    pdf = FPDF()
    pdf.set_font("Helvetica")
    pdf.add_page()
    pdf.set_x(50)
    pdf.cell(30, 10, txt="30x10", border=1)
    pdf.set_x(75)
    pdf.cell(40, 20, txt="40x20", border=1)
    pdf.set_x(0)
    pdf.cell(50, 30, txt="50x30", border=1)
    pdf.set_x(-61)
    pdf.cell(60, 40, txt="60x40", border=1)
    pdf.output("result.pdf")
