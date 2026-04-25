from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field
import json
from .. import types

from ..types import UNSET, Unset

from ..types import File, FileTypes
from ..types import UNSET, Unset
from io import BytesIO
from typing import cast






T = TypeVar("T", bound="DictationStoreBody")



@_attrs_define
class DictationStoreBody:
    """ 
        Attributes:
            title (str):
            file (File):
            client_name (None | str | Unset):
            comment (None | str | Unset):
            instruction_set_id (str | Unset):  Example: aid-xyz12345.
            folders (list[str] | Unset):
            shared_with (list[str] | None | Unset):
     """

    title: str
    file: File
    client_name: None | str | Unset = UNSET
    comment: None | str | Unset = UNSET
    instruction_set_id: str | Unset = UNSET
    folders: list[str] | Unset = UNSET
    shared_with: list[str] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        title = self.title

        file = self.file.to_tuple()


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
            "title": title,
            "file": file,
        })
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


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("title", (None, str(self.title).encode(), "text/plain")))



        files.append(("file", self.file.to_tuple()))



        if not isinstance(self.client_name, Unset):
            if isinstance(self.client_name, str):

                files.append(("client_name", (None, str(self.client_name).encode(), "text/plain")))
            else:
                files.append(("client_name", (None, str(self.client_name).encode(), "text/plain")))


        if not isinstance(self.comment, Unset):
            if isinstance(self.comment, str):

                files.append(("comment", (None, str(self.comment).encode(), "text/plain")))
            else:
                files.append(("comment", (None, str(self.comment).encode(), "text/plain")))


        if not isinstance(self.instruction_set_id, Unset):
            files.append(("instruction_set_id", (None, str(self.instruction_set_id).encode(), "text/plain")))



        if not isinstance(self.folders, Unset):
            for folders_item_element in self.folders:
                files.append(("folders", (None, str(folders_item_element).encode(), "text/plain")))




        if not isinstance(self.shared_with, Unset):
            if isinstance(self.shared_with, list):

                for shared_with_type_0_item_element in self.shared_with:
                    files.append(("shared_with", (None, str(shared_with_type_0_item_element).encode(), "text/plain")))
            else:
                files.append(("shared_with", (None, str(self.shared_with).encode(), "text/plain")))



        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        file = File(
             payload = BytesIO(d.pop("file"))
        )




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


        dictation_store_body = cls(
            title=title,
            file=file,
            client_name=client_name,
            comment=comment,
            instruction_set_id=instruction_set_id,
            folders=folders,
            shared_with=shared_with,
        )


        dictation_store_body.additional_properties = d
        return dictation_store_body

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
