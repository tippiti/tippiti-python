from enum import Enum

class UpdateSubUserRequestDictationAccess(str, Enum):
    ALL = "all"
    FOLDERS = "folders"
    SPECIFIC = "specific"

    def __str__(self) -> str:
        return str(self.value)
