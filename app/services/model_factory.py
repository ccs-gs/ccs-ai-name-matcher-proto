from functools import lru_cache

from langchain_openai import AzureChatOpenAI

from app.config import get_settings, missing_azure_vars


@lru_cache(maxsize=1)
def get_chat_model():
    settings = get_settings()
    missing = missing_azure_vars(settings)

    if missing:
        raise RuntimeError("Missing required env vars: " + ", ".join(missing))

    return AzureChatOpenAI(
        azure_endpoint=settings.azure_openai_endpoint,
        openai_api_key=settings.azure_openai_key,
        azure_deployment=settings.azure_openai_deployment_name,
        openai_api_version=settings.azure_openai_api_version,
    )


