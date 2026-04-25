from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="DictationUpdateBody")



@_attrs_define
class DictationUpdateBody:
    """ 
        Attributes:
            title (str | Unset):
            client_name (None | str | Unset):
            comment (None | str | Unset):
            instruction_set_id (str | Unset):  Example: aid-xyz12345.
            folders (list[str] | Unset):
            shared_with (list[str] | None | Unset):
     """

    title: str | Unset = UNSET
    client_name: None | str | Unset = UNSET
    comment: None | str | Unset = UNSET
    instruction_set_id: str | Unset = UNSET
    folders: list[str] | Unset = UNSET
    shared_with: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        title = self.title

        client_name: None | str | Unset
        if isinstance(self.client_name, Unset):
            client_name = UNSET
        else:
            client_name = self.client_name

        comment: None | str | Unset
        if isinstance(self.comment, Unset):
            comment = UNSET
        else:
            comment = self.comment

        instruction_set_id = self.instruction_set_id

        folders: list[str] | Unset = UNSET
        if not isinstance(self.folders, Unset):
            folders = self.folders



        shared_with: list[str] | None | Unset
        if isinstance(self.shared_with, Unset):
            shared_with = UNSET
        elif isinstance(self.shared_with, list):
            shared_with = self.shared_with


        else:
            shared_with = self.shared_with


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if title is not UNSET:
            field_dict["title"] = title
        if client_name is not UNSET:
            field_dict["client_name"] = client_name
        if comment is not UNSET:
            field_dict["comment"] = comment
        if instruction_set_id is not UNSET:
            field_dict["instruction_set_id"] = instruction_set_id
        if folders is not UNSET:
            field_dict["folders"] = folders
        if shared_with is not UNSET:
            field_dict["shared_with"] = shared_with

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title", UNSET)

        def _parse_client_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        client_name = _parse_client_name(d.pop("client_name", UNSET))


        def _parse_comment(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        comment = _parse_comment(d.pop("comment", UNSET))


        instruction_set_id = d.pop("instruction_set_id", UNSET)

        folders = cast(list[str], d.pop("folders", UNSET))


        def _parse_shared_with(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                shared_with_type_0 = cast(list[str], data)

                return shared_with_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        shared_with = _parse_shared_with(d.pop("shared_with", UNSET))


        dictation_update_body = cls(
            title=title,
            client_name=client_name,
            comment=comment,
            instruction_set_id=instruction_set_id,
            folders=folders,
            shared_with=shared_with,
        )


        dictation_update_body.additional_properties = d
        return dictation_update_body

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
