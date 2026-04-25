from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AutoTopupUpdateBody")



@_attrs_define
class AutoTopupUpdateBody:
    """ 
        Attributes:
            enabled (bool):
            threshold (int | None | Unset):
            amount (float | None | Unset):
            payment_method_id (str | Unset): Decoded from Sqid by DecodeSqidIds middleware Example: aid-xyz12345.
     """

    enabled: bool
    threshold: int | None | Unset = UNSET
    amount: float | None | Unset = UNSET
    payment_method_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        enabled = self.enabled

        threshold: int | None | Unset
        if isinstance(self.threshold, Unset):
            threshold = UNSET
        else:
            threshold = self.threshold

        amount: float | None | Unset
        if isinstance(self.amount, Unset):
            amount = UNSET
        else:
            amount = self.amount

        payment_method_id = self.payment_method_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "enabled": enabled,
        })
        if threshold is not UNSET:
            field_dict["threshold"] = threshold
        if amount is not UNSET:
            field_dict["amount"] = amount
        if payment_method_id is not UNSET:
            field_dict["payment_method_id"] = payment_method_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        enabled = d.pop("enabled")

        def _parse_threshold(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        threshold = _parse_threshold(d.pop("threshold", UNSET))


        def _parse_amount(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        amount = _parse_amount(d.pop("amount", UNSET))


        payment_method_id = d.pop("payment_method_id", UNSET)

        auto_topup_update_body = cls(
            enabled=enabled,
            threshold=threshold,
            amount=amount,
            payment_method_id=payment_method_id,
        )


        auto_topup_update_body.additional_properties = d
        return auto_topup_update_body

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
