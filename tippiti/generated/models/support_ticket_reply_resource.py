from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.support_ticket_attachment_resource import SupportTicketAttachmentResource
  from ..models.support_ticket_reply_resource_user_type_0 import SupportTicketReplyResourceUserType0
  from ..models.support_ticket_reply_resource_user_type_1 import SupportTicketReplyResourceUserType1





T = TypeVar("T", bound="SupportTicketReplyResource")



@_attrs_define
class SupportTicketReplyResource:
    """ 
        Attributes:
            id (str):  Example: aid-xyz12345.
            content (str):
            created_at (str):
            user (SupportTicketReplyResourceUserType0 | SupportTicketReplyResourceUserType1):
            attachments (list[SupportTicketAttachmentResource] | Unset):
     """

    id: str
    content: str
    created_at: str
    user: SupportTicketReplyResourceUserType0 | SupportTicketReplyResourceUserType1
    attachments: list[SupportTicketAttachmentResource] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.support_ticket_attachment_resource import SupportTicketAttachmentResource
        from ..models.support_ticket_reply_resource_user_type_0 import SupportTicketReplyResourceUserType0
        from ..models.support_ticket_reply_resource_user_type_1 import SupportTicketReplyResourceUserType1
        id = self.id

        content = self.content

        created_at = self.created_at

        user: dict[str, Any]
        if isinstance(self.user, SupportTicketReplyResourceUserType0):
            user = self.user.to_dict()
        else:
            user = self.user.to_dict()


        attachments: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.attachments, Unset):
            attachments = []
            for attachments_item_data in self.attachments:
                attachments_item = attachments_item_data.to_dict()
                attachments.append(attachments_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "content": content,
            "created_at": created_at,
            "user": user,
        })
        if attachments is not UNSET:
            field_dict["attachments"] = attachments

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.support_ticket_attachment_resource import SupportTicketAttachmentResource
        from ..models.support_ticket_reply_resource_user_type_0 import SupportTicketReplyResourceUserType0
        from ..models.support_ticket_reply_resource_user_type_1 import SupportTicketReplyResourceUserType1
        d = dict(src_dict)
        id = d.pop("id")

        content = d.pop("content")

        created_at = d.pop("created_at")

        def _parse_user(data: object) -> SupportTicketReplyResourceUserType0 | SupportTicketReplyResourceUserType1:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                user_type_0 = SupportTicketReplyResourceUserType0.from_dict(data)



                return user_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            user_type_1 = SupportTicketReplyResourceUserType1.from_dict(data)



            return user_type_1

        user = _parse_user(d.pop("user"))


        _attachments = d.pop("attachments", UNSET)
        attachments: list[SupportTicketAttachmentResource] | Unset = UNSET
        if _attachments is not UNSET:
            attachments = []
            for attachments_item_data in _attachments:
                attachments_item = SupportTicketAttachmentResource.from_dict(attachments_item_data)



                attachments.append(attachments_item)


        support_ticket_reply_resource = cls(
            id=id,
            content=content,
            created_at=created_at,
            user=user,
            attachments=attachments,
        )


        support_ticket_reply_resource.additional_properties = d
        return support_ticket_reply_resource

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
