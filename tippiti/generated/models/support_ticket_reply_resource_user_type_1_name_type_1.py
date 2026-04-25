from enum import Enum

class SupportTicketReplyResourceUserType1NameType1(str, Enum):
    GAST = "Gast"

    def __str__(self) -> str:
        return str(self.value)
