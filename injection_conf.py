import logging
from typing import List
from uart_connection_utils import create_empty_line
import sys

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger = logging.getLogger(__name__)


class InjectionAction():
    injection_address: int
    global_variable_address: int
    global_variable_value: int

    def __init__(self,
                 injection_address: int,
                 global_variable_address: int,
                 global_variable_value):
        self.injection_address = injection_address
        self.global_variable_address = global_variable_address
        self.global_variable_value = global_variable_value
        logger.info(f"Create injection action")


    def to_line_msg(self) -> List[str]:
        return [create_empty_line(self.injection_address),
                create_empty_line(self.global_variable_address),
                create_empty_line(self.global_variable_value)]

    @staticmethod
    def get_line_number() -> int:
        return 3


class InjectionConf():
    actions: List[InjectionAction]
    version: str = "0.1"

    def __init__(self, actions: List[InjectionAction]):
        self.actions = actions

    def get_conf_as_lines(self):
        conf_bytes_lines = []

        conf_bytes_lines.append(create_empty_line(f"version = {self.version}"))
        conf_bytes_lines.append(create_empty_line(len(self.actions)))
        conf_bytes_lines.append(create_empty_line(sum([i.get_line_number() for i in self.actions]) + 3))

        for action in self.actions:
            conf_bytes_lines.extend(action.to_line_msg())

        return conf_bytes_lines

def get_dummy_configuration() -> InjectionConf:
    action1 = InjectionAction(134219193, 536870912, 150)
    action2 = InjectionAction(134219233, 536870916, 45)

    conf = InjectionConf(actions=[action1, action2])

    return conf

if __name__ == "__main__":
    get_dummy_configuration()