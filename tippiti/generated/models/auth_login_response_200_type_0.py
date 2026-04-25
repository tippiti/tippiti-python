from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.auth_login_response_200_type_0_data import AuthLoginResponse200Type0Data





T = TypeVar("T", bound="AuthLoginResponse200Type0")



@_attrs_define
class AuthLoginResponse200Type0:
    """ 
        Attributes:
            success (bool):
            data (AuthLoginResponse200Type0Data):
     """

    success: bool
    data: AuthLoginResponse200Type0Data
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.auth_login_response_200_type_0_data import AuthLoginResponse200Type0Data
        success = self.success

        data = self.data.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "success": success,
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.auth_login_response_200_type_0_data import AuthLoginResponse200Type0Data
        d = dict(src_dict)
        success = d.pop("success")

        data = AuthLoginResponse200Type0Data.from_dict(d.pop("data"))




        auth_login_response_200_type_0 = cls(
            success=success,
            data=data,
        )


        auth_login_response_200_type_0.additional_properties = d
        return auth_login_response_200_type_0

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
