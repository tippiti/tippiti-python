from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="AffiliatePayoutsResponse200DataItem")



@_attrs_define
class AffiliatePayoutsResponse200DataItem:
    """ 
        Attributes:
            id (int):
            amount (str):
            status (str):
            bank_holder (str):
            bank_iban (str):
            rejection_reason (None | str):
            requested_at (str):
            paid_at (str):
     """

    id: int
    amount: str
    status: str
    bank_holder: str
    bank_iban: str
    rejection_reason: None | str
    requested_at: str
    paid_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        amount = self.amount

        status = self.status

        bank_holder = self.bank_holder

        bank_iban = self.bank_iban

        rejection_reason: None | str
        rejection_reason = self.rejection_reason

        requested_at = self.requested_at

        paid_at = self.paid_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "amount": amount,
            "status": status,
            "bank_holder": bank_holder,
            "bank_iban": bank_iban,
            "rejection_reason": rejection_reason,
            "requested_at": requested_at,
            "paid_at": paid_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        amount = d.pop("amount")

        status = d.pop("status")

        bank_holder = d.pop("bank_holder")

        bank_iban = d.pop("bank_iban")

        def _parse_rejection_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rejection_reason = _parse_rejection_reason(d.pop("rejection_reason"))


        requested_at = d.pop("requested_at")

        paid_at = d.pop("paid_at")

        affiliate_payouts_response_200_data_item = cls(
            id=id,
            amount=amount,
            status=status,
            bank_holder=bank_holder,
            bank_iban=bank_iban,
            rejection_reason=rejection_reason,
            requested_at=requested_at,
            paid_at=paid_at,
        )


        affiliate_payouts_response_200_data_item.additional_properties = d
        return affiliate_payouts_response_200_data_item

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
