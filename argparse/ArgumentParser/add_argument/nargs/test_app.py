import re
from argparse import ArgumentParser


class FakeFile:
    message = None

    def write(self, msg):
        self.message = msg


file = FakeFile()


def test_case():

    parser = ArgumentParser(prog="tester")
    parser.add_argument("--three", nargs=3)
    parser.add_argument("--optional", nargs="?")
    parser.add_argument("--all", nargs="*")
    parser.add_argument("--one-or-more", nargs="+")
    parser.print_help(file)

    assert re.search(r"three THREE THREE THREE", file.message)
    assert re.search(r"--optional \[OPTIONAL\]", file.message)
    assert re.search(r"--all \[ALL ...\]", file.message)
    assert re.search(r"--one-or-more ONE_OR_MORE \[ONE_OR_MORE ...\]", file.message)
