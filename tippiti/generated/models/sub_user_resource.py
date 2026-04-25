from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="SubUserResource")



@_attrs_define
class SubUserResource:
    """ 
        Attributes:
            id (str):  Example: aid-xyz12345.
            first_name (str):
            last_name (str):
            name (str):
            email (str):
            status (str):
            is_active (str):
            last_login_at (str):
            invited_at (str):
            created_at (str):
            permissions (str):
            dictation_access (str):
            folders (list[str]):
            shared_dictations (str):
     """

    id: str
    first_name: str
    last_name: str
    name: str
    email: str
    status: str
    is_active: str
    last_login_at: str
    invited_at: str
    created_at: str
    permissions: str
    dictation_access: str
    folders: list[str]
    shared_dictations: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        first_name = self.first_name

        last_name = self.last_name

        name = self.name

        email = self.email

        status = self.status

        is_active = self.is_active

        last_login_at = self.last_login_at

        invited_at = self.invited_at

        created_at = self.created_at

        permissions = self.permissions

        dictation_access = self.dictation_access

        folders = self.folders



        shared_dictations = self.shared_dictations


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "first_name": first_name,
            "last_name": last_name,
            "name": name,
            "email": email,
            "status": status,
            "is_active": is_active,
            "last_login_at": last_login_at,
            "invited_at": invited_at,
            "created_at": created_at,
            "permissions": permissions,
            "dictation_access": dictation_access,
            "folders": folders,
            "shared_dictations": shared_dictations,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        name = d.pop("name")

        email = d.pop("email")

        status = d.pop("status")

        is_active = d.pop("is_active")

        last_login_at = d.pop("last_login_at")

        invited_at = d.pop("invited_at")

        created_at = d.pop("created_at")

        permissions = d.pop("permissions")

        dictation_access = d.pop("dictation_access")

        folders = cast(list[str], d.pop("folders"))


        shared_dictations = d.pop("shared_dictations")

        sub_user_resource = cls(
            id=id,
            first_name=first_name,
            last_name=last_name,
            name=name,
            email=email,
            status=status,
            is_active=is_active,
            last_login_at=last_login_at,
            invited_at=invited_at,
            created_at=created_at,
            permissions=permissions,
            dictation_access=dictation_access,
            folders=folders,
            shared_dictations=shared_dictations,
        )


        sub_user_resource.additional_properties = d
        return sub_user_resource

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
