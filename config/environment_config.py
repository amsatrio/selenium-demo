from pydantic_settings import BaseSettings
from functools import lru_cache

class Env(BaseSettings):
    username: str
    password: str
    url: str
    wait_time: int

    class Config:
        env_file = ".env"


@lru_cache()
def get_env():
    return Env()