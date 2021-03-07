from injection_action.injection_action import InjectionAction, MaskOperation

from typing import List, Set


class RegistersChangeInjectionAction(InjectionAction):
    registers_to_change: Set[str]
    registers_masks: Set[int]
    registers_mask_operations: Set[MaskOperation]

    def __init__(self,
                 injection_address: int,
                 registers_to_change: Set[str],
                 registers_masks: Set[int],
                 registers_mask_operations: Set[MaskOperation]):

        super().__init__(injection_address)

        self.registers_to_change = registers_to_change
        self.registers_masks = registers_masks
        self.registers_mask_operations = registers_mask_operations

    def to_line_msg(self) -> List[str]:
        pass

    def get_line_number(self) -> int:
        pass
