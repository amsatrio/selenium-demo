import datetime

def logi(message: str):
    x = datetime.datetime.now()
    print(f"\n{x} [INFO] {message}")

def loge(message: str):
    x = datetime.datetime.now()
    print(f"\n{x} [ERROR] {message}")