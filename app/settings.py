from pydantic import BaseSetting


class Settings(BaseSetting):
    bot_token: str
