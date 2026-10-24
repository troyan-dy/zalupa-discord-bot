from pydantic import AnyUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file="local.env")

    bot_token: str
    sentry_dsn: AnyUrl
    env: str
