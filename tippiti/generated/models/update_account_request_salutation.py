from enum import Enum

class UpdateAccountRequestSalutation(str, Enum):
    FRAU = "Frau"
    HERR = "Herr"

    def __str__(self) -> str:
        return str(self.value)
