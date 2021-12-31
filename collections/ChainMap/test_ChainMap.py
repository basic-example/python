from collections import ChainMap
import pytest


def test_case():
    first = "aaa"
    second = ["bbb"]
    chain_map = ChainMap(first, second)

    assert str(chain_map) == "ChainMap('aaa', ['bbb'])"

    chain_map.new_child({"port": 1234})
    assert str(chain_map) != "ChainMap({'port': 1234}, 'aaa', ['bbb'])"

    chain_map = chain_map.new_child({"port": 1234})
    assert str(chain_map) == "ChainMap({'port': 1234}, 'aaa', ['bbb'])"

    chain_map["port"] = 8000

    assert str(chain_map) == "ChainMap({'port': 8000}, 'aaa', ['bbb'])"
    assert str(chain_map.maps) == "[{'port': 8000}, 'aaa', ['bbb']]"
    assert str(chain_map.parents) == "ChainMap('aaa', ['bbb'])"
