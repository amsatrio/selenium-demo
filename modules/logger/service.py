from pathlib import Path
import datetime
from enum import Enum
from config.environment_config import get_env
from model.logger import LogType

def _create_log_dir():
    env = get_env()
    Path(env.log_dir).mkdir(parents=True, exist_ok=True)

def _create_log_file(filename: str):
    env = get_env()
    file_path = f"{env.log_dir}/{filename}.log"
    try:
        with open(file_path, 'x') as file:
            return
    except FileExistsError:
        # print(f"the file '{file_path}' already exists")
        return

def _append_message_to_file(filename: str, message: str):
    env = get_env()
    file_path = f"{env.log_dir}/{filename}.log"
    try:
        with open(file_path, 'a') as file:
            file.write(message)
    except Exception as e:
        print(f"append message error: {e}")

def _print_log(status: str, message: str):
    env = get_env()
    now = datetime.datetime.now()
    x = now.strftime("%Y-%m-%d %H:%M:%S")
    output = f"\n{x} [{status}] {message}"
    
    if(env.log_type == LogType.STDOUT):
        print(output)
        return
    
    filename = "app"
    if(env.log_type == LogType.ROLLINGFILE):
        filename = now.strftime("%Y-%m-%d")
    
    _create_log_dir()
    _create_log_file(filename)
    _append_message_to_file(filename, output)

def logi(message: str):
    _print_log("INFO", message)

def loge(message: str):
    _print_log("ERROR", message)

def logw(message: str):
    _print_log("WARNING", message)

def logd(message: str):
    _print_log("DEBUG", message)
