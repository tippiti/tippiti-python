from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="DictationShareResourceViewsItem")



@_attrs_define
class DictationShareResourceViewsItem:
    """ 
        Attributes:
            id (str):  Example: aid-xyz12345.
            viewed_at (None | str):
     """

    id: str
    viewed_at: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        viewed_at: None | str
        viewed_at = self.viewed_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "viewed_at": viewed_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_viewed_at(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        viewed_at = _parse_viewed_at(d.pop("viewed_at"))


        dictation_share_resource_views_item = cls(
            id=id,
            viewed_at=viewed_at,
        )


        dictation_share_resource_views_item.additional_properties = d
        return dictation_share_resource_views_item

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
