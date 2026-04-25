from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.payment_method_setup_intent_body_gateway import PaymentMethodSetupIntentBodyGateway
from ..types import UNSET, Unset






T = TypeVar("T", bound="PaymentMethodSetupIntentBody")



@_attrs_define
class PaymentMethodSetupIntentBody:
    """ 
        Attributes:
            gateway (PaymentMethodSetupIntentBodyGateway | Unset):
     """

    gateway: PaymentMethodSetupIntentBodyGateway | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        gateway: str | Unset = UNSET
        if not isinstance(self.gateway, Unset):
            gateway = self.gateway.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if gateway is not UNSET:
            field_dict["gateway"] = gateway

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _gateway = d.pop("gateway", UNSET)
        gateway: PaymentMethodSetupIntentBodyGateway | Unset
        if isinstance(_gateway,  Unset):
            gateway = UNSET
        else:
            gateway = PaymentMethodSetupIntentBodyGateway(_gateway)




        payment_method_setup_intent_body = cls(
            gateway=gateway,
        )


        payment_method_setup_intent_body.additional_properties = d
        return payment_method_setup_intent_body

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
