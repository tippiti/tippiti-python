from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.dictation_version_resource_format_type_1 import DictationVersionResourceFormatType1
from ..models.dictation_version_resource_status_type_1 import DictationVersionResourceStatusType1
from typing import cast






T = TypeVar("T", bound="DictationVersionResource")



@_attrs_define
class DictationVersionResource:
    """ 
        Attributes:
            id (str):  Example: aid-xyz12345.
            dictation_id (str):  Example: aid-xyz12345.
            version_number (int):
            text (str):
            format_ (DictationVersionResourceFormatType1 | str):
            status (DictationVersionResourceStatusType1 | str):
            source (str):
            changes (list[Any] | None):
            created_at (str):
            updated_at (str):
     """

    id: str
    dictation_id: str
    version_number: int
    text: str
    format_: DictationVersionResourceFormatType1 | str
    status: DictationVersionResourceStatusType1 | str
    source: str
    changes: list[Any] | None
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        dictation_id = self.dictation_id

        version_number = self.version_number

        text = self.text

        format_: str
        if isinstance(self.format_, DictationVersionResourceFormatType1):
            format_ = self.format_.value
        else:
            format_ = self.format_

        status: str
        if isinstance(self.status, DictationVersionResourceStatusType1):
            status = self.status.value
        else:
            status = self.status

        source = self.source

        changes: list[Any] | None
        if isinstance(self.changes, list):
            changes = self.changes


        else:
            changes = self.changes

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "dictation_id": dictation_id,
            "version_number": version_number,
            "text": text,
            "format": format_,
            "status": status,
            "source": source,
            "changes": changes,
            "created_at": created_at,
            "updated_at": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        dictation_id = d.pop("dictation_id")

        version_number = d.pop("version_number")

        text = d.pop("text")

        def _parse_format_(data: object) -> DictationVersionResourceFormatType1 | str:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                format_type_1 = DictationVersionResourceFormatType1(data)



                return format_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DictationVersionResourceFormatType1 | str, data)

        format_ = _parse_format_(d.pop("format"))


        def _parse_status(data: object) -> DictationVersionResourceStatusType1 | str:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                status_type_1 = DictationVersionResourceStatusType1(data)



                return status_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DictationVersionResourceStatusType1 | str, data)

        status = _parse_status(d.pop("status"))


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


        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        dictation_version_resource = cls(
            id=id,
            dictation_id=dictation_id,
            version_number=version_number,
            text=text,
            format_=format_,
            status=status,
            source=source,
            changes=changes,
            created_at=created_at,
            updated_at=updated_at,
        )


        dictation_version_resource.additional_properties = d
        return dictation_version_resource

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
