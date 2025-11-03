from pydantic_settings import BaseSettings
from functools import lru_cache
from model.logger import LogType

class Env(BaseSettings):
    username: str
    password: str
    url: str
    wait_time: int
    log_dir: str = "logs"
    log_type: LogType

    class Config:
        env_file = ".env"


@lru_cache()
def get_env():
    return Env()