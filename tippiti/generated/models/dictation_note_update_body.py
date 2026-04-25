from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DictationNoteUpdateBody")



@_attrs_define
class DictationNoteUpdateBody:
    """ 
        Attributes:
            content (str | Unset):
            is_important (bool | Unset):
            show_on_top (bool | Unset):
     """

    content: str | Unset = UNSET
    is_important: bool | Unset = UNSET
    show_on_top: bool | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        content = self.content

        is_important = self.is_important

        show_on_top = self.show_on_top


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if content is not UNSET:
            field_dict["content"] = content
        if is_important is not UNSET:
            field_dict["is_important"] = is_important
        if show_on_top is not UNSET:
            field_dict["show_on_top"] = show_on_top

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        content = d.pop("content", UNSET)

        is_important = d.pop("is_important", UNSET)

        show_on_top = d.pop("show_on_top", UNSET)

        dictation_note_update_body = cls(
            content=content,
            is_important=is_important,
            show_on_top=show_on_top,
        )


        dictation_note_update_body.additional_properties = d
        return dictation_note_update_body

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
