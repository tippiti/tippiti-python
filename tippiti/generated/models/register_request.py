from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="RegisterRequest")



@_attrs_define
class RegisterRequest:
    """ 
        Attributes:
            first_name (str):
            last_name (str):
            email (str):
            password (str):
            password_confirmation (str):
            referral_code (None | str | Unset):
            accept_terms (str | Unset):
            accept_privacy (str | Unset):
            accept_business (str | Unset):
     """

    first_name: str
    last_name: str
    email: str
    password: str
    password_confirmation: str
    referral_code: None | str | Unset = UNSET
    accept_terms: str | Unset = UNSET
    accept_privacy: str | Unset = UNSET
    accept_business: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        first_name = self.first_name

        last_name = self.last_name

        email = self.email

        password = self.password

        password_confirmation = self.password_confirmation

        referral_code: None | str | Unset
        if isinstance(self.referral_code, Unset):
            referral_code = UNSET
        else:
            referral_code = self.referral_code

        accept_terms = self.accept_terms

        accept_privacy = self.accept_privacy

        accept_business = self.accept_business


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "password": password,
            "password_confirmation": password_confirmation,
        })
        if referral_code is not UNSET:
            field_dict["referral_code"] = referral_code
        if accept_terms is not UNSET:
            field_dict["accept_terms"] = accept_terms
        if accept_privacy is not UNSET:
            field_dict["accept_privacy"] = accept_privacy
        if accept_business is not UNSET:
            field_dict["accept_business"] = accept_business

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        first_name = d.pop("first_name")

        last_name = d.pop("last_name")

        email = d.pop("email")

        password = d.pop("password")

        password_confirmation = d.pop("password_confirmation")

        def _parse_referral_code(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        referral_code = _parse_referral_code(d.pop("referral_code", UNSET))


        accept_terms = d.pop("accept_terms", UNSET)

        accept_privacy = d.pop("accept_privacy", UNSET)

        accept_business = d.pop("accept_business", UNSET)

        register_request = cls(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            password_confirmation=password_confirmation,
            referral_code=referral_code,
            accept_terms=accept_terms,
            accept_privacy=accept_privacy,
            accept_business=accept_business,
        )


        register_request.additional_properties = d
        return register_request

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
