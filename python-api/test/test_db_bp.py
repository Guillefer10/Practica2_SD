def test_db_success(client):
    resp = client.get("/db-test/")
    assert resp.status_code == 200
    assert b"records" in resp.data

def test_db_invalid(client):
    resp = client.get("/db-test/?invalid=true")
    assert resp.status_code == 500
    assert b"Fallo de acceso a BD" in resp.data
    assert b"invalid" in resp.data
    assert b"InvalidRequestError" in resp.data 