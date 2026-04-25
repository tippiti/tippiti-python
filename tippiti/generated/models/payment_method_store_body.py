from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.payment_method_store_body_gateway import PaymentMethodStoreBodyGateway
from ..types import UNSET, Unset






T = TypeVar("T", bound="PaymentMethodStoreBody")



@_attrs_define
class PaymentMethodStoreBody:
    """ 
        Attributes:
            payment_method_id (str):  Example: aid-xyz12345.
            gateway (PaymentMethodStoreBodyGateway | Unset):
     """

    payment_method_id: str
    gateway: PaymentMethodStoreBodyGateway | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        payment_method_id = self.payment_method_id

        gateway: str | Unset = UNSET
        if not isinstance(self.gateway, Unset):
            gateway = self.gateway.value



        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "payment_method_id": payment_method_id,
        })
        if gateway is not UNSET:
            field_dict["gateway"] = gateway

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        payment_method_id = d.pop("payment_method_id")

        _gateway = d.pop("gateway", UNSET)
        gateway: PaymentMethodStoreBodyGateway | Unset
        if isinstance(_gateway,  Unset):
            gateway = UNSET
        else:
            gateway = PaymentMethodStoreBodyGateway(_gateway)




        payment_method_store_body = cls(
            payment_method_id=payment_method_id,
            gateway=gateway,
        )


        payment_method_store_body.additional_properties = d
        return payment_method_store_body

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
