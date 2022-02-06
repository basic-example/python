from fastapi import FastAPI
from fastapi.testclient import TestClient

from .routers import users

app = FastAPI()
app.include_router(
    users.router,
    prefix="/users",
)
client = TestClient(app)


def test_case():
    response = client.get("/users")

    assert response.json()["data"][0]["name"] == "yoo"
