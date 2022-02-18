from fastapi import FastAPI, Query
from fastapi.testclient import TestClient

app = FastAPI()
client = TestClient(app)


@app.get("/")
async def hello_world(q: str = Query(None, max_length=5)):
    return {"result": q}


def test_case():
    response = client.get("/?q=" + "a" * 5)
    assert response.json() == {"result": "aaaaa"}

    response = client.get("/?q=" + "a" * 6)
    assert response.json() == {
        "detail": [
            {
                "ctx": {"limit_value": 5},
                "loc": ["query", "q"],
                "msg": "ensure this value has at most 5 characters",
                "type": "value_error.any_str.max_length",
            }
        ]
    }
