from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset







T = TypeVar("T", bound="PaymentMethodSetupIntentResponse200Data")



@_attrs_define
class PaymentMethodSetupIntentResponse200Data:
    """ 
        Attributes:
            gateway (str):
            client_secret (str):
     """

    gateway: str
    client_secret: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        gateway = self.gateway

        client_secret = self.client_secret


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "gateway": gateway,
            "client_secret": client_secret,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        gateway = d.pop("gateway")

        client_secret = d.pop("client_secret")

        payment_method_setup_intent_response_200_data = cls(
            gateway=gateway,
            client_secret=client_secret,
        )


        payment_method_setup_intent_response_200_data.additional_properties = d
        return payment_method_setup_intent_response_200_data

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
