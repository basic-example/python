from fpdf import FPDF


def test_case():
    pdf = FPDF()
    pdf.set_font("Helvetica", size=12)

    pdf.set_margin(30)
    pdf.add_page()
    pdf.write(
        h=30,
        txt="hello world. hello world. hello world. hello world. hello world. hello world. hello world. hello world. hello world. ",
    )

    pdf.set_margin(60)
    pdf.add_page()
    pdf.write(
        h=30,
        txt="hello world. hello world. hello world. hello world. hello world. hello world. hello world. hello world. hello world. ",
    )

    pdf.set_margin(90)
    pdf.add_page()
    pdf.write(
        h=30,
        txt="hello world. hello world. hello world. hello world. hello world. hello world. hello world. hello world. hello world. ",
    )

    pdf.set_margin(90)
    pdf.add_page()
    pdf.cell(30, 10, txt="30x10", border=1)
    pdf.cell(30, 10, txt="30x10", border=1)
    pdf.cell(30, 10, txt="30x10", border=1)
    pdf.cell(30, 10, txt="30x10", border=1)
    pdf.cell(30, 10, txt="30x10", border=1)

    pdf.output("result.pdf")
