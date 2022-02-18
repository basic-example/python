from fastapi import FastAPI, Path
from fastapi.testclient import TestClient

app = FastAPI()
client = TestClient(app)


@app.get("/{msg}")
async def hello_world(msg: str = Path(...)):
    return msg


@app.get("/{msg}/{num}")
async def hello_world(msg: str = Path(...), num: int = Path(...)):
    return {"message": msg, "number": num}


def test_case():
    response = client.get("/hello-world")
    assert response.json() == "hello-world"

    response = client.get("/hello-world/1234")
    assert response.json() == {"message": "hello-world", "number": 1234}
