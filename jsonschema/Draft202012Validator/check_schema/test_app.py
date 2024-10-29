import pytest

from jsonschema import Draft202012Validator


def test_case():

    valid_schema = {
        "$schema": Draft202012Validator.META_SCHEMA["$id"],
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "email": {"type": "string"},
        },
        "required": ["email"],
    }
    invalid_schema = {
        "$schema": Draft202012Validator.META_SCHEMA["$id"],
        "type": "unknown",
        "properties": {
            "name": {"type": "string"},
            "email": {"type": "string"},
        },
        "required": ["email"],
    }

    with pytest.raises(Exception) as exception:
        Draft202012Validator.check_schema(invalid_schema)

    assert "'unknown' is not valid under any of the given schemas" in str(
        exception.value
    )
    assert Draft202012Validator.check_schema(valid_schema) == None
