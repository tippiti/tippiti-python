from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="DictationStatsResponse200Data")



@_attrs_define
class DictationStatsResponse200Data:
    """ 
        Attributes:
            total_dictations (str):
            completed_dictations (str):
            total_characters (str):
            credit_balance (int):
     """

    total_dictations: str
    completed_dictations: str
    total_characters: str
    credit_balance: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        total_dictations = self.total_dictations

        completed_dictations = self.completed_dictations

        total_characters = self.total_characters

        credit_balance = self.credit_balance


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "total_dictations": total_dictations,
            "completed_dictations": completed_dictations,
            "total_characters": total_characters,
            "credit_balance": credit_balance,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_dictations = d.pop("total_dictations")

        completed_dictations = d.pop("completed_dictations")

        total_characters = d.pop("total_characters")

        credit_balance = d.pop("credit_balance")

        dictation_stats_response_200_data = cls(
            total_dictations=total_dictations,
            completed_dictations=completed_dictations,
            total_characters=total_characters,
            credit_balance=credit_balance,
        )


        dictation_stats_response_200_data.additional_properties = d
        return dictation_stats_response_200_data

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
