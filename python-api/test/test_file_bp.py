def test_file_success(tmp_path, client):
    # crea un fichero temporal
    p = tmp_path / "data.txt"
    p.write_text("contenido")
    resp = client.get(f"/file-test/?path={p}")
    assert resp.status_code == 200
    assert b"contenido" in resp.data

def test_file_error(client):
    resp = client.get("/file-test/?path=no_existe.txt")
    assert resp.status_code == 500
    assert b"Fallo al leer archivo" in resp.data
    assert b"no_existe.txt" in resp.data
    assert b"FileNotFoundError" in resp.data
    assert b"no such file or directory" in resp.data

