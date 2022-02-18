from fastapi import FastAPI, Query
from fastapi.testclient import TestClient

app = FastAPI()
client = TestClient(app)


@app.get("/")
async def hello_world(aaa: int = Query(1, gt=10)):
    return {"result": aaa}


def test_case():
    response = client.get("/?aaa=11")
    assert response.json() == {"result": 11}

    response = client.get("/?aaa=10")
    assert response.json() == {
        "detail": [
            {
                "ctx": {"limit_value": 10},
                "loc": ["query", "aaa"],
                "msg": "ensure this value is greater than 10",
                "type": "value_error.number.not_gt",
            }
        ]
    }
