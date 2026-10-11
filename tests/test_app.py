from fastapi.testclient import TestClient

from app import app

client = TestClient(app)


def test_welcome_root_returns_message():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ML API"}


def test_health_check_returns_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_predict_returns_class_name():
    response = client.post(
        "/predict",
        json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2,
        },
    )

    assert response.status_code == 200
    assert response.json() == {"prediction": "setosa"}


def test_predict_rejects_missing_feature():
    response = client.post("/predict", json={"sepal_length": 5.1})

    assert response.status_code == 422
