from enum import Enum

class DictationVersionResourceFormatType1(str, Enum):
    MARKDOWN = "markdown"

    def __str__(self) -> str:
        return str(self.value)
