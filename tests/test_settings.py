import pytest
from pydantic import ValidationError

from settings import Settings


def test_settings_are_loaded_from_env_test_file():
    settings = Settings()

    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "ml-api-test"
    assert settings.API_KEY == "sk-fake-test-key"


def test_unknown_environment_is_rejected():
    with pytest.raises(ValidationError):
        Settings(ENVIRONMENT="xyz")
