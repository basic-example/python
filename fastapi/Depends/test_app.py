from fastapi import Depends, FastAPI, Query
from fastapi.testclient import TestClient

app = FastAPI()
client = TestClient(app)


class QueryParams:
    def __init__(self, ids: list[int] = Query([])):
        self.ids = ids


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
    assert response.json() == {"limit": 10, "skip": 0, "query": {"ids": []}}

    response = client.get("/", params={"ids": [1, 2]})
    assert response.json() == {"limit": 10, "skip": 0, "query": {"ids": [1, 2]}}
