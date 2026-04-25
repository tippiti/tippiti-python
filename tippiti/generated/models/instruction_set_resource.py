from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.instruction_set_resource_instructions_item import InstructionSetResourceInstructionsItem
  from ..models.instruction_set_resource_replacements_item import InstructionSetResourceReplacementsItem





T = TypeVar("T", bound="InstructionSetResource")



@_attrs_define
class InstructionSetResource:
    """ 
        Attributes:
            id (str):  Example: aid-xyz12345.
            name (str):
            description (None | str):
            is_default (bool):
            created_at (str):
            instructions (list[InstructionSetResourceInstructionsItem] | Unset):
            replacements (list[InstructionSetResourceReplacementsItem] | Unset):
     """

    id: str
    name: str
    description: None | str
    is_default: bool
    created_at: str
    instructions: list[InstructionSetResourceInstructionsItem] | Unset = UNSET
    replacements: list[InstructionSetResourceReplacementsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.instruction_set_resource_instructions_item import InstructionSetResourceInstructionsItem
        from ..models.instruction_set_resource_replacements_item import InstructionSetResourceReplacementsItem
        id = self.id

        name = self.name

        description: None | str
        description = self.description

        is_default = self.is_default

        created_at = self.created_at

        instructions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.instructions, Unset):
            instructions = []
            for instructions_item_data in self.instructions:
                instructions_item = instructions_item_data.to_dict()
                instructions.append(instructions_item)



        replacements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.replacements, Unset):
            replacements = []
            for replacements_item_data in self.replacements:
                replacements_item = replacements_item_data.to_dict()
                replacements.append(replacements_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "description": description,
            "is_default": is_default,
            "created_at": created_at,
        })
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if replacements is not UNSET:
            field_dict["replacements"] = replacements

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.instruction_set_resource_instructions_item import InstructionSetResourceInstructionsItem
        from ..models.instruction_set_resource_replacements_item import InstructionSetResourceReplacementsItem
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))


        is_default = d.pop("is_default")

        created_at = d.pop("created_at")

        _instructions = d.pop("instructions", UNSET)
        instructions: list[InstructionSetResourceInstructionsItem] | Unset = UNSET
        if _instructions is not UNSET:
            instructions = []
            for instructions_item_data in _instructions:
                instructions_item = InstructionSetResourceInstructionsItem.from_dict(instructions_item_data)



                instructions.append(instructions_item)


        _replacements = d.pop("replacements", UNSET)
        replacements: list[InstructionSetResourceReplacementsItem] | Unset = UNSET
        if _replacements is not UNSET:
            replacements = []
            for replacements_item_data in _replacements:
                replacements_item = InstructionSetResourceReplacementsItem.from_dict(replacements_item_data)



                replacements.append(replacements_item)


        instruction_set_resource = cls(
            id=id,
            name=name,
            description=description,
            is_default=is_default,
            created_at=created_at,
            instructions=instructions,
            replacements=replacements,
        )


        instruction_set_resource.additional_properties = d
        return instruction_set_resource

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
