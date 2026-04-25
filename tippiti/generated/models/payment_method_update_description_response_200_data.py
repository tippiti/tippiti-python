from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast
from typing import Literal, cast

if TYPE_CHECKING:
  from ..models.payment_method_resource import PaymentMethodResource





T = TypeVar("T", bound="PaymentMethodUpdateDescriptionResponse200Data")



@_attrs_define
class PaymentMethodUpdateDescriptionResponse200Data:
    """ 
        Attributes:
            message (Literal['Beschreibung wurde aktualisiert.']):
            payment_method (PaymentMethodResource):
     """

    message: Literal['Beschreibung wurde aktualisiert.']
    payment_method: PaymentMethodResource
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.payment_method_resource import PaymentMethodResource
        message = self.message

        payment_method = self.payment_method.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "message": message,
            "payment_method": payment_method,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.payment_method_resource import PaymentMethodResource
        d = dict(src_dict)
        message = cast(Literal['Beschreibung wurde aktualisiert.'] , d.pop("message"))
        if message != 'Beschreibung wurde aktualisiert.':
            raise ValueError(f"message must match const 'Beschreibung wurde aktualisiert.', got '{message}'")

        payment_method = PaymentMethodResource.from_dict(d.pop("payment_method"))




        payment_method_update_description_response_200_data = cls(
            message=message,
            payment_method=payment_method,
        )


        payment_method_update_description_response_200_data.additional_properties = d
        return payment_method_update_description_response_200_data

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
