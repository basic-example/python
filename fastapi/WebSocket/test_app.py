from fastapi import FastAPI, WebSocket
from fastapi.testclient import TestClient

app = FastAPI()


@app.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    await websocket.send_json({"msg": "Hello World1"})
    await websocket.send_json({"msg": "Hello World2"})
    await websocket.close()


client = TestClient(app)


def test_case():
    with client.websocket_connect("/") as websocket:
        assert websocket.receive_json() == {"msg": "Hello World1"}
        assert websocket.receive_json() == {"msg": "Hello World2"}
