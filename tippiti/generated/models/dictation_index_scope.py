from enum import Enum

class DictationIndexScope(str, Enum):
    ARCHIVED = "archived"

    def __str__(self) -> str:
        return str(self.value)
