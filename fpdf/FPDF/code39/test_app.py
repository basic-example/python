from fpdf import FPDF


def test_case():

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica")
    pdf.code39("*ABCD*", x=0, y=0, w=1, h=5)
    pdf.output("result.pdf")
