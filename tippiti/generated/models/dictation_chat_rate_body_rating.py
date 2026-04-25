from enum import Enum

class DictationChatRateBodyRating(str, Enum):
    DOWN = "down"
    UP = "up"

    def __str__(self) -> str:
        return str(self.value)
