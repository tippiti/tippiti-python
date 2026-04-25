from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Literal, cast






T = TypeVar("T", bound="DictationChatSendResponse403Type1")



@_attrs_define
class DictationChatSendResponse403Type1:
    """ 
        Attributes:
            success (bool):
            message (Literal['Keine Berechtigung.']):
     """

    success: bool
    message: Literal['Keine Berechtigung.']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        success = self.success

        message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "success": success,
            "message": message,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        success = d.pop("success")

        message = cast(Literal['Keine Berechtigung.'] , d.pop("message"))
        if message != 'Keine Berechtigung.':
            raise ValueError(f"message must match const 'Keine Berechtigung.', got '{message}'")

        dictation_chat_send_response_403_type_1 = cls(
            success=success,
            message=message,
        )


        dictation_chat_send_response_403_type_1.additional_properties = d
        return dictation_chat_send_response_403_type_1

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
