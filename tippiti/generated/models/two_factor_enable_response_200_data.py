from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="TwoFactorEnableResponse200Data")



@_attrs_define
class TwoFactorEnableResponse200Data:
    """ 
        Attributes:
            secret (str):
            qr_code_url (str):
     """

    secret: str
    qr_code_url: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        secret = self.secret

        qr_code_url = self.qr_code_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "secret": secret,
            "qr_code_url": qr_code_url,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        secret = d.pop("secret")

        qr_code_url = d.pop("qr_code_url")

        two_factor_enable_response_200_data = cls(
            secret=secret,
            qr_code_url=qr_code_url,
        )


        two_factor_enable_response_200_data.additional_properties = d
        return two_factor_enable_response_200_data

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
