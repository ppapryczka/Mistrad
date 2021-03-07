from injection_action.injection_action import InjectionAction, MaskOperation
from typing import List


class VariableChangeInjectionAction(InjectionAction):
    variable_address: int
    variable_mask: int
    mask_operation: MaskOperation

    def __init__(self,
                 injection_address: int,
                 variable_address: int,
                 variable_mask: int,
                 mask_operation):

        super().__init__(injection_address)

        self.variable_address = variable_address
        self.variable_mask = variable_mask
        self.mask_operation = mask_operation

    def to_line_msg(self) -> List[str]:
        pass

    def get_line_number(self) -> int:
        pass
