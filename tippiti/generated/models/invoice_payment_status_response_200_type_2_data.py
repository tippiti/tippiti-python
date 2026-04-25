from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Literal, cast






T = TypeVar("T", bound="InvoicePaymentStatusResponse200Type2Data")



@_attrs_define
class InvoicePaymentStatusResponse200Type2Data:
    """ 
        Attributes:
            status (Literal['succeeded']):
     """

    status: Literal['succeeded']
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        status = self.status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "status": status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        status = cast(Literal['succeeded'] , d.pop("status"))
        if status != 'succeeded':
            raise ValueError(f"status must match const 'succeeded', got '{status}'")

        invoice_payment_status_response_200_type_2_data = cls(
            status=status,
        )


        invoice_payment_status_response_200_type_2_data.additional_properties = d
        return invoice_payment_status_response_200_type_2_data

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
