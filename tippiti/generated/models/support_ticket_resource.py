from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.support_ticket_reply_resource import SupportTicketReplyResource
  from ..models.support_ticket_resource_department import SupportTicketResourceDepartment
  from ..models.support_ticket_resource_dictation import SupportTicketResourceDictation
  from ..models.support_ticket_resource_priority_type_0 import SupportTicketResourcePriorityType0
  from ..models.support_ticket_resource_status import SupportTicketResourceStatus





T = TypeVar("T", bound="SupportTicketResource")



@_attrs_define
class SupportTicketResource:
    """ 
        Attributes:
            id (str):  Example: aid-xyz12345.
            title (str):
            dictation_id (str):  Example: aid-xyz12345.
            last_reply_at (str):
            closed_at (str):
            created_at (str):
            status (SupportTicketResourceStatus):
            department (SupportTicketResourceDepartment):
            priority (None | SupportTicketResourcePriorityType0):
            dictation (SupportTicketResourceDictation | Unset):
            replies (list[SupportTicketReplyResource] | Unset):
     """

    id: str
    title: str
    dictation_id: str
    last_reply_at: str
    closed_at: str
    created_at: str
    status: SupportTicketResourceStatus
    department: SupportTicketResourceDepartment
    priority: None | SupportTicketResourcePriorityType0
    dictation: SupportTicketResourceDictation | Unset = UNSET
    replies: list[SupportTicketReplyResource] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.support_ticket_reply_resource import SupportTicketReplyResource
        from ..models.support_ticket_resource_department import SupportTicketResourceDepartment
        from ..models.support_ticket_resource_dictation import SupportTicketResourceDictation
        from ..models.support_ticket_resource_priority_type_0 import SupportTicketResourcePriorityType0
        from ..models.support_ticket_resource_status import SupportTicketResourceStatus
        id = self.id

        title = self.title

        dictation_id = self.dictation_id

        last_reply_at = self.last_reply_at

        closed_at = self.closed_at

        created_at = self.created_at

        status = self.status.to_dict()

        department = self.department.to_dict()

        priority: dict[str, Any] | None
        if isinstance(self.priority, SupportTicketResourcePriorityType0):
            priority = self.priority.to_dict()
        else:
            priority = self.priority

        dictation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.dictation, Unset):
            dictation = self.dictation.to_dict()

        replies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.replies, Unset):
            replies = []
            for replies_item_data in self.replies:
                replies_item = replies_item_data.to_dict()
                replies.append(replies_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "title": title,
            "dictation_id": dictation_id,
            "last_reply_at": last_reply_at,
            "closed_at": closed_at,
            "created_at": created_at,
            "status": status,
            "department": department,
            "priority": priority,
        })
        if dictation is not UNSET:
            field_dict["dictation"] = dictation
        if replies is not UNSET:
            field_dict["replies"] = replies

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.support_ticket_reply_resource import SupportTicketReplyResource
        from ..models.support_ticket_resource_department import SupportTicketResourceDepartment
        from ..models.support_ticket_resource_dictation import SupportTicketResourceDictation
        from ..models.support_ticket_resource_priority_type_0 import SupportTicketResourcePriorityType0
        from ..models.support_ticket_resource_status import SupportTicketResourceStatus
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        dictation_id = d.pop("dictation_id")

        last_reply_at = d.pop("last_reply_at")

        closed_at = d.pop("closed_at")

        created_at = d.pop("created_at")

        status = SupportTicketResourceStatus.from_dict(d.pop("status"))




        department = SupportTicketResourceDepartment.from_dict(d.pop("department"))




        def _parse_priority(data: object) -> None | SupportTicketResourcePriorityType0:
            if data is None:
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                priority_type_0 = SupportTicketResourcePriorityType0.from_dict(data)



                return priority_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | SupportTicketResourcePriorityType0, data)

        priority = _parse_priority(d.pop("priority"))


        _dictation = d.pop("dictation", UNSET)
        dictation: SupportTicketResourceDictation | Unset
        if isinstance(_dictation,  Unset):
            dictation = UNSET
        else:
            dictation = SupportTicketResourceDictation.from_dict(_dictation)




        _replies = d.pop("replies", UNSET)
        replies: list[SupportTicketReplyResource] | Unset = UNSET
        if _replies is not UNSET:
            replies = []
            for replies_item_data in _replies:
                replies_item = SupportTicketReplyResource.from_dict(replies_item_data)



                replies.append(replies_item)


        support_ticket_resource = cls(
            id=id,
            title=title,
            dictation_id=dictation_id,
            last_reply_at=last_reply_at,
            closed_at=closed_at,
            created_at=created_at,
            status=status,
            department=department,
            priority=priority,
            dictation=dictation,
            replies=replies,
        )


        support_ticket_resource.additional_properties = d
        return support_ticket_resource

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
