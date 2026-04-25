from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="SupportTicketResourceStatus")



@_attrs_define
class SupportTicketResourceStatus:
    """ 
        Attributes:
            id (str):  Example: aid-xyz12345.
            name (str):
            color (str):
            is_closed (bool):
            customer_filter_group (None | str):
            customer_filter_color (None | str):
     """

    id: str
    name: str
    color: str
    is_closed: bool
    customer_filter_group: None | str
    customer_filter_color: None | str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        color = self.color

        is_closed = self.is_closed

        customer_filter_group: None | str
        customer_filter_group = self.customer_filter_group

        customer_filter_color: None | str
        customer_filter_color = self.customer_filter_color


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "color": color,
            "is_closed": is_closed,
            "customer_filter_group": customer_filter_group,
            "customer_filter_color": customer_filter_color,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        name = d.pop("name")

        color = d.pop("color")

        is_closed = d.pop("is_closed")

        def _parse_customer_filter_group(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        customer_filter_group = _parse_customer_filter_group(d.pop("customer_filter_group"))


        def _parse_customer_filter_color(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        customer_filter_color = _parse_customer_filter_color(d.pop("customer_filter_color"))


        support_ticket_resource_status = cls(
            id=id,
            name=name,
            color=color,
            is_closed=is_closed,
            customer_filter_group=customer_filter_group,
            customer_filter_color=customer_filter_color,
        )


        support_ticket_resource_status.additional_properties = d
        return support_ticket_resource_status

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
