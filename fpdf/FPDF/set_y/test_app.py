from fpdf import FPDF


def test_case():

    pdf = FPDF()
    pdf.set_font("Helvetica")
    pdf.add_page()
    pdf.set_y(50)
    pdf.cell(30, 10, txt="30x10", border=1)
    pdf.set_y(75)
    pdf.cell(40, 20, txt="40x20", border=1)
    pdf.set_y(9900)
    pdf.cell(50, 30, txt="50x30", border=1)
    pdf.set_y(10)
    assert pdf.cell(60, 40, txt="60x40", border=1) == False
    pdf.set_y(15)
    assert pdf.cell(70, 50, txt="70x50", border=1) == False
    pdf.set_y(99900)
    assert pdf.cell(60, 40, txt="60x40", border=1) == True  # new page
    pdf.set_y(999900)
    assert pdf.cell(50, 30, txt="50x30", border=1) == True  # new page
    pdf.output("result.pdf")
