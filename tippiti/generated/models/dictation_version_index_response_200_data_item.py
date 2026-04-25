from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="DictationVersionIndexResponse200DataItem")



@_attrs_define
class DictationVersionIndexResponse200DataItem:
    """ 
        Attributes:
            id (int):
            version_number (int):
            status (str):
            source (str):
            changes (list[Any] | None):
            updated_at (str):
     """

    id: int
    version_number: int
    status: str
    source: str
    changes: list[Any] | None
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        version_number = self.version_number

        status = self.status

        source = self.source

        changes: list[Any] | None
        if isinstance(self.changes, list):
            changes = self.changes


        else:
            changes = self.changes

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "version_number": version_number,
            "status": status,
            "source": source,
            "changes": changes,
            "updated_at": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        version_number = d.pop("version_number")

        status = d.pop("status")

        source = d.pop("source")

        def _parse_changes(data: object) -> list[Any] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                changes_type_0 = cast(list[Any], data)

                return changes_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | None, data)

        changes = _parse_changes(d.pop("changes"))


        updated_at = d.pop("updated_at")

        dictation_version_index_response_200_data_item = cls(
            id=id,
            version_number=version_number,
            status=status,
            source=source,
            changes=changes,
            updated_at=updated_at,
        )


        dictation_version_index_response_200_data_item.additional_properties = d
        return dictation_version_index_response_200_data_item

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
