from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="AutoTopupUpdateResponse200Data")



@_attrs_define
class AutoTopupUpdateResponse200Data:
    """ 
        Attributes:
            enabled (bool):
            threshold (int | None):
            amount (float | None):
            payment_method_id (int | None):
     """

    enabled: bool
    threshold: int | None
    amount: float | None
    payment_method_id: int | None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        threshold: int | None
        threshold = self.threshold

        amount: float | None
        amount = self.amount

        payment_method_id: int | None
        payment_method_id = self.payment_method_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "enabled": enabled,
            "threshold": threshold,
            "amount": amount,
            "payment_method_id": payment_method_id,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        def _parse_threshold(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        threshold = _parse_threshold(d.pop("threshold"))


        def _parse_amount(data: object) -> float | None:
            if data is None:
                return data
            return cast(float | None, data)

        amount = _parse_amount(d.pop("amount"))


        def _parse_payment_method_id(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        payment_method_id = _parse_payment_method_id(d.pop("payment_method_id"))


        auto_topup_update_response_200_data = cls(
            enabled=enabled,
            threshold=threshold,
            amount=amount,
            payment_method_id=payment_method_id,
        )


        auto_topup_update_response_200_data.additional_properties = d
        return auto_topup_update_response_200_data

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
