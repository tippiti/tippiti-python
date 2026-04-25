from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="AffiliateRequestPayoutBody")



@_attrs_define
class AffiliateRequestPayoutBody:
    """ 
        Attributes:
            bank_holder (str):
            bank_iban (str):
            bank_bic (None | str | Unset):
     """

    bank_holder: str
    bank_iban: str
    bank_bic: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        bank_holder = self.bank_holder

        bank_iban = self.bank_iban

        bank_bic: None | str | Unset
        if isinstance(self.bank_bic, Unset):
            bank_bic = UNSET
        else:
            bank_bic = self.bank_bic


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "bank_holder": bank_holder,
            "bank_iban": bank_iban,
        })
        if bank_bic is not UNSET:
            field_dict["bank_bic"] = bank_bic

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        bank_holder = d.pop("bank_holder")

        bank_iban = d.pop("bank_iban")

        def _parse_bank_bic(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        bank_bic = _parse_bank_bic(d.pop("bank_bic", UNSET))


        affiliate_request_payout_body = cls(
            bank_holder=bank_holder,
            bank_iban=bank_iban,
            bank_bic=bank_bic,
        )


        affiliate_request_payout_body.additional_properties = d
        return affiliate_request_payout_body

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
