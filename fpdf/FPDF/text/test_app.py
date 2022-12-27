from fpdf import FPDF


def test_case():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica")
    pdf.text(
        x=10,
        y=10,
        txt="hello world 1. hello world 2. hello world 3. hello world 4. hello world 5. hello world 6. hello world 7. hello world 8. hello world 9.",
    )
    pdf.text(
        x=50,
        y=50,
        txt="hello world 1. hello world 2. hello world 3. hello world 4. hello world 5. hello world 6. hello world 7. hello world 8. hello world 9.",
    )
    pdf.write(
        h=100,
        txt="hello world 1. hello world 2. hello world 3. hello world 4. hello world 5. hello world 6. hello world 7. hello world 8. hello world 9.",
    )

    pdf.output("result.pdf")
