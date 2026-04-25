from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="DictationShareResourceEmailsItem")



@_attrs_define
class DictationShareResourceEmailsItem:
    """ 
        Attributes:
            id (str):  Example: aid-xyz12345.
            recipient_email (str):
            sent_at (str):
     """

    id: str
    recipient_email: str
    sent_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        recipient_email = self.recipient_email

        sent_at = self.sent_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "recipient_email": recipient_email,
            "sent_at": sent_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        recipient_email = d.pop("recipient_email")

        sent_at = d.pop("sent_at")

        dictation_share_resource_emails_item = cls(
            id=id,
            recipient_email=recipient_email,
            sent_at=sent_at,
        )


        dictation_share_resource_emails_item.additional_properties = d
        return dictation_share_resource_emails_item

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
