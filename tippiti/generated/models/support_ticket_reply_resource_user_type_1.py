from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.support_ticket_reply_resource_user_type_1_name_type_1 import SupportTicketReplyResourceUserType1NameType1
from typing import cast






T = TypeVar("T", bound="SupportTicketReplyResourceUserType1")



@_attrs_define
class SupportTicketReplyResourceUserType1:
    """ 
        Attributes:
            id (None):
            name (str | SupportTicketReplyResourceUserType1NameType1):
            is_staff (bool):
     """

    id: None
    name: str | SupportTicketReplyResourceUserType1NameType1
    is_staff: bool
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name: str
        if isinstance(self.name, SupportTicketReplyResourceUserType1NameType1):
            name = self.name.value
        else:
            name = self.name

        is_staff = self.is_staff


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "name": name,
            "is_staff": is_staff,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_name(data: object) -> str | SupportTicketReplyResourceUserType1NameType1:
            try:
                if not isinstance(data, str):
                    raise TypeError()
                name_type_1 = SupportTicketReplyResourceUserType1NameType1(data)



                return name_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(str | SupportTicketReplyResourceUserType1NameType1, data)

        name = _parse_name(d.pop("name"))


        is_staff = d.pop("is_staff")

        support_ticket_reply_resource_user_type_1 = cls(
            id=id,
            name=name,
            is_staff=is_staff,
        )


        support_ticket_reply_resource_user_type_1.additional_properties = d
        return support_ticket_reply_resource_user_type_1

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
