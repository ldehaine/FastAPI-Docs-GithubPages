import json

from fastapi.testclient import TestClient

from main import my_awesome_api

client = TestClient(my_awesome_api)
with open("openapi.json", "w") as f:
    json.dump(client.get("/openapi.json").json(), f, indent=4)
