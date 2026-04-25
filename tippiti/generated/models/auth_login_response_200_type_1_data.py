from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="AuthLoginResponse200Type1Data")



@_attrs_define
class AuthLoginResponse200Type1Data:
    """ 
        Attributes:
            two_factor_required (bool):
            two_factor_token (str):
     """

    two_factor_required: bool
    two_factor_token: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        two_factor_required = self.two_factor_required

        two_factor_token = self.two_factor_token


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "two_factor_required": two_factor_required,
            "two_factor_token": two_factor_token,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        two_factor_required = d.pop("two_factor_required")

        two_factor_token = d.pop("two_factor_token")

        auth_login_response_200_type_1_data = cls(
            two_factor_required=two_factor_required,
            two_factor_token=two_factor_token,
        )


        auth_login_response_200_type_1_data.additional_properties = d
        return auth_login_response_200_type_1_data

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
