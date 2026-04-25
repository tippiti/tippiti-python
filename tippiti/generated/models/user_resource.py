from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from dateutil.parser import isoparse
from typing import cast
import datetime






T = TypeVar("T", bound="UserResource")



@_attrs_define
class UserResource:
    """ 
        Attributes:
            id (str):  Example: aid-xyz12345.
            salutation (None | str):
            title (None | str):
            first_name (None | str):
            last_name (None | str):
            name (str):
            email (str):
            is_sub_user (bool):
            is_regular_user (bool):
            is_admin (bool):
            credit_balance (int):
            price_per_1k_chars (str):
            email_verified_at (datetime.datetime | None):
            has_starting_credits (bool):
            created_at (datetime.datetime | None):
            billing_company (None | str):
            billing_name (None | str):
            billing_street (None | str):
            billing_street_2 (None | str):
            billing_zip (None | str):
            billing_city (None | str):
            billing_country (str):
            tax_id (None | str):
            profile_complete (bool):
            two_factor_enabled (bool):
            help_seen (bool):
            ui_preferences (None | str):
            is_auto_topup_active (str):
            permissions (str | Unset):
            dictation_access (str | Unset):
     """

    id: str
    salutation: None | str
    title: None | str
    first_name: None | str
    last_name: None | str
    name: str
    email: str
    is_sub_user: bool
    is_regular_user: bool
    is_admin: bool
    credit_balance: int
    price_per_1k_chars: str
    email_verified_at: datetime.datetime | None
    has_starting_credits: bool
    created_at: datetime.datetime | None
    billing_company: None | str
    billing_name: None | str
    billing_street: None | str
    billing_street_2: None | str
    billing_zip: None | str
    billing_city: None | str
    billing_country: str
    tax_id: None | str
    profile_complete: bool
    two_factor_enabled: bool
    help_seen: bool
    ui_preferences: None | str
    is_auto_topup_active: str
    permissions: str | Unset = UNSET
    dictation_access: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        salutation: None | str
        salutation = self.salutation

        title: None | str
        title = self.title

        first_name: None | str
        first_name = self.first_name

        last_name: None | str
        last_name = self.last_name

        name = self.name

        email = self.email

        is_sub_user = self.is_sub_user

        is_regular_user = self.is_regular_user

        is_admin = self.is_admin

        credit_balance = self.credit_balance

        price_per_1k_chars = self.price_per_1k_chars

        email_verified_at: None | str
        if isinstance(self.email_verified_at, datetime.datetime):
            email_verified_at = self.email_verified_at.isoformat()
        else:
            email_verified_at = self.email_verified_at

        has_starting_credits = self.has_starting_credits

        created_at: None | str
        if isinstance(self.created_at, datetime.datetime):
            created_at = self.created_at.isoformat()
        else:
            created_at = self.created_at

        billing_company: None | str
        billing_company = self.billing_company

        billing_name: None | str
        billing_name = self.billing_name

        billing_street: None | str
        billing_street = self.billing_street

        billing_street_2: None | str
        billing_street_2 = self.billing_street_2

        billing_zip: None | str
        billing_zip = self.billing_zip

        billing_city: None | str
        billing_city = self.billing_city

        billing_country = self.billing_country

        tax_id: None | str
        tax_id = self.tax_id

        profile_complete = self.profile_complete

        two_factor_enabled = self.two_factor_enabled

        help_seen = self.help_seen

        ui_preferences: None | str
        ui_preferences = self.ui_preferences

        is_auto_topup_active = self.is_auto_topup_active

        permissions = self.permissions

        dictation_access = self.dictation_access


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "salutation": salutation,
            "title": title,
            "first_name": first_name,
            "last_name": last_name,
            "name": name,
            "email": email,
            "is_sub_user": is_sub_user,
            "is_regular_user": is_regular_user,
            "is_admin": is_admin,
            "credit_balance": credit_balance,
            "price_per_1k_chars": price_per_1k_chars,
            "email_verified_at": email_verified_at,
            "has_starting_credits": has_starting_credits,
            "created_at": created_at,
            "billing_company": billing_company,
            "billing_name": billing_name,
            "billing_street": billing_street,
            "billing_street_2": billing_street_2,
            "billing_zip": billing_zip,
            "billing_city": billing_city,
            "billing_country": billing_country,
            "tax_id": tax_id,
            "profile_complete": profile_complete,
            "two_factor_enabled": two_factor_enabled,
            "help_seen": help_seen,
            "ui_preferences": ui_preferences,
            "is_auto_topup_active": is_auto_topup_active,
        })
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if dictation_access is not UNSET:
            field_dict["dictation_access"] = dictation_access

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_salutation(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        salutation = _parse_salutation(d.pop("salutation"))


        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))


        def _parse_first_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        first_name = _parse_first_name(d.pop("first_name"))


        def _parse_last_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        last_name = _parse_last_name(d.pop("last_name"))


        name = d.pop("name")

        email = d.pop("email")

        is_sub_user = d.pop("is_sub_user")

        is_regular_user = d.pop("is_regular_user")

        is_admin = d.pop("is_admin")

        credit_balance = d.pop("credit_balance")

        price_per_1k_chars = d.pop("price_per_1k_chars")

        def _parse_email_verified_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                email_verified_at_type_0 = isoparse(data)



                return email_verified_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        email_verified_at = _parse_email_verified_at(d.pop("email_verified_at"))


        has_starting_credits = d.pop("has_starting_credits")

        def _parse_created_at(data: object) -> datetime.datetime | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                created_at_type_0 = isoparse(data)



                return created_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None, data)

        created_at = _parse_created_at(d.pop("created_at"))


        def _parse_billing_company(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        billing_company = _parse_billing_company(d.pop("billing_company"))


        def _parse_billing_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        billing_name = _parse_billing_name(d.pop("billing_name"))


        def _parse_billing_street(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        billing_street = _parse_billing_street(d.pop("billing_street"))


        def _parse_billing_street_2(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        billing_street_2 = _parse_billing_street_2(d.pop("billing_street_2"))


        def _parse_billing_zip(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        billing_zip = _parse_billing_zip(d.pop("billing_zip"))


        def _parse_billing_city(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        billing_city = _parse_billing_city(d.pop("billing_city"))


        billing_country = d.pop("billing_country")

        def _parse_tax_id(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        tax_id = _parse_tax_id(d.pop("tax_id"))


        profile_complete = d.pop("profile_complete")

        two_factor_enabled = d.pop("two_factor_enabled")

        help_seen = d.pop("help_seen")

        def _parse_ui_preferences(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        ui_preferences = _parse_ui_preferences(d.pop("ui_preferences"))


        is_auto_topup_active = d.pop("is_auto_topup_active")

        permissions = d.pop("permissions", UNSET)

        dictation_access = d.pop("dictation_access", UNSET)

        user_resource = cls(
            id=id,
            salutation=salutation,
            title=title,
            first_name=first_name,
            last_name=last_name,
            name=name,
            email=email,
            is_sub_user=is_sub_user,
            is_regular_user=is_regular_user,
            is_admin=is_admin,
            credit_balance=credit_balance,
            price_per_1k_chars=price_per_1k_chars,
            email_verified_at=email_verified_at,
            has_starting_credits=has_starting_credits,
            created_at=created_at,
            billing_company=billing_company,
            billing_name=billing_name,
            billing_street=billing_street,
            billing_street_2=billing_street_2,
            billing_zip=billing_zip,
            billing_city=billing_city,
            billing_country=billing_country,
            tax_id=tax_id,
            profile_complete=profile_complete,
            two_factor_enabled=two_factor_enabled,
            help_seen=help_seen,
            ui_preferences=ui_preferences,
            is_auto_topup_active=is_auto_topup_active,
            permissions=permissions,
            dictation_access=dictation_access,
        )


        user_resource.additional_properties = d
        return user_resource

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
