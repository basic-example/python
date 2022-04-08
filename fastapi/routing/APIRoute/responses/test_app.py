from fastapi import Body, FastAPI
from fastapi.testclient import TestClient

app = FastAPI()


@app.post(
    "/odd",
    responses={
        200: {
            "description": "Success",
            "content": {
                "application/json": {
                    "examples": {
                        "odd": {
                            "summary": "Odd Number",
                            "value": {"result": True},
                        },
                        "even": {
                            "summary": "Even Number",
                            "value": {"result": False},
                        },
                    }
                }
            },
        },
    },
)
def odd(data=Body(...)):
    return {"result": True if data["number"] % 2 else False}


def test_case():
    client = TestClient(app)
    response = client.get("/openapi.json").json()
    assert (
        "Odd Number"
        == response["paths"]["/odd"]["post"]["responses"]["200"]["content"][
            "application/json"
        ]["examples"]["odd"]["summary"]
    )

    assert (
        "Even Number"
        in response["paths"]["/odd"]["post"]["responses"]["200"]["content"][
            "application/json"
        ]["examples"]["even"]["summary"]
    )
