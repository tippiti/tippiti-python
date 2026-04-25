from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_sub_user_request_dictation_access import UpdateSubUserRequestDictationAccess
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateSubUserRequest")



@_attrs_define
class UpdateSubUserRequest:
    """ 
        Attributes:
            first_name (str | Unset):
            last_name (str | Unset):
            email (str | Unset):
            is_active (bool | Unset):
            dictation_access (UpdateSubUserRequestDictationAccess | Unset):
            folders (list[str] | Unset):
            permissions (list[bool] | None | Unset):
     """

    first_name: str | Unset = UNSET
    last_name: str | Unset = UNSET
    email: str | Unset = UNSET
    is_active: bool | Unset = UNSET
    dictation_access: UpdateSubUserRequestDictationAccess | Unset = UNSET
    folders: list[str] | Unset = UNSET
    permissions: list[bool] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        email = self.email

        is_active = self.is_active

        dictation_access: str | Unset = UNSET
        if not isinstance(self.dictation_access, Unset):
            dictation_access = self.dictation_access.value


        folders: list[str] | Unset = UNSET
        if not isinstance(self.folders, Unset):
            folders = self.folders



        permissions: list[bool] | None | Unset
        if isinstance(self.permissions, Unset):
            permissions = UNSET
        elif isinstance(self.permissions, list):
            permissions = self.permissions


        else:
            permissions = self.permissions


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if dictation_access is not UNSET:
            field_dict["dictation_access"] = dictation_access
        if folders is not UNSET:
            field_dict["folders"] = folders
        if permissions is not UNSET:
            field_dict["permissions"] = permissions

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        email = d.pop("email", UNSET)

        is_active = d.pop("is_active", UNSET)

        _dictation_access = d.pop("dictation_access", UNSET)
        dictation_access: UpdateSubUserRequestDictationAccess | Unset
        if isinstance(_dictation_access,  Unset):
            dictation_access = UNSET
        else:
            dictation_access = UpdateSubUserRequestDictationAccess(_dictation_access)




        folders = cast(list[str], d.pop("folders", UNSET))


        def _parse_permissions(data: object) -> list[bool] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                permissions_type_0 = cast(list[bool], data)

                return permissions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[bool] | None | Unset, data)

        permissions = _parse_permissions(d.pop("permissions", UNSET))


        update_sub_user_request = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
            is_active=is_active,
            dictation_access=dictation_access,
            folders=folders,
            permissions=permissions,
        )


        update_sub_user_request.additional_properties = d
        return update_sub_user_request

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
