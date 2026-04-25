from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="PermissionIndexResponse200DataDefinitionsItem")



@_attrs_define
class PermissionIndexResponse200DataDefinitionsItem:
    """ 
        Attributes:
            keys (list[Any]):
            label (str):
            description (None | str):
            group (None | str):
            type_ (str):
            default (bool):
            configurable_by (str):
     """

    keys: list[Any]
    label: str
    description: None | str
    group: None | str
    type_: str
    default: bool
    configurable_by: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        keys = self.keys



        label = self.label

        description: None | str
        description = self.description

        group: None | str
        group = self.group

        type_ = self.type_

        default = self.default

        configurable_by = self.configurable_by


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "keys": keys,
            "label": label,
            "description": description,
            "group": group,
            "type": type_,
            "default": default,
            "configurable_by": configurable_by,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        keys = cast(list[Any], d.pop("keys"))


        label = d.pop("label")

        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))


        def _parse_group(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        group = _parse_group(d.pop("group"))


        type_ = d.pop("type")

        default = d.pop("default")

        configurable_by = d.pop("configurable_by")

        permission_index_response_200_data_definitions_item = cls(
            keys=keys,
            label=label,
            description=description,
            group=group,
            type_=type_,
            default=default,
            configurable_by=configurable_by,
        )


        permission_index_response_200_data_definitions_item.additional_properties = d
        return permission_index_response_200_data_definitions_item

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
