from enum import Enum

class LogType(Enum):
    STDOUT = "stdout"
    FILE = "file"
    ROLLINGFILE = "rollingfile"