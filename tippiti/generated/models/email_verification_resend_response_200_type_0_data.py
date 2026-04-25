from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Literal, cast






T = TypeVar("T", bound="EmailVerificationResendResponse200Type0Data")



@_attrs_define
class EmailVerificationResendResponse200Type0Data:
    """ 
        Attributes:
            message (Literal['Verifizierungs-E-Mail wurde gesendet.']):
     """

    message: Literal['Verifizierungs-E-Mail wurde gesendet.']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "message": message,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        message = cast(Literal['Verifizierungs-E-Mail wurde gesendet.'] , d.pop("message"))
        if message != 'Verifizierungs-E-Mail wurde gesendet.':
            raise ValueError(f"message must match const 'Verifizierungs-E-Mail wurde gesendet.', got '{message}'")

        email_verification_resend_response_200_type_0_data = cls(
            message=message,
        )


        email_verification_resend_response_200_type_0_data.additional_properties = d
        return email_verification_resend_response_200_type_0_data

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
