from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="InvoiceValidateVatResponse200Type0Data")



@_attrs_define
class InvoiceValidateVatResponse200Type0Data:
    """ 
        Attributes:
            has_tax_id (bool):
            valid (bool):
            bypassed (bool):
     """

    has_tax_id: bool
    valid: bool
    bypassed: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        has_tax_id = self.has_tax_id

        valid = self.valid

        bypassed = self.bypassed


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "has_tax_id": has_tax_id,
            "valid": valid,
            "bypassed": bypassed,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_tax_id = d.pop("has_tax_id")

        valid = d.pop("valid")

        bypassed = d.pop("bypassed")

        invoice_validate_vat_response_200_type_0_data = cls(
            has_tax_id=has_tax_id,
            valid=valid,
            bypassed=bypassed,
        )


        invoice_validate_vat_response_200_type_0_data.additional_properties = d
        return invoice_validate_vat_response_200_type_0_data

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
