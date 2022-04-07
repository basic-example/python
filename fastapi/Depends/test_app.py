from fastapi import Depends, FastAPI, Query
from fastapi.testclient import TestClient

app = FastAPI()
client = TestClient(app)
count = 0
customDict = {"x": 10, "y": 20}

def increase():
    global count
    count = count + 1

class CustomClass:
    def __init__(
        self,
        data = Depends(lambda: customDict),
        fn1 = Depends(increase),
        fn2 = Depends(increase),
        fn3 = Depends(increase),
    ):
        self.prop = "something"
        self.data = data


class QueryParams:
    def __init__(
        self,
        ids: list[int] = Query([]),
        obj = Depends(CustomClass),
        fn1 = Depends(increase),
        fn2 = Depends(increase),
        fn3 = Depends(increase),
    ):
        self.ids = ids
        self.obj = obj


class ListParams:
    def __init__(
        self,
        query: QueryParams = Depends(),
        skip: int = Query(0),
        limit: int = Query(10),
        fn1 = Depends(increase),
        fn2 = Depends(increase),
        fn3 = Depends(increase),
    ):
        self.skip = skip
        self.limit = limit
        self.query = query


@app.get("/")
async def hello_world(params: ListParams = Depends()):
    return params


def test_case():

    global count
    response = client.get("/")
    assert response.json() == {
        "limit": 10,
        "skip": 0,
        "query": {
            "obj": {"prop": "something", "data": {"x": 10, "y": 20}},
            "ids": [],
        },
    }
    assert count == 1

    response = client.get("/", params={"ids": [1, 2]})
    assert response.json() == {
        "limit": 10,
        "skip": 0,
        "query": {
            "obj": {"prop": "something", "data": {"x": 10, "y": 20}},
            "ids": [1, 2],
        },
    }
    assert count == 2
