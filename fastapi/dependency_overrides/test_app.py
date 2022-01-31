from fastapi import Depends, FastAPI
from fastapi.testclient import TestClient

app = FastAPI()
client = TestClient(app)


class Auth:
    def user(self):
        return None


class FakeAuth:
    def user(self):
        return {"name": "yoo"}


app.dependency_overrides[Auth] = FakeAuth


@app.get("/auth-user")
async def read_users(auth=Depends(Auth)):
    return {"user": auth.user()}


def test_case():
    response = client.get("/auth-user")
    assert response.json()["user"]["name"] == "yoo"
