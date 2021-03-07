from enum import Enum
from typing import Any


class State(Enum):
    WAITING_FOR_WAITING_FOR_CONF_MSG = 1
    WAITING_FOR_CONF_RECEIVED_MSG = 2
    WAITING_FOR_CONF_INFO_MSG = 3
    CONF_INCORRECT_MSG = 4
    CONF_CORRECT_MSG = 5
    GETTING_LOGS = 6


MESSAGE_LINE_SIZE: int = 30


WAITING_FOR_CONF_MSG: bytes = b"CONF_WAITING"
CONF_RECEIVED_MSG: bytes = b"CONF_RECEIVED"
CONF_INFO_MSG: bytes = b"CONF_INFO"
CONF_CORRECT_MSG: bytes = b"CONF_CORRECT"
CONF_INCORRECT_MSG: bytes = b"CONF_INCORRECT"
CONF_STATUS_MSG_STR: bytes = b"CONF_STATUS"


def create_empty_line(data: Any)-> bytes:
    data_as_str = str(data)
    str_to_add_len = MESSAGE_LINE_SIZE - len(data_as_str)

    for i in range(str_to_add_len):
        data_as_str += '\0'

    return data_as_str

if __name__ == "__main__":
    a = create_empty_line("nie wiem")
    print(a, len(a))




