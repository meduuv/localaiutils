from localaiutils import endpoint, model_name


def test_helpers():
    assert endpoint("http://localhost:8000", "/v1/models") == "http://localhost:8000/v1/models"
    assert model_name({"model_name": "demo"}) == "demo"
