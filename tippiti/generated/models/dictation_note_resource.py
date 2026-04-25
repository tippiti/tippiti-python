from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dictation_note_attachment_resource import DictationNoteAttachmentResource





T = TypeVar("T", bound="DictationNoteResource")



@_attrs_define
class DictationNoteResource:
    """ 
        Attributes:
            id (str):  Example: aid-xyz12345.
            dictation_id (str):  Example: aid-xyz12345.
            user_id (str):  Example: aid-xyz12345.
            content (str):
            is_important (bool):
            show_on_top (bool):
            created_at (str):
            updated_at (str):
            user_name (str | Unset):
            attachments (list[DictationNoteAttachmentResource] | Unset):
            can_edit (str | Unset):
            can_delete (str | Unset):
     """

    id: str
    dictation_id: str
    user_id: str
    content: str
    is_important: bool
    show_on_top: bool
    created_at: str
    updated_at: str
    user_name: str | Unset = UNSET
    attachments: list[DictationNoteAttachmentResource] | Unset = UNSET
    can_edit: str | Unset = UNSET
    can_delete: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dictation_note_attachment_resource import DictationNoteAttachmentResource
        id = self.id

        dictation_id = self.dictation_id

        user_id = self.user_id

        content = self.content

        is_important = self.is_important

        show_on_top = self.show_on_top

        created_at = self.created_at

        updated_at = self.updated_at

        user_name = self.user_name

        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)



        can_edit = self.can_edit

        can_delete = self.can_delete


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "dictation_id": dictation_id,
            "user_id": user_id,
            "content": content,
            "is_important": is_important,
            "show_on_top": show_on_top,
            "created_at": created_at,
            "updated_at": updated_at,
        })
        if user_name is not UNSET:
            field_dict["user_name"] = user_name
        if attachments is not UNSET:
            field_dict["attachments"] = attachments
        if can_edit is not UNSET:
            field_dict["can_edit"] = can_edit
        if can_delete is not UNSET:
            field_dict["can_delete"] = can_delete

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dictation_note_attachment_resource import DictationNoteAttachmentResource
        d = dict(src_dict)
        id = d.pop("id")

        dictation_id = d.pop("dictation_id")

        user_id = d.pop("user_id")

        content = d.pop("content")

        is_important = d.pop("is_important")

        show_on_top = d.pop("show_on_top")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        user_name = d.pop("user_name", UNSET)

        _attachments = d.pop("attachments", UNSET)
        attachments: list[DictationNoteAttachmentResource] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = DictationNoteAttachmentResource.from_dict(attachments_item_data)



                attachments.append(attachments_item)


        can_edit = d.pop("can_edit", UNSET)

        can_delete = d.pop("can_delete", UNSET)

        dictation_note_resource = cls(
            id=id,
            dictation_id=dictation_id,
            user_id=user_id,
            content=content,
            is_important=is_important,
            show_on_top=show_on_top,
            created_at=created_at,
            updated_at=updated_at,
            user_name=user_name,
            attachments=attachments,
            can_edit=can_edit,
            can_delete=can_delete,
        )


        dictation_note_resource.additional_properties = d
        return dictation_note_resource

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
