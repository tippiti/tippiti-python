from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.save_version_request_format import SaveVersionRequestFormat
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="SaveVersionRequest")



@_attrs_define
class SaveVersionRequest:
    """ 
        Attributes:
            text (str):
            format_ (SaveVersionRequestFormat | Unset):
            expected_updated_at (None | str | Unset):
            change_summary (None | str | Unset):
     """

    text: str
    format_: SaveVersionRequestFormat | Unset = UNSET
    expected_updated_at: None | str | Unset = UNSET
    change_summary: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        text = self.text

        format_: str | Unset = UNSET
        if not isinstance(self.format_, Unset):
            format_ = self.format_.value


        expected_updated_at: None | str | Unset
        if isinstance(self.expected_updated_at, Unset):
            expected_updated_at = UNSET
        else:
            expected_updated_at = self.expected_updated_at

        change_summary: None | str | Unset
        if isinstance(self.change_summary, Unset):
            change_summary = UNSET
        else:
            change_summary = self.change_summary


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "text": text,
        })
        if format_ is not UNSET:
            field_dict["format"] = format_
        if expected_updated_at is not UNSET:
            field_dict["expected_updated_at"] = expected_updated_at
        if change_summary is not UNSET:
            field_dict["change_summary"] = change_summary

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        text = d.pop("text")

        _format_ = d.pop("format", UNSET)
        format_: SaveVersionRequestFormat | Unset
        if isinstance(_format_,  Unset):
            format_ = UNSET
        else:
            format_ = SaveVersionRequestFormat(_format_)




        def _parse_expected_updated_at(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        expected_updated_at = _parse_expected_updated_at(d.pop("expected_updated_at", UNSET))


        def _parse_change_summary(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        change_summary = _parse_change_summary(d.pop("change_summary", UNSET))


        save_version_request = cls(
            text=text,
            format_=format_,
            expected_updated_at=expected_updated_at,
            change_summary=change_summary,
        )


        save_version_request.additional_properties = d
        return save_version_request

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
