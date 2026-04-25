from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AffiliateReferralsResponse200DataItem")



@_attrs_define
class AffiliateReferralsResponse200DataItem:
    """ 
        Attributes:
            id (int):
            created_at (str):
            is_active (bool):
            total_commission (float):
            pending_commission (float):
     """

    id: int
    created_at: str
    is_active: bool
    total_commission: float
    pending_commission: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        created_at = self.created_at

        is_active = self.is_active

        total_commission = self.total_commission

        pending_commission = self.pending_commission


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "created_at": created_at,
            "is_active": is_active,
            "total_commission": total_commission,
            "pending_commission": pending_commission,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        created_at = d.pop("created_at")

        is_active = d.pop("is_active")

        total_commission = d.pop("total_commission")

        pending_commission = d.pop("pending_commission")

        affiliate_referrals_response_200_data_item = cls(
            id=id,
            created_at=created_at,
            is_active=is_active,
            total_commission=total_commission,
            pending_commission=pending_commission,
        )


        affiliate_referrals_response_200_data_item.additional_properties = d
        return affiliate_referrals_response_200_data_item

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
