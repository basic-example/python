import pytest
from fastapi import Depends, FastAPI
from fastapi.responses import JSONResponse
from fastapi.testclient import TestClient

app = FastAPI()
client = TestClient(app)
arr = []


class CustomException(Exception):
    pass


@app.exception_handler(Exception)
def exception_handler1(request, exception):
    arr.append("exception1")
    return JSONResponse({}, 200)


@app.exception_handler(CustomException)
def exception_handler0(request, exception):
    arr.append("exception0")
    return JSONResponse({}, 200)


@app.exception_handler(Exception)
def exception_handler2(request, exception):
    arr.append("exception2")
    return JSONResponse({}, 200)


@app.get("/error")
async def error():
    raise CustomException


def test_case():
    result = client.get("/error")

    assert len(arr) == 1
    assert arr[0] == "exception0"
