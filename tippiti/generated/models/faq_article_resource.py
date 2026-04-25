from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="FaqArticleResource")



@_attrs_define
class FaqArticleResource:
    """ 
        Attributes:
            id (str):  Example: aid-xyz12345.
            title (str):
            slug (str):
            categories (list[Any] | list[str] | None):
            icon (None | str):
            content (str):
            is_public (bool):
            is_support (bool):
            sort_order (int):
            created_at (str):
            updated_at (str):
     """

    id: str
    title: str
    slug: str
    categories: list[Any] | list[str] | None
    icon: None | str
    content: str
    is_public: bool
    is_support: bool
    sort_order: int
    created_at: str
    updated_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        title = self.title

        slug = self.slug

        categories: list[Any] | list[str] | None
        if isinstance(self.categories, list):
            categories = self.categories


        elif isinstance(self.categories, list):
            categories = self.categories


        else:
            categories = self.categories

        icon: None | str
        icon = self.icon

        content = self.content

        is_public = self.is_public

        is_support = self.is_support

        sort_order = self.sort_order

        created_at = self.created_at

        updated_at = self.updated_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "title": title,
            "slug": slug,
            "categories": categories,
            "icon": icon,
            "content": content,
            "is_public": is_public,
            "is_support": is_support,
            "sort_order": sort_order,
            "created_at": created_at,
            "updated_at": updated_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        title = d.pop("title")

        slug = d.pop("slug")

        def _parse_categories(data: object) -> list[Any] | list[str] | None:
            if data is None:
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                categories_type_0 = cast(list[Any], data)

                return categories_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, list):
                    raise TypeError()
                categories_type_2 = cast(list[str], data)

                return categories_type_2
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[Any] | list[str] | None, data)

        categories = _parse_categories(d.pop("categories"))


        def _parse_icon(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        icon = _parse_icon(d.pop("icon"))


        content = d.pop("content")

        is_public = d.pop("is_public")

        is_support = d.pop("is_support")

        sort_order = d.pop("sort_order")

        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        faq_article_resource = cls(
            id=id,
            title=title,
            slug=slug,
            categories=categories,
            icon=icon,
            content=content,
            is_public=is_public,
            is_support=is_support,
            sort_order=sort_order,
            created_at=created_at,
            updated_at=updated_at,
        )


        faq_article_resource.additional_properties = d
        return faq_article_resource

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
