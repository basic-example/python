import re
from argparse import ArgumentParser


class FakeFile:
    message = None

    def write(self, msg):
        self.message = msg


file = FakeFile()


def test_case():
    parser = ArgumentParser(prog="tester")
    parser.print_help(file)
    assert re.match("^usage: tester", file.message)
