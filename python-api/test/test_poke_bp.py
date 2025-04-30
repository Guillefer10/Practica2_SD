def test_poke_success(monkeypatch, client):
    class DummyResp:
        status_code = 200
        def raise_for_status(self): pass
        def json(self): return {"name":"test","height":1,"weight":1,"types":[{"type":{"name":"x"}}]}
    monkeypatch.setattr("blueprints.poke_bp.requests.get", lambda *args, **kw: DummyResp())
    resp = client.get("/poke-test/?name=test")
    assert resp.status_code == 200
    assert b"test" in resp.data

def test_poke_error(monkeypatch, client):
    from requests.exceptions import RequestException
    def bad_get(*args, **kw): raise RequestException("fail")
    monkeypatch.setattr("blueprints.poke_bp.requests.get", bad_get)
    resp = client.get("/poke-test/?name=test")
    assert resp.status_code == 502
    assert b"Fallo en llamada a PokeAPI" in resp.data
    assert b"test" in resp.data
    assert b"RequestException" in resp.data