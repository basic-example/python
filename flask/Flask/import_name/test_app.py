from flask import Flask

app = Flask(__name__)
client = app.test_client()


@app.route("/")
def hello_world():
    return "hello world"


def test_case():
    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"hello world"
