from enum import Enum

class AccountPricingResponse200DataTaxStatus(str, Enum):
    EXEMPT = "exempt"
    REVERSE_CHARGE = "reverse_charge"
    TAXABLE = "taxable"

    def __str__(self) -> str:
        return str(self.value)
