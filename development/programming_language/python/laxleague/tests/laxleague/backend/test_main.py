from fastapi.testclient import TestClient

from laxleague.backend import main


client = TestClient(main.app)


def test_main():
    response = client.get("/")
    assert 200 == response.status_code
    assert {"msg": "Hello World"} == response.json()
