from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="DictationExportDocxBody")



@_attrs_define
class DictationExportDocxBody:
    """ 
        Attributes:
            html (str):
            version_id (str | Unset):  Example: aid-xyz12345.
            template_id (str | Unset):  Example: aid-xyz12345.
     """

    html: str
    version_id: str | Unset = UNSET
    template_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        html = self.html

        version_id = self.version_id

        template_id = self.template_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "html": html,
        })
        if version_id is not UNSET:
            field_dict["version_id"] = version_id
        if template_id is not UNSET:
            field_dict["template_id"] = template_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        html = d.pop("html")

        version_id = d.pop("version_id", UNSET)

        template_id = d.pop("template_id", UNSET)

        dictation_export_docx_body = cls(
            html=html,
            version_id=version_id,
            template_id=template_id,
        )


        dictation_export_docx_body.additional_properties = d
        return dictation_export_docx_body

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
