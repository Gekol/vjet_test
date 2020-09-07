from app import app


def test_valid_post():
    r = app.test_client().post('/', data="days=365&people=4&range=300",
                               content_type="application/x-www-form-urlencoded")
    assert r.status_code == 200
    assert r.json["result"] == 0.8207481076592033


def test_invalid_post():
    r = app.test_client().post('/', data="days=365&people=-4&range=300",
                               content_type="application/x-www-form-urlencoded")
    assert r.status_code == 400
    assert r.json["result"] == "Wrong data!!!"
