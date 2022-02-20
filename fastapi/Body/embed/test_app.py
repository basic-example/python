from fastapi import Body, FastAPI
from pydantic import BaseModel
from fastapi.testclient import TestClient

app = FastAPI()
client = TestClient(app)


class User(BaseModel):
    name: str
    age: int | None = None


@app.get("/man/embed/true")
async def hello_world(man: User = Body(None, embed=True)):
    return {"man": man}


@app.get("/man/embed/false")
async def hello_world(man: User = Body(..., embed=False)):
    return {"man": man}


@app.get("/both/embed/true")
async def hello_world(
    man: User = Body(..., embed=False), woman: User = Body(..., embed=False)
):
    return {"man": man, "woman": woman}


@app.get("/both/embed/false")
async def hello_world(
    man: User = Body(..., embed=True), woman: User = Body(..., embed=True)
):
    return {"man": man, "woman": woman}


def test_case_man_embed_true():
    response = client.get(
        "/man/embed/true",
        json={
            "man": {
                "name": "yoo",
                "age": 20,
            }
        },
    )

    assert response.json() == {"man": {"name": "yoo", "age": 20}}


def test_case_man_embed_false():
    response = client.get(
        "/man/embed/false",
        json={
            "name": "yoo",
            "age": 20,
        },
    )

    assert response.json() == {"man": {"name": "yoo", "age": 20}}


def test_case_both_embed_false():
    response = client.get(
        "/both/embed/false",
        json={"man": {"name": "yoo", "age": 20}, "woman": {"name": "yoo", "age": 20}},
    )

    assert response.json() == {
        "man": {"name": "yoo", "age": 20},
        "woman": {"name": "yoo", "age": 20},
    }


def test_case_both_embed_true():
    response = client.get(
        "/both/embed/true",
        json={"man": {"name": "yoo", "age": 20}, "woman": {"name": "yoo", "age": 20}},
    )

    assert response.json() == {
        "man": {"name": "yoo", "age": 20},
        "woman": {"name": "yoo", "age": 20},
    }
