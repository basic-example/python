from enum import Enum


class Status(Enum):
    READY = "ready"
    DONE = "done"


def test_case():

    assert str(Status._value2member_map_.keys().__class__) == "<class 'dict_keys'>"
    assert list(Status._value2member_map_.keys()) == ["ready", "done"]
