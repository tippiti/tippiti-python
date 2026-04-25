from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="PaymentMethodResource")



@_attrs_define
class PaymentMethodResource:
    """ 
        Attributes:
            id (str):  Example: aid-xyz12345.
            gateway (str):
            type_ (str):
            brand (None | str):
            last_four (None | str):
            expiry_month (int | None):
            expiry_year (int | None):
            is_default (bool):
            description (None | str):
            label (str):
            created_at (str):
     """

    id: str
    gateway: str
    type_: str
    brand: None | str
    last_four: None | str
    expiry_month: int | None
    expiry_year: int | None
    is_default: bool
    description: None | str
    label: str
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        gateway = self.gateway

        type_ = self.type_

        brand: None | str
        brand = self.brand

        last_four: None | str
        last_four = self.last_four

        expiry_month: int | None
        expiry_month = self.expiry_month

        expiry_year: int | None
        expiry_year = self.expiry_year

        is_default = self.is_default

        description: None | str
        description = self.description

        label = self.label

        created_at = self.created_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "gateway": gateway,
            "type": type_,
            "brand": brand,
            "last_four": last_four,
            "expiry_month": expiry_month,
            "expiry_year": expiry_year,
            "is_default": is_default,
            "description": description,
            "label": label,
            "created_at": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        gateway = d.pop("gateway")

        type_ = d.pop("type")

        def _parse_brand(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        brand = _parse_brand(d.pop("brand"))


        def _parse_last_four(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_four = _parse_last_four(d.pop("last_four"))


        def _parse_expiry_month(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        expiry_month = _parse_expiry_month(d.pop("expiry_month"))


        def _parse_expiry_year(data: object) -> int | None:
            if data is None:
                return data
            return cast(int | None, data)

        expiry_year = _parse_expiry_year(d.pop("expiry_year"))


        is_default = d.pop("is_default")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))


        label = d.pop("label")

        created_at = d.pop("created_at")

        payment_method_resource = cls(
            id=id,
            gateway=gateway,
            type_=type_,
            brand=brand,
            last_four=last_four,
            expiry_month=expiry_month,
            expiry_year=expiry_year,
            is_default=is_default,
            description=description,
            label=label,
            created_at=created_at,
        )


        payment_method_resource.additional_properties = d
        return payment_method_resource

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
