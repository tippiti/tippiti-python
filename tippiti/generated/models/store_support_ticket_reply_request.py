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






T = TypeVar("T", bound="StoreSupportTicketReplyRequest")



@_attrs_define
class StoreSupportTicketReplyRequest:
    """ 
        Attributes:
            content (str):
            attachments (list[File] | None | Unset):
     """

    content: str
    attachments: list[File] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        content = self.content

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
            "content": content,
        })
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict


    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("content", (None, str(self.content).encode(), "text/plain")))



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
        content = d.pop("content")

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


        store_support_ticket_reply_request = cls(
            content=content,
            attachments=attachments,
        )


        store_support_ticket_reply_request.additional_properties = d
        return store_support_ticket_reply_request

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
