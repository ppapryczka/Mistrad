from injection_action.injection_action import InjectionAction, MaskOperation

from typing import Set, List


class LogInjectionAction(InjectionAction):
    log_id: int
    registers_to_log: Set[str]
    variables_addresses_to_log: Set[int]

    def __init__(self,
                 injection_address: int,
                 log_id: int,
                 registers_to_log: Set[str],
                 variables_addresses_to_log: Set[int]):
        super().__init__(injection_address)

        self.log_id = log_id
        self.registers_to_log = registers_to_log
        self.variables_addresses_to_log = variables_addresses_to_log

    def to_line_msg(self) -> List[str]:
        pass

    def get_line_number(self) -> int:
        pass

