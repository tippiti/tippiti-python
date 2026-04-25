from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="ChangePasswordRequest")



@_attrs_define
class ChangePasswordRequest:
    """ 
        Attributes:
            current_password (str):
            password (str):
            password_confirmation (str):
     """

    current_password: str
    password: str
    password_confirmation: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        current_password = self.current_password

        password = self.password

        password_confirmation = self.password_confirmation


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "current_password": current_password,
            "password": password,
            "password_confirmation": password_confirmation,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        current_password = d.pop("current_password")

        password = d.pop("password")

        password_confirmation = d.pop("password_confirmation")

        change_password_request = cls(
            current_password=current_password,
            password=password,
            password_confirmation=password_confirmation,
        )


        change_password_request.additional_properties = d
        return change_password_request

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
