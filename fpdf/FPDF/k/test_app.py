from fpdf import FPDF


def test_case():

    pdf = FPDF()

    assert pdf.k == 2.834645669291339  # mm to pt coefficient
