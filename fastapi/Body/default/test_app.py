from fastapi import Body, FastAPI
from fastapi.testclient import TestClient

app = FastAPI()
client = TestClient(app)


@app.get("/")
async def hello_world(msg: int = Body("hello world")):
    return {"msg": msg}


def test_case():
    response = client.get("/")
    assert response.json() == {"msg": "hello world"}
