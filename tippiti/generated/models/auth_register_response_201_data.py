from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.user_resource import UserResource





T = TypeVar("T", bound="AuthRegisterResponse201Data")



@_attrs_define
class AuthRegisterResponse201Data:
    """ 
        Attributes:
            user (UserResource):
            token (str):
     """

    user: UserResource
    token: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.user_resource import UserResource
        user = self.user.to_dict()

        token = self.token


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "user": user,
            "token": token,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.user_resource import UserResource
        d = dict(src_dict)
        user = UserResource.from_dict(d.pop("user"))




        token = d.pop("token")

        auth_register_response_201_data = cls(
            user=user,
            token=token,
        )


        auth_register_response_201_data.additional_properties = d
        return auth_register_response_201_data

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
