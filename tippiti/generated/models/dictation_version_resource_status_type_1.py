from enum import Enum

class DictationVersionResourceStatusType1(str, Enum):
    ACTIVE = "active"

    def __str__(self) -> str:
        return str(self.value)
