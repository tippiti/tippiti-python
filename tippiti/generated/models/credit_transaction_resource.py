from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="CreditTransactionResource")



@_attrs_define
class CreditTransactionResource:
    """ 
        Attributes:
            id (str):  Example: aid-xyz12345.
            type_ (str):
            amount (int):
            balance_before (int):
            balance_after (int):
            description (None | str):
            metadata (str):
            created_at (str):
     """

    id: str
    type_: str
    amount: int
    balance_before: int
    balance_after: int
    description: None | str
    metadata: str
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        type_ = self.type_

        amount = self.amount

        balance_before = self.balance_before

        balance_after = self.balance_after

        description: None | str
        description = self.description

        metadata = self.metadata

        created_at = self.created_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "type": type_,
            "amount": amount,
            "balance_before": balance_before,
            "balance_after": balance_after,
            "description": description,
            "metadata": metadata,
            "created_at": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        type_ = d.pop("type")

        amount = d.pop("amount")

        balance_before = d.pop("balance_before")

        balance_after = d.pop("balance_after")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))


        metadata = d.pop("metadata")

        created_at = d.pop("created_at")

        credit_transaction_resource = cls(
            id=id,
            type_=type_,
            amount=amount,
            balance_before=balance_before,
            balance_after=balance_after,
            description=description,
            metadata=metadata,
            created_at=created_at,
        )


        credit_transaction_resource.additional_properties = d
        return credit_transaction_resource

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
