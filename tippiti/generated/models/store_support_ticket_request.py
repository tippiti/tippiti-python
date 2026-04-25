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






T = TypeVar("T", bound="StoreSupportTicketRequest")



@_attrs_define
class StoreSupportTicketRequest:
    """ 
        Attributes:
            title (str):
            department_id (str):  Example: aid-xyz12345.
            content (str):
            priority_id (str):  Example: aid-xyz12345.
            dictation_id (str | Unset):  Example: aid-xyz12345.
            attachments (list[File] | None | Unset):
     """

    title: str
    department_id: str
    content: str
    priority_id: str
    dictation_id: str | Unset = UNSET
    attachments: list[File] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        title = self.title

        department_id = self.department_id

        content = self.content

        priority_id = self.priority_id

        dictation_id = self.dictation_id

        attachments: list[FileTypes] | None | Unset
        if isinstance(self.attachments, Unset):
            attachments = UNSET
        elif isinstance(self.attachments, list):
            attachments = []
            for attachments_type_0_item_data in self.attachments:
                attachments_type_0_item = attachments_type_0_item_data.to_tuple()

                attachments.append(attachments_type_0_item)


        else:
            attachments = self.attachments


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "title": title,
            "department_id": department_id,
            "content": content,
            "priority_id": priority_id,
        })
        if dictation_id is not UNSET:
            field_dict["dictation_id"] = dictation_id
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("title", (None, str(self.title).encode(), "text/plain")))



        files.append(("department_id", (None, str(self.department_id).encode(), "text/plain")))



        files.append(("content", (None, str(self.content).encode(), "text/plain")))



        files.append(("priority_id", (None, str(self.priority_id).encode(), "text/plain")))



        if not isinstance(self.dictation_id, Unset):
            files.append(("dictation_id", (None, str(self.dictation_id).encode(), "text/plain")))



        if not isinstance(self.attachments, Unset):
            if isinstance(self.attachments, list):

                for attachments_type_0_item_element in self.attachments:
                    files.append(("attachments", attachments_type_0_item_element.to_tuple()))
            else:
                files.append(("attachments", (None, str(self.attachments).encode(), "text/plain")))



        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))



        return files


    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        title = d.pop("title")

        department_id = d.pop("department_id")

        content = d.pop("content")

        priority_id = d.pop("priority_id")

        dictation_id = d.pop("dictation_id", UNSET)

        def _parse_attachments(data: object) -> list[File] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                attachments_type_0 = []
                _attachments_type_0 = data
                for attachments_type_0_item_data in (_attachments_type_0):
                    attachments_type_0_item = File(
                         payload = BytesIO(attachments_type_0_item_data)
                    )



                    attachments_type_0.append(attachments_type_0_item)

                return attachments_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[File] | None | Unset, data)

        attachments = _parse_attachments(d.pop("attachments", UNSET))


        store_support_ticket_request = cls(
            title=title,
            department_id=department_id,
            content=content,
            priority_id=priority_id,
            dictation_id=dictation_id,
            attachments=attachments,
        )


        store_support_ticket_request.additional_properties = d
        return store_support_ticket_request

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
