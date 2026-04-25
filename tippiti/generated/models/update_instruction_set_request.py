from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_instruction_set_request_instructions_type_0_item import UpdateInstructionSetRequestInstructionsType0Item
  from ..models.update_instruction_set_request_replacements_type_0_item import UpdateInstructionSetRequestReplacementsType0Item





T = TypeVar("T", bound="UpdateInstructionSetRequest")



@_attrs_define
class UpdateInstructionSetRequest:
    """ 
        Attributes:
            name (str):
            description (None | str | Unset):
            instructions (list[UpdateInstructionSetRequestInstructionsType0Item] | None | Unset):
            replacements (list[UpdateInstructionSetRequestReplacementsType0Item] | None | Unset):
     """

    name: str
    description: None | str | Unset = UNSET
    instructions: list[UpdateInstructionSetRequestInstructionsType0Item] | None | Unset = UNSET
    replacements: list[UpdateInstructionSetRequestReplacementsType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_instruction_set_request_instructions_type_0_item import UpdateInstructionSetRequestInstructionsType0Item
        from ..models.update_instruction_set_request_replacements_type_0_item import UpdateInstructionSetRequestReplacementsType0Item
        name = self.name

        description: None | str | Unset
        if isinstance(self.description, Unset):
            description = UNSET
        else:
            description = self.description

        instructions: list[dict[str, Any]] | None | Unset
        if isinstance(self.instructions, Unset):
            instructions = UNSET
        elif isinstance(self.instructions, list):
            instructions = []
            for instructions_type_0_item_data in self.instructions:
                instructions_type_0_item = instructions_type_0_item_data.to_dict()
                instructions.append(instructions_type_0_item)


        else:
            instructions = self.instructions

        replacements: list[dict[str, Any]] | None | Unset
        if isinstance(self.replacements, Unset):
            replacements = UNSET
        elif isinstance(self.replacements, list):
            replacements = []
            for replacements_type_0_item_data in self.replacements:
                replacements_type_0_item = replacements_type_0_item_data.to_dict()
                replacements.append(replacements_type_0_item)


        else:
            replacements = self.replacements


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "name": name,
        })
        if description is not UNSET:
            field_dict["description"] = description
        if instructions is not UNSET:
            field_dict["instructions"] = instructions
        if replacements is not UNSET:
            field_dict["replacements"] = replacements

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_instruction_set_request_instructions_type_0_item import UpdateInstructionSetRequestInstructionsType0Item
        from ..models.update_instruction_set_request_replacements_type_0_item import UpdateInstructionSetRequestReplacementsType0Item
        d = dict(src_dict)
        name = d.pop("name")

        def _parse_description(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        description = _parse_description(d.pop("description", UNSET))


        def _parse_instructions(data: object) -> list[UpdateInstructionSetRequestInstructionsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                instructions_type_0 = []
                _instructions_type_0 = data
                for instructions_type_0_item_data in (_instructions_type_0):
                    instructions_type_0_item = UpdateInstructionSetRequestInstructionsType0Item.from_dict(instructions_type_0_item_data)



                    instructions_type_0.append(instructions_type_0_item)

                return instructions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UpdateInstructionSetRequestInstructionsType0Item] | None | Unset, data)

        instructions = _parse_instructions(d.pop("instructions", UNSET))


        def _parse_replacements(data: object) -> list[UpdateInstructionSetRequestReplacementsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                replacements_type_0 = []
                _replacements_type_0 = data
                for replacements_type_0_item_data in (_replacements_type_0):
                    replacements_type_0_item = UpdateInstructionSetRequestReplacementsType0Item.from_dict(replacements_type_0_item_data)



                    replacements_type_0.append(replacements_type_0_item)

                return replacements_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[UpdateInstructionSetRequestReplacementsType0Item] | None | Unset, data)

        replacements = _parse_replacements(d.pop("replacements", UNSET))


        update_instruction_set_request = cls(
            name=name,
            description=description,
            instructions=instructions,
            replacements=replacements,
        )


        update_instruction_set_request.additional_properties = d
        return update_instruction_set_request

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
