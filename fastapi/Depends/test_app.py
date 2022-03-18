from fastapi import Depends, FastAPI, Query
from fastapi.testclient import TestClient

app = FastAPI()
client = TestClient(app)
customDict = {"x": 10, "y": 20}


class CustomClass:
    def __init__(self, data=Depends(lambda: customDict)):
        self.prop = "something"
        self.data = data


class QueryParams:
    def __init__(
        self,
        ids: list[int] = Query([]),
        obj=Depends(CustomClass),
    ):
        self.ids = ids
        self.obj = obj


class ListParams:
    def __init__(
        self,
        query: QueryParams = Depends(),
        skip: int = Query(0),
        limit: int = Query(10),
    ):
        self.skip = skip
        self.limit = limit
        self.query = query


@app.get("/")
async def hello_world(params: ListParams = Depends()):
    return params


def test_case():
    response = client.get("/")
    assert response.json() == {
        "limit": 10,
        "skip": 0,
        "query": {
            "obj": {"prop": "something", "data": {"x": 10, "y": 20}},
            "ids": [],
        },
    }

    response = client.get("/", params={"ids": [1, 2]})
    assert response.json() == {
        "limit": 10,
        "skip": 0,
        "query": {
            "obj": {"prop": "something", "data": {"x": 10, "y": 20}},
            "ids": [1, 2],
        },
    }