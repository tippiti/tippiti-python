from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="SupportTicketAttachmentResource")



@_attrs_define
class SupportTicketAttachmentResource:
    """ 
        Attributes:
            id (str):  Example: aid-xyz12345.
            original_filename (str):
            file_size (int):
            created_at (str):
     """

    id: str
    original_filename: str
    file_size: int
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        original_filename = self.original_filename

        file_size = self.file_size

        created_at = self.created_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "original_filename": original_filename,
            "file_size": file_size,
            "created_at": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        original_filename = d.pop("original_filename")

        file_size = d.pop("file_size")

        created_at = d.pop("created_at")

        support_ticket_attachment_resource = cls(
            id=id,
            original_filename=original_filename,
            file_size=file_size,
            created_at=created_at,
        )


        support_ticket_attachment_resource.additional_properties = d
        return support_ticket_attachment_resource

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
