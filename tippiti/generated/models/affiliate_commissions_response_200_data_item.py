from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="AffiliateCommissionsResponse200DataItem")



@_attrs_define
class AffiliateCommissionsResponse200DataItem:
    """ 
        Attributes:
            id (int):
            net_amount (str):
            commission_rate (str):
            commission_amount (str):
            status (str):
            rejection_reason (None | str):
            available_at (str):
            created_at (str):
     """

    id: int
    net_amount: str
    commission_rate: str
    commission_amount: str
    status: str
    rejection_reason: None | str
    available_at: str
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        net_amount = self.net_amount

        commission_rate = self.commission_rate

        commission_amount = self.commission_amount

        status = self.status

        rejection_reason: None | str
        rejection_reason = self.rejection_reason

        available_at = self.available_at

        created_at = self.created_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "net_amount": net_amount,
            "commission_rate": commission_rate,
            "commission_amount": commission_amount,
            "status": status,
            "rejection_reason": rejection_reason,
            "available_at": available_at,
            "created_at": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        net_amount = d.pop("net_amount")

        commission_rate = d.pop("commission_rate")

        commission_amount = d.pop("commission_amount")

        status = d.pop("status")

        def _parse_rejection_reason(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        rejection_reason = _parse_rejection_reason(d.pop("rejection_reason"))


        available_at = d.pop("available_at")

        created_at = d.pop("created_at")

        affiliate_commissions_response_200_data_item = cls(
            id=id,
            net_amount=net_amount,
            commission_rate=commission_rate,
            commission_amount=commission_amount,
            status=status,
            rejection_reason=rejection_reason,
            available_at=available_at,
            created_at=created_at,
        )


        affiliate_commissions_response_200_data_item.additional_properties = d
        return affiliate_commissions_response_200_data_item

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
