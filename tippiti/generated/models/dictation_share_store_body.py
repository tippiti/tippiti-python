from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="DictationShareStoreBody")



@_attrs_define
class DictationShareStoreBody:
    """ 
        Attributes:
            password (None | str | Unset):
            allow_delete (bool | Unset):
            allow_archive (bool | Unset):
            show_notes (bool | Unset):
            expires_at (datetime.datetime | None | Unset):
     """

    password: None | str | Unset = UNSET
    allow_delete: bool | Unset = UNSET
    allow_archive: bool | Unset = UNSET
    show_notes: bool | Unset = UNSET
    expires_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password

        allow_delete = self.allow_delete

        allow_archive = self.allow_archive

        show_notes = self.show_notes

        expires_at: None | str | Unset
        if isinstance(self.expires_at, Unset):
            expires_at = UNSET
        elif isinstance(self.expires_at, datetime.datetime):
            expires_at = self.expires_at.isoformat()
        else:
            expires_at = self.expires_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if password is not UNSET:
            field_dict["password"] = password
        if allow_delete is not UNSET:
            field_dict["allow_delete"] = allow_delete
        if allow_archive is not UNSET:
            field_dict["allow_archive"] = allow_archive
        if show_notes is not UNSET:
            field_dict["show_notes"] = show_notes
        if expires_at is not UNSET:
            field_dict["expires_at"] = expires_at

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))


        allow_delete = d.pop("allow_delete", UNSET)

        allow_archive = d.pop("allow_archive", UNSET)

        show_notes = d.pop("show_notes", UNSET)

        def _parse_expires_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                expires_at_type_0 = isoparse(data)



                return expires_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        expires_at = _parse_expires_at(d.pop("expires_at", UNSET))


        dictation_share_store_body = cls(
            password=password,
            allow_delete=allow_delete,
            allow_archive=allow_archive,
            show_notes=show_notes,
            expires_at=expires_at,
        )


        dictation_share_store_body.additional_properties = d
        return dictation_share_store_body

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
