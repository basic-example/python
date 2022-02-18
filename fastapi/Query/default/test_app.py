from fastapi import FastAPI, Query
from fastapi.testclient import TestClient

app = FastAPI()
client = TestClient(app)


@app.get("/")
async def hello_world(page: int = Query(1)):
    return {"page": page}


def test_case():
    response = client.get("/")
    assert response.json() == {"page": 1}
