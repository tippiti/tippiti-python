from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.update_account_request_salutation import UpdateAccountRequestSalutation
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="UpdateAccountRequest")



@_attrs_define
class UpdateAccountRequest:
    """ 
        Attributes:
            salutation (UpdateAccountRequestSalutation | Unset): Profile
            title (None | str | Unset):
            first_name (None | str | Unset):
            last_name (str | Unset):
            email (str | Unset):
            billing_company (None | str | Unset): Billing
            billing_name (None | str | Unset):
            billing_street (None | str | Unset):
            billing_street_2 (None | str | Unset):
            billing_zip (None | str | Unset):
            billing_city (None | str | Unset):
            billing_country (None | str | Unset):
            tax_id (None | str | Unset):
     """

    salutation: UpdateAccountRequestSalutation | Unset = UNSET
    title: None | str | Unset = UNSET
    first_name: None | str | Unset = UNSET
    last_name: str | Unset = UNSET
    email: str | Unset = UNSET
    billing_company: None | str | Unset = UNSET
    billing_name: None | str | Unset = UNSET
    billing_street: None | str | Unset = UNSET
    billing_street_2: None | str | Unset = UNSET
    billing_zip: None | str | Unset = UNSET
    billing_city: None | str | Unset = UNSET
    billing_country: None | str | Unset = UNSET
    tax_id: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        salutation: str | Unset = UNSET
        if not isinstance(self.salutation, Unset):
            salutation = self.salutation.value


        title: None | str | Unset
        if isinstance(self.title, Unset):
            title = UNSET
        else:
            title = self.title

        first_name: None | str | Unset
        if isinstance(self.first_name, Unset):
            first_name = UNSET
        else:
            first_name = self.first_name

        last_name = self.last_name

        email = self.email

        billing_company: None | str | Unset
        if isinstance(self.billing_company, Unset):
            billing_company = UNSET
        else:
            billing_company = self.billing_company

        billing_name: None | str | Unset
        if isinstance(self.billing_name, Unset):
            billing_name = UNSET
        else:
            billing_name = self.billing_name

        billing_street: None | str | Unset
        if isinstance(self.billing_street, Unset):
            billing_street = UNSET
        else:
            billing_street = self.billing_street

        billing_street_2: None | str | Unset
        if isinstance(self.billing_street_2, Unset):
            billing_street_2 = UNSET
        else:
            billing_street_2 = self.billing_street_2

        billing_zip: None | str | Unset
        if isinstance(self.billing_zip, Unset):
            billing_zip = UNSET
        else:
            billing_zip = self.billing_zip

        billing_city: None | str | Unset
        if isinstance(self.billing_city, Unset):
            billing_city = UNSET
        else:
            billing_city = self.billing_city

        billing_country: None | str | Unset
        if isinstance(self.billing_country, Unset):
            billing_country = UNSET
        else:
            billing_country = self.billing_country

        tax_id: None | str | Unset
        if isinstance(self.tax_id, Unset):
            tax_id = UNSET
        else:
            tax_id = self.tax_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if salutation is not UNSET:
            field_dict["salutation"] = salutation
        if title is not UNSET:
            field_dict["title"] = title
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if email is not UNSET:
            field_dict["email"] = email
        if billing_company is not UNSET:
            field_dict["billing_company"] = billing_company
        if billing_name is not UNSET:
            field_dict["billing_name"] = billing_name
        if billing_street is not UNSET:
            field_dict["billing_street"] = billing_street
        if billing_street_2 is not UNSET:
            field_dict["billing_street_2"] = billing_street_2
        if billing_zip is not UNSET:
            field_dict["billing_zip"] = billing_zip
        if billing_city is not UNSET:
            field_dict["billing_city"] = billing_city
        if billing_country is not UNSET:
            field_dict["billing_country"] = billing_country
        if tax_id is not UNSET:
            field_dict["tax_id"] = tax_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _salutation = d.pop("salutation", UNSET)
        salutation: UpdateAccountRequestSalutation | Unset
        if isinstance(_salutation,  Unset):
            salutation = UNSET
        else:
            salutation = UpdateAccountRequestSalutation(_salutation)




        def _parse_title(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        title = _parse_title(d.pop("title", UNSET))


        def _parse_first_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        first_name = _parse_first_name(d.pop("first_name", UNSET))


        last_name = d.pop("last_name", UNSET)

        email = d.pop("email", UNSET)

        def _parse_billing_company(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        billing_company = _parse_billing_company(d.pop("billing_company", UNSET))


        def _parse_billing_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        billing_name = _parse_billing_name(d.pop("billing_name", UNSET))


        def _parse_billing_street(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        billing_street = _parse_billing_street(d.pop("billing_street", UNSET))


        def _parse_billing_street_2(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        billing_street_2 = _parse_billing_street_2(d.pop("billing_street_2", UNSET))


        def _parse_billing_zip(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        billing_zip = _parse_billing_zip(d.pop("billing_zip", UNSET))


        def _parse_billing_city(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        billing_city = _parse_billing_city(d.pop("billing_city", UNSET))


        def _parse_billing_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        billing_country = _parse_billing_country(d.pop("billing_country", UNSET))


        def _parse_tax_id(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        tax_id = _parse_tax_id(d.pop("tax_id", UNSET))


        update_account_request = cls(
            salutation=salutation,
            title=title,
            first_name=first_name,
            last_name=last_name,
            email=email,
            billing_company=billing_company,
            billing_name=billing_name,
            billing_street=billing_street,
            billing_street_2=billing_street_2,
            billing_zip=billing_zip,
            billing_city=billing_city,
            billing_country=billing_country,
            tax_id=tax_id,
        )


        update_account_request.additional_properties = d
        return update_account_request

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
