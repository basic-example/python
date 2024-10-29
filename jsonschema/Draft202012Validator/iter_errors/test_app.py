import jsonschema.exceptions

import jsonschema


def test_case():

    schema = {
        "$schema": jsonschema.Draft202012Validator.META_SCHEMA["$id"],
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "email": {"type": "string"},
        },
        "required": ["email"],
    }
    errors = jsonschema.Draft202012Validator(schema).iter_errors(
        {"name": ["chulsu", "park"]}
    )
    dict_errors = dict()

    for error in errors:
        if error.validator == "required":
            dict_errors[error.message.split(" ")[0].strip("'")] = error
        else:
            dict_errors[error.path[-1]] = error

    for error in errors:
        assert isinstance(error, jsonschema.exceptions.ValidationError) == True

    assert str(dict_errors["name"].path) == "deque(['name'])"
    assert str(dict_errors["email"].path) == "deque([])"
    assert dict_errors["name"].message == "['chulsu', 'park'] is not of type 'string'"
    assert dict_errors["email"].message == "'email' is a required property"
