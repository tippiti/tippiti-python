from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.dictation_share_resource_email_count_type_1 import DictationShareResourceEmailCountType1
from ..models.dictation_share_resource_view_count_type_1 import DictationShareResourceViewCountType1
from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dictation_share_resource_emails_item import DictationShareResourceEmailsItem
  from ..models.dictation_share_resource_views_item import DictationShareResourceViewsItem





T = TypeVar("T", bound="DictationShareResource")



@_attrs_define
class DictationShareResource:
    """ 
        Attributes:
            id (str):  Example: aid-xyz12345.
            dictation_id (str):  Example: aid-xyz12345.
            dictation_title (str):
            token (str):
            has_password (bool):
            allow_delete (bool):
            allow_archive (bool):
            show_notes (bool):
            expires_at (str):
            is_expired (bool):
            view_count (DictationShareResourceViewCountType1 | str):
            email_count (DictationShareResourceEmailCountType1 | str):
            created_at (str):
            emails (list[DictationShareResourceEmailsItem] | Unset):
            created_by_name (str | Unset):
            views (list[DictationShareResourceViewsItem] | Unset):
     """

    id: str
    dictation_id: str
    dictation_title: str
    token: str
    has_password: bool
    allow_delete: bool
    allow_archive: bool
    show_notes: bool
    expires_at: str
    is_expired: bool
    view_count: DictationShareResourceViewCountType1 | str
    email_count: DictationShareResourceEmailCountType1 | str
    created_at: str
    emails: list[DictationShareResourceEmailsItem] | Unset = UNSET
    created_by_name: str | Unset = UNSET
    views: list[DictationShareResourceViewsItem] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dictation_share_resource_emails_item import DictationShareResourceEmailsItem
        from ..models.dictation_share_resource_views_item import DictationShareResourceViewsItem
        id = self.id

        dictation_id = self.dictation_id

        dictation_title = self.dictation_title

        token = self.token

        has_password = self.has_password

        allow_delete = self.allow_delete

        allow_archive = self.allow_archive

        show_notes = self.show_notes

        expires_at = self.expires_at

        is_expired = self.is_expired

        view_count: int | str
        if isinstance(self.view_count, DictationShareResourceViewCountType1):
            view_count = self.view_count.value
        else:
            view_count = self.view_count

        email_count: int | str
        if isinstance(self.email_count, DictationShareResourceEmailCountType1):
            email_count = self.email_count.value
        else:
            email_count = self.email_count

        created_at = self.created_at

        emails: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.emails, Unset):
            emails = []
            for emails_item_data in self.emails:
                emails_item = emails_item_data.to_dict()
                emails.append(emails_item)



        created_by_name = self.created_by_name

        views: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.views, Unset):
            views = []
            for views_item_data in self.views:
                views_item = views_item_data.to_dict()
                views.append(views_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "dictation_id": dictation_id,
            "dictation_title": dictation_title,
            "token": token,
            "has_password": has_password,
            "allow_delete": allow_delete,
            "allow_archive": allow_archive,
            "show_notes": show_notes,
            "expires_at": expires_at,
            "is_expired": is_expired,
            "view_count": view_count,
            "email_count": email_count,
            "created_at": created_at,
        })
        if emails is not UNSET:
            field_dict["emails"] = emails
        if created_by_name is not UNSET:
            field_dict["created_by_name"] = created_by_name
        if views is not UNSET:
            field_dict["views"] = views

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dictation_share_resource_emails_item import DictationShareResourceEmailsItem
        from ..models.dictation_share_resource_views_item import DictationShareResourceViewsItem
        d = dict(src_dict)
        id = d.pop("id")

        dictation_id = d.pop("dictation_id")

        dictation_title = d.pop("dictation_title")

        token = d.pop("token")

        has_password = d.pop("has_password")

        allow_delete = d.pop("allow_delete")

        allow_archive = d.pop("allow_archive")

        show_notes = d.pop("show_notes")

        expires_at = d.pop("expires_at")

        is_expired = d.pop("is_expired")

        def _parse_view_count(data: object) -> DictationShareResourceViewCountType1 | str:
            try:
                if not isinstance(data, int):
                    raise TypeError()
                view_count_type_1 = DictationShareResourceViewCountType1(data)



                return view_count_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DictationShareResourceViewCountType1 | str, data)

        view_count = _parse_view_count(d.pop("view_count"))


        def _parse_email_count(data: object) -> DictationShareResourceEmailCountType1 | str:
            try:
                if not isinstance(data, int):
                    raise TypeError()
                email_count_type_1 = DictationShareResourceEmailCountType1(data)



                return email_count_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DictationShareResourceEmailCountType1 | str, data)

        email_count = _parse_email_count(d.pop("email_count"))


        created_at = d.pop("created_at")

        _emails = d.pop("emails", UNSET)
        emails: list[DictationShareResourceEmailsItem] | Unset = UNSET
        if _emails is not UNSET:
            emails = []
            for emails_item_data in _emails:
                emails_item = DictationShareResourceEmailsItem.from_dict(emails_item_data)



                emails.append(emails_item)


        created_by_name = d.pop("created_by_name", UNSET)

        _views = d.pop("views", UNSET)
        views: list[DictationShareResourceViewsItem] | Unset = UNSET
        if _views is not UNSET:
            views = []
            for views_item_data in _views:
                views_item = DictationShareResourceViewsItem.from_dict(views_item_data)



                views.append(views_item)


        dictation_share_resource = cls(
            id=id,
            dictation_id=dictation_id,
            dictation_title=dictation_title,
            token=token,
            has_password=has_password,
            allow_delete=allow_delete,
            allow_archive=allow_archive,
            show_notes=show_notes,
            expires_at=expires_at,
            is_expired=is_expired,
            view_count=view_count,
            email_count=email_count,
            created_at=created_at,
            emails=emails,
            created_by_name=created_by_name,
            views=views,
        )


        dictation_share_resource.additional_properties = d
        return dictation_share_resource

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
