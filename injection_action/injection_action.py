from abc import ABC, abstractmethod
from typing import List
from enum import Enum


class MaskOperation(Enum):
    OR = 1
    XOR = 0


class InjectionAction(ABC):
    injection_address: int

    def __init__(self, injection_address: int) -> None:
        self.injection_address = injection_address

    @abstractmethod
    def to_line_msg(self) -> List[str]:
        pass

    @abstractmethod
    def get_line_number(self) -> int:
        pass
