import os


def test_case():

    assert os.cpu_count() > 0
