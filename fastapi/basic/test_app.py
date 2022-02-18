from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()
client = TestClient(app)


@app.get("/")
async def hello_world():
    return "hello world"


def test_case():
    response = client.get("/")
    assert response.json() == "hello world"
