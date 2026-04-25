from enum import Enum

class DictationAiLogResourceResultType3Type1(str, Enum):
    FAIL = "fail"
    PASS = "pass"

    def __str__(self) -> str:
        return str(self.value)
