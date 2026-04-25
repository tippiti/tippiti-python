from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.affiliate_dashboard_response_200_data_conversion_rate_type_1 import AffiliateDashboardResponse200DataConversionRateType1
from typing import cast






T = TypeVar("T", bound="AffiliateDashboardResponse200Data")



@_attrs_define
class AffiliateDashboardResponse200Data:
    """ 
        Attributes:
            referral_count (int):
            total_earned (float):
            available_balance (float):
            pending_balance (float):
            pending_payout (float):
            paid_out (float):
            total_clicks (int):
            unique_clicks (int):
            conversion_rate (AffiliateDashboardResponse200DataConversionRateType1 | float):
            commission_rate (float):
            min_payout_amount (float):
            holding_days (int | None):
            cookie_days (int):
            affiliate_link_code (str):
     """

    referral_count: int
    total_earned: float
    available_balance: float
    pending_balance: float
    pending_payout: float
    paid_out: float
    total_clicks: int
    unique_clicks: int
    conversion_rate: AffiliateDashboardResponse200DataConversionRateType1 | float
    commission_rate: float
    min_payout_amount: float
    holding_days: int | None
    cookie_days: int
    affiliate_link_code: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        referral_count = self.referral_count

        total_earned = self.total_earned

        available_balance = self.available_balance

        pending_balance = self.pending_balance

        pending_payout = self.pending_payout

        paid_out = self.paid_out

        total_clicks = self.total_clicks

        unique_clicks = self.unique_clicks

        conversion_rate: float | int
        if isinstance(self.conversion_rate, AffiliateDashboardResponse200DataConversionRateType1):
            conversion_rate = self.conversion_rate.value
        else:
            conversion_rate = self.conversion_rate

        commission_rate = self.commission_rate

        min_payout_amount = self.min_payout_amount

        holding_days: int | None
        holding_days = self.holding_days

        cookie_days = self.cookie_days

        affiliate_link_code = self.affiliate_link_code


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "referral_count": referral_count,
            "total_earned": total_earned,
            "available_balance": available_balance,
            "pending_balance": pending_balance,
            "pending_payout": pending_payout,
            "paid_out": paid_out,
            "total_clicks": total_clicks,
            "unique_clicks": unique_clicks,
            "conversion_rate": conversion_rate,
            "commission_rate": commission_rate,
            "min_payout_amount": min_payout_amount,
            "holding_days": holding_days,
            "cookie_days": cookie_days,
            "affiliate_link_code": affiliate_link_code,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        referral_count = d.pop("referral_count")

        total_earned = d.pop("total_earned")

        available_balance = d.pop("available_balance")

        pending_balance = d.pop("pending_balance")

        pending_payout = d.pop("pending_payout")

        paid_out = d.pop("paid_out")

        total_clicks = d.pop("total_clicks")

        unique_clicks = d.pop("unique_clicks")

        def _parse_conversion_rate(data: object) -> AffiliateDashboardResponse200DataConversionRateType1 | float:
            try:
                if not isinstance(data, int):
                    raise TypeError()
                conversion_rate_type_1 = AffiliateDashboardResponse200DataConversionRateType1(data)



                return conversion_rate_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(AffiliateDashboardResponse200DataConversionRateType1 | float, data)

        conversion_rate = _parse_conversion_rate(d.pop("conversion_rate"))


        commission_rate = d.pop("commission_rate")

        min_payout_amount = d.pop("min_payout_amount")

        def _parse_holding_days(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        holding_days = _parse_holding_days(d.pop("holding_days"))


        cookie_days = d.pop("cookie_days")

        affiliate_link_code = d.pop("affiliate_link_code")

        affiliate_dashboard_response_200_data = cls(
            referral_count=referral_count,
            total_earned=total_earned,
            available_balance=available_balance,
            pending_balance=pending_balance,
            pending_payout=pending_payout,
            paid_out=paid_out,
            total_clicks=total_clicks,
            unique_clicks=unique_clicks,
            conversion_rate=conversion_rate,
            commission_rate=commission_rate,
            min_payout_amount=min_payout_amount,
            holding_days=holding_days,
            cookie_days=cookie_days,
            affiliate_link_code=affiliate_link_code,
        )


        affiliate_dashboard_response_200_data.additional_properties = d
        return affiliate_dashboard_response_200_data

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
