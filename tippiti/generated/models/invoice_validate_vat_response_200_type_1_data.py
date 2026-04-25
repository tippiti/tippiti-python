from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="InvoiceValidateVatResponse200Type1Data")



@_attrs_define
class InvoiceValidateVatResponse200Type1Data:
    """ 
        Attributes:
            has_tax_id (bool):
            valid (bool):
            tax_id_removed (bool):
            removed_tax_id (None | str):
            message (str):
            tax_rate (str):
            tax_status (str):
     """

    has_tax_id: bool
    valid: bool
    tax_id_removed: bool
    removed_tax_id: None | str
    message: str
    tax_rate: str
    tax_status: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        has_tax_id = self.has_tax_id

        valid = self.valid

        tax_id_removed = self.tax_id_removed

        removed_tax_id: None | str
        removed_tax_id = self.removed_tax_id

        message = self.message

        tax_rate = self.tax_rate

        tax_status = self.tax_status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "has_tax_id": has_tax_id,
            "valid": valid,
            "tax_id_removed": tax_id_removed,
            "removed_tax_id": removed_tax_id,
            "message": message,
            "tax_rate": tax_rate,
            "tax_status": tax_status,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        has_tax_id = d.pop("has_tax_id")

        valid = d.pop("valid")

        tax_id_removed = d.pop("tax_id_removed")

        def _parse_removed_tax_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        removed_tax_id = _parse_removed_tax_id(d.pop("removed_tax_id"))


        message = d.pop("message")

        tax_rate = d.pop("tax_rate")

        tax_status = d.pop("tax_status")

        invoice_validate_vat_response_200_type_1_data = cls(
            has_tax_id=has_tax_id,
            valid=valid,
            tax_id_removed=tax_id_removed,
            removed_tax_id=removed_tax_id,
            message=message,
            tax_rate=tax_rate,
            tax_status=tax_status,
        )


        invoice_validate_vat_response_200_type_1_data.additional_properties = d
        return invoice_validate_vat_response_200_type_1_data

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
