from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Literal, cast






T = TypeVar("T", bound="LegalSubProcessorsResponse200DataItemType0")



@_attrs_define
class LegalSubProcessorsResponse200DataItemType0:
    """ 
        Attributes:
            company (Literal['Hetzner Online GmbH']):
            purpose (Literal['Hosting, Serverinfrastruktur']):
            location (Literal['Deutschland (EU)']):
            guarantee (None):
     """

    company: Literal['Hetzner Online GmbH']
    purpose: Literal['Hosting, Serverinfrastruktur']
    location: Literal['Deutschland (EU)']
    guarantee: None
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        company = self.company

        purpose = self.purpose

        location = self.location

        guarantee = self.guarantee


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "company": company,
            "purpose": purpose,
            "location": location,
            "guarantee": guarantee,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        company = cast(Literal['Hetzner Online GmbH'] , d.pop("company"))
        if company != 'Hetzner Online GmbH':
            raise ValueError(f"company must match const 'Hetzner Online GmbH', got '{company}'")

        purpose = cast(Literal['Hosting, Serverinfrastruktur'] , d.pop("purpose"))
        if purpose != 'Hosting, Serverinfrastruktur':
            raise ValueError(f"purpose must match const 'Hosting, Serverinfrastruktur', got '{purpose}'")

        location = cast(Literal['Deutschland (EU)'] , d.pop("location"))
        if location != 'Deutschland (EU)':
            raise ValueError(f"location must match const 'Deutschland (EU)', got '{location}'")

        guarantee = d.pop("guarantee")

        legal_sub_processors_response_200_data_item_type_0 = cls(
            company=company,
            purpose=purpose,
            location=location,
            guarantee=guarantee,
        )


        legal_sub_processors_response_200_data_item_type_0.additional_properties = d
        return legal_sub_processors_response_200_data_item_type_0

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
