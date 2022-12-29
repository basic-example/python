from fpdf import FPDF, line_break


def get_text_lines(self, fit_width, txt: str = "", print_sh: bool = False):
    normalized_string = self.normalize_text(txt).replace("\r", "")
    styled_text_fragments = self._preload_font_styles(normalized_string, False)
    text_lines = []
    multi_line_break = line_break.MultiLineBreak(
        styled_text_fragments,
        print_sh=print_sh,
    )

    while not text_lines or (text_line) is not None:
        text_line = multi_line_break.get_line_of_given_width(fit_width)
        if text_line:
            text_lines.append(text_line)

    return text_lines


def test_case():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica")
    txt = "11111 22222 33333 44444 55555 66666 77777 88888 99999 aaaaa bbbbb ccccc ddddd eeeee fffff ggggg hhhhh iiiii jjjjj kkkkk lllll mmmmm nnnnn ooooo ppppp qqqqq rrrrr sssss ttttt uuuuu vvvvv wwwww xxxxx yyyyy zzzzz"

    text_lines_width_200 = get_text_lines(pdf, 200, txt=txt)
    text_lines_width_300 = get_text_lines(pdf, 300, txt=txt)

    assert len(text_lines_width_300) < len(text_lines_width_200)
    assert len(text_lines_width_300) == 2
    assert (
        "".join(text_lines_width_300[0].fragments[0].characters)
        + " "
        + "".join(text_lines_width_300[1].fragments[0].characters)
        == txt
    )
