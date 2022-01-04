from pydantic import AnyUrl, BaseSettings


class Settings(BaseSettings):
    bot_token: str
    sentry_dsn: AnyUrl
    env: str = "local"

    class Config:
        env_file = "local.env"
