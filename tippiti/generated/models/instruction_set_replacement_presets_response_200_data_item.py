from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="InstructionSetReplacementPresetsResponse200DataItem")



@_attrs_define
class InstructionSetReplacementPresetsResponse200DataItem:
    """ 
        Attributes:
            id (int):
            search (str):
            replace (str):
            case_insensitive (bool):
            default_active (bool):
     """

    id: int
    search: str
    replace: str
    case_insensitive: bool
    default_active: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        search = self.search

        replace = self.replace

        case_insensitive = self.case_insensitive

        default_active = self.default_active


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "search": search,
            "replace": replace,
            "case_insensitive": case_insensitive,
            "default_active": default_active,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        search = d.pop("search")

        replace = d.pop("replace")

        case_insensitive = d.pop("case_insensitive")

        default_active = d.pop("default_active")

        instruction_set_replacement_presets_response_200_data_item = cls(
            id=id,
            search=search,
            replace=replace,
            case_insensitive=case_insensitive,
            default_active=default_active,
        )


        instruction_set_replacement_presets_response_200_data_item.additional_properties = d
        return instruction_set_replacement_presets_response_200_data_item

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
