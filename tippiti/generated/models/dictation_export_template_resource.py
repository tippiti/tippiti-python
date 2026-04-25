from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="DictationExportTemplateResource")



@_attrs_define
class DictationExportTemplateResource:
    """ 
        Attributes:
            id (str):  Example: aid-xyz12345.
            name (str):
            original_filename (str):
            file_size (int):
            is_shared_with_subusers (bool):
            is_owner (str):
            folder_ids (list[str]):
            created_at (str):
     """

    id: str
    name: str
    original_filename: str
    file_size: int
    is_shared_with_subusers: bool
    is_owner: str
    folder_ids: list[str]
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        original_filename = self.original_filename

        file_size = self.file_size

        is_shared_with_subusers = self.is_shared_with_subusers

        is_owner = self.is_owner

        folder_ids = self.folder_ids



        created_at = self.created_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "original_filename": original_filename,
            "file_size": file_size,
            "is_shared_with_subusers": is_shared_with_subusers,
            "is_owner": is_owner,
            "folder_ids": folder_ids,
            "created_at": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        original_filename = d.pop("original_filename")

        file_size = d.pop("file_size")

        is_shared_with_subusers = d.pop("is_shared_with_subusers")

        is_owner = d.pop("is_owner")

        folder_ids = cast(list[str], d.pop("folder_ids"))


        created_at = d.pop("created_at")

        dictation_export_template_resource = cls(
            id=id,
            name=name,
            original_filename=original_filename,
            file_size=file_size,
            is_shared_with_subusers=is_shared_with_subusers,
            is_owner=is_owner,
            folder_ids=folder_ids,
            created_at=created_at,
        )


        dictation_export_template_resource.additional_properties = d
        return dictation_export_template_resource

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
