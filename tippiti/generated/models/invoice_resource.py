from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="InvoiceResource")



@_attrs_define
class InvoiceResource:
    """ 
        Attributes:
            id (str):  Example: aid-xyz12345.
            invoice_number (str):
            type_ (str):
            status (str):
            subtotal (float):
            tax_rate (float):
            tax_amount (float):
            total (float):
            currency (str):
            paid_at (str):
            period_start (str):
            period_end (str):
            created_at (str):
     """

    id: str
    invoice_number: str
    type_: str
    status: str
    subtotal: float
    tax_rate: float
    tax_amount: float
    total: float
    currency: str
    paid_at: str
    period_start: str
    period_end: str
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        invoice_number = self.invoice_number

        type_ = self.type_

        status = self.status

        subtotal = self.subtotal

        tax_rate = self.tax_rate

        tax_amount = self.tax_amount

        total = self.total

        currency = self.currency

        paid_at = self.paid_at

        period_start = self.period_start

        period_end = self.period_end

        created_at = self.created_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "invoice_number": invoice_number,
            "type": type_,
            "status": status,
            "subtotal": subtotal,
            "tax_rate": tax_rate,
            "tax_amount": tax_amount,
            "total": total,
            "currency": currency,
            "paid_at": paid_at,
            "period_start": period_start,
            "period_end": period_end,
            "created_at": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        invoice_number = d.pop("invoice_number")

        type_ = d.pop("type")

        status = d.pop("status")

        subtotal = d.pop("subtotal")

        tax_rate = d.pop("tax_rate")

        tax_amount = d.pop("tax_amount")

        total = d.pop("total")

        currency = d.pop("currency")

        paid_at = d.pop("paid_at")

        period_start = d.pop("period_start")

        period_end = d.pop("period_end")

        created_at = d.pop("created_at")

        invoice_resource = cls(
            id=id,
            invoice_number=invoice_number,
            type_=type_,
            status=status,
            subtotal=subtotal,
            tax_rate=tax_rate,
            tax_amount=tax_amount,
            total=total,
            currency=currency,
            paid_at=paid_at,
            period_start=period_start,
            period_end=period_end,
            created_at=created_at,
        )


        invoice_resource.additional_properties = d
        return invoice_resource

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
