from enum import Enum

class PaymentMethodStoreBodyGateway(str, Enum):
    STRIPE = "stripe"

    def __str__(self) -> str:
        return str(self.value)
