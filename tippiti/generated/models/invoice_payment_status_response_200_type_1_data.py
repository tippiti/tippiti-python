from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Literal, cast






T = TypeVar("T", bound="InvoicePaymentStatusResponse200Type1Data")



@_attrs_define
class InvoicePaymentStatusResponse200Type1Data:
    """ 
        Attributes:
            status (Literal['failed']):
            message (str):
     """

    status: Literal['failed']
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        status = self.status

        message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
            "message": message,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = cast(Literal['failed'] , d.pop("status"))
        if status != 'failed':
            raise ValueError(f"status must match const 'failed', got '{status}'")

        message = d.pop("message")

        invoice_payment_status_response_200_type_1_data = cls(
            status=status,
            message=message,
        )


        invoice_payment_status_response_200_type_1_data.additional_properties = d
        return invoice_payment_status_response_200_type_1_data

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
