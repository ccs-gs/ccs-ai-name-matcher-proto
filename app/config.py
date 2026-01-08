from functools import lru_cache
from typing import Optional, Tuple

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Centralized, typed configuration.

    Reads from environment variables and (optionally) repo-root `.env` / `.ev`.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    azure_openai_endpoint: str = ""
    azure_openai_key: str = ""
    azure_openai_deployment_name: str = ""
    azure_openai_api_version: str = ""


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


def missing_azure_vars(settings: Optional[Settings] = None) -> Tuple[str, ...]:
    s = settings or get_settings()
    missing = []
    if not s.azure_openai_endpoint:
        missing.append("AZURE_OPENAI_ENDPOINT")
    if not s.azure_openai_key:
        missing.append("AZURE_OPENAI_KEY")
    if not s.azure_openai_deployment_name:
        missing.append("AZURE_OPENAI_DEPLOYMENT_NAME")
    if not s.azure_openai_api_version:
        missing.append("AZURE_OPENAI_API_VERSION")
    return tuple(missing)


