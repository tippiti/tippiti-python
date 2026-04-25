from enum import Enum

class AffiliateChartDataPeriod(str, Enum):
    ALL = "all"
    VALUE_0 = "30d"
    VALUE_1 = "1y"

    def __str__(self) -> str:
        return str(self.value)
