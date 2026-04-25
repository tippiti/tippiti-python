from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.permission_index_response_200_data_definitions_item import PermissionIndexResponse200DataDefinitionsItem





T = TypeVar("T", bound="PermissionIndexResponse200Data")



@_attrs_define
class PermissionIndexResponse200Data:
    """ 
        Attributes:
            definitions (list[PermissionIndexResponse200DataDefinitionsItem]):
     """

    definitions: list[PermissionIndexResponse200DataDefinitionsItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.permission_index_response_200_data_definitions_item import PermissionIndexResponse200DataDefinitionsItem
        definitions = []
        for definitions_item_data in self.definitions:
            definitions_item = definitions_item_data.to_dict()
            definitions.append(definitions_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "definitions": definitions,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.permission_index_response_200_data_definitions_item import PermissionIndexResponse200DataDefinitionsItem
        d = dict(src_dict)
        definitions = []
        _definitions = d.pop("definitions")
        for definitions_item_data in (_definitions):
            definitions_item = PermissionIndexResponse200DataDefinitionsItem.from_dict(definitions_item_data)



            definitions.append(definitions_item)


        permission_index_response_200_data = cls(
            definitions=definitions,
        )


        permission_index_response_200_data.additional_properties = d
        return permission_index_response_200_data

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
