from fastapi import Body, FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.post("/odd")
def odd(
    data=Body(
        ...,
        examples={
            "odd": {"summary": "odd number", "value": {"number": 111}},
            "even": {"summary": "even number", "value": {"number": 222}},
            "alphabet": {
                "summary": "alphabet string",
                "description": """Using invalid, non-number input.<br />
                    Will raise `Error: Unprocessable Entity` message.""",
                "value": {"number": "abc"},
            },
        },
    )
):
    return {"result": True if data["number"] % 2 else False}


def test_case():
    client = TestClient(app)
    response = client.get("/openapi.json").json()
    assert (
        111
        == response["paths"]["/odd"]["post"]["requestBody"]["content"][
            "application/json"
        ]["examples"]["odd"]["value"]["number"]
    )

    assert (
        222
        == response["paths"]["/odd"]["post"]["requestBody"]["content"][
            "application/json"
        ]["examples"]["even"]["value"]["number"]
    )
