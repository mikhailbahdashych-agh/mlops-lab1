import joblib

from training import MODEL_PATH


def load_model(path: str = MODEL_PATH):
    return joblib.load(path)


def predict(model, features: list[float]) -> str:
    """Features order: sepal_length, sepal_width, petal_length, petal_width."""
    return model.predict([features])[0]
