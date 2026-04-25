from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.account_pricing_response_200_data_tax_status import AccountPricingResponse200DataTaxStatus
from typing import Literal, cast






T = TypeVar("T", bound="AccountPricingResponse200Data")



@_attrs_define
class AccountPricingResponse200Data:
    """ 
        Attributes:
            price_per_1k_chars (float):
            min_topup_amount (float):
            tax_rate (float):
            tax_status (AccountPricingResponse200DataTaxStatus):
            currency (Literal['EUR']):
     """

    price_per_1k_chars: float
    min_topup_amount: float
    tax_rate: float
    tax_status: AccountPricingResponse200DataTaxStatus
    currency: Literal['EUR']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        price_per_1k_chars = self.price_per_1k_chars

        min_topup_amount = self.min_topup_amount

        tax_rate = self.tax_rate

        tax_status = self.tax_status.value

        currency = self.currency


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "price_per_1k_chars": price_per_1k_chars,
            "min_topup_amount": min_topup_amount,
            "tax_rate": tax_rate,
            "tax_status": tax_status,
            "currency": currency,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        price_per_1k_chars = d.pop("price_per_1k_chars")

        min_topup_amount = d.pop("min_topup_amount")

        tax_rate = d.pop("tax_rate")

        tax_status = AccountPricingResponse200DataTaxStatus(d.pop("tax_status"))




        currency = cast(Literal['EUR'] , d.pop("currency"))
        if currency != 'EUR':
            raise ValueError(f"currency must match const 'EUR', got '{currency}'")

        account_pricing_response_200_data = cls(
            price_per_1k_chars=price_per_1k_chars,
            min_topup_amount=min_topup_amount,
            tax_rate=tax_rate,
            tax_status=tax_status,
            currency=currency,
        )


        account_pricing_response_200_data.additional_properties = d
        return account_pricing_response_200_data

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
