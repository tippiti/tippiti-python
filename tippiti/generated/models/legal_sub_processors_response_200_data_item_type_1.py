from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import Literal, cast






T = TypeVar("T", bound="LegalSubProcessorsResponse200DataItemType1")



@_attrs_define
class LegalSubProcessorsResponse200DataItemType1:
    """ 
        Attributes:
            company (Literal['Amazon Web Services EMEA SARL']):
            purpose (Literal['KI-Datenverarbeitung, E-Mail-Versand']):
            location (Literal['Luxemburg (EU)']):
            guarantee (None):
     """

    company: Literal['Amazon Web Services EMEA SARL']
    purpose: Literal['KI-Datenverarbeitung, E-Mail-Versand']
    location: Literal['Luxemburg (EU)']
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
        company = cast(Literal['Amazon Web Services EMEA SARL'] , d.pop("company"))
        if company != 'Amazon Web Services EMEA SARL':
            raise ValueError(f"company must match const 'Amazon Web Services EMEA SARL', got '{company}'")

        purpose = cast(Literal['KI-Datenverarbeitung, E-Mail-Versand'] , d.pop("purpose"))
        if purpose != 'KI-Datenverarbeitung, E-Mail-Versand':
            raise ValueError(f"purpose must match const 'KI-Datenverarbeitung, E-Mail-Versand', got '{purpose}'")

        location = cast(Literal['Luxemburg (EU)'] , d.pop("location"))
        if location != 'Luxemburg (EU)':
            raise ValueError(f"location must match const 'Luxemburg (EU)', got '{location}'")

        guarantee = d.pop("guarantee")

        legal_sub_processors_response_200_data_item_type_1 = cls(
            company=company,
            purpose=purpose,
            location=location,
            guarantee=guarantee,
        )


        legal_sub_processors_response_200_data_item_type_1.additional_properties = d
        return legal_sub_processors_response_200_data_item_type_1

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
