from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="DictationShareSendEmailBody")



@_attrs_define
class DictationShareSendEmailBody:
    """ 
        Attributes:
            recipient_emails (list[str]):
            message (None | str | Unset):
            include_password (bool | Unset):
            password (None | str | Unset):
     """

    recipient_emails: list[str]
    message: None | str | Unset = UNSET
    include_password: bool | Unset = UNSET
    password: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        recipient_emails = self.recipient_emails



        message: None | str | Unset
        if isinstance(self.message, Unset):
            message = UNSET
        else:
            message = self.message

        include_password = self.include_password

        password: None | str | Unset
        if isinstance(self.password, Unset):
            password = UNSET
        else:
            password = self.password


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "recipient_emails": recipient_emails,
        })
        if message is not UNSET:
            field_dict["message"] = message
        if include_password is not UNSET:
            field_dict["include_password"] = include_password
        if password is not UNSET:
            field_dict["password"] = password

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        recipient_emails = cast(list[str], d.pop("recipient_emails"))


        def _parse_message(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        message = _parse_message(d.pop("message", UNSET))


        include_password = d.pop("include_password", UNSET)

        def _parse_password(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        password = _parse_password(d.pop("password", UNSET))


        dictation_share_send_email_body = cls(
            recipient_emails=recipient_emails,
            message=message,
            include_password=include_password,
            password=password,
        )


        dictation_share_send_email_body.additional_properties = d
        return dictation_share_send_email_body

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
