from fpdf import FPDF


def test_case():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size=12)
    pdf.set_display_mode("fullwidth", "two")
    pdf.cell(30, 10, txt="30x10")
    pdf.output("result.pdf")
