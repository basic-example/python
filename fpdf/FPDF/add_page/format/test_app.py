from fpdf import FPDF


def test_case():
    pdf = FPDF()
    pdf.set_font("Helvetica", size=12)
    pdf.add_page(format=(300, 100))
    pdf.add_page(format=(150, 150))
    pdf.add_page(format=(100, 300))
    pdf.output("result.pdf")
