from argparse import ArgumentParser

import pytest


def test_case():

    with pytest.raises(Exception) as info:
        parser = ArgumentParser()
        parser.add_argument("-f", "--foo", help="old foo help")
        parser.add_argument("--foo", help="new foo help")

    assert "argument --foo: conflicting option string: --foo" in str(info.value)

    parser = ArgumentParser(conflict_handler="resolve")
    parser.add_argument("-f", "--foo", help="old foo help")
    parser.add_argument("--foo", help="new foo help")
