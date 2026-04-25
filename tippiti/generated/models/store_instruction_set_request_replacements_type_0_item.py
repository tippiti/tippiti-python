from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="StoreInstructionSetRequestReplacementsType0Item")



@_attrs_define
class StoreInstructionSetRequestReplacementsType0Item:
    """ 
        Attributes:
            search (str | Unset):
            replace (str | Unset):
            case_insensitive (bool | Unset):
            is_active (bool | Unset):
            is_preset (bool | Unset):
            replacement_preset_id (str | Unset):  Example: aid-xyz12345.
     """

    search: str | Unset = UNSET
    replace: str | Unset = UNSET
    case_insensitive: bool | Unset = UNSET
    is_active: bool | Unset = UNSET
    is_preset: bool | Unset = UNSET
    replacement_preset_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        search = self.search

        replace = self.replace

        case_insensitive = self.case_insensitive

        is_active = self.is_active

        is_preset = self.is_preset

        replacement_preset_id = self.replacement_preset_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if search is not UNSET:
            field_dict["search"] = search
        if replace is not UNSET:
            field_dict["replace"] = replace
        if case_insensitive is not UNSET:
            field_dict["case_insensitive"] = case_insensitive
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_preset is not UNSET:
            field_dict["is_preset"] = is_preset
        if replacement_preset_id is not UNSET:
            field_dict["replacement_preset_id"] = replacement_preset_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        search = d.pop("search", UNSET)

        replace = d.pop("replace", UNSET)

        case_insensitive = d.pop("case_insensitive", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_preset = d.pop("is_preset", UNSET)

        replacement_preset_id = d.pop("replacement_preset_id", UNSET)

        store_instruction_set_request_replacements_type_0_item = cls(
            search=search,
            replace=replace,
            case_insensitive=case_insensitive,
            is_active=is_active,
            is_preset=is_preset,
            replacement_preset_id=replacement_preset_id,
        )


        store_instruction_set_request_replacements_type_0_item.additional_properties = d
        return store_instruction_set_request_replacements_type_0_item

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
