from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.faq_article_resource import FaqArticleResource





T = TypeVar("T", bound="FaqArticleSupportResponse200")



@_attrs_define
class FaqArticleSupportResponse200:
    """ 
        Attributes:
            success (bool):
            data (list[FaqArticleResource]):
     """

    success: bool
    data: list[FaqArticleResource]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.faq_article_resource import FaqArticleResource
        success = self.success

        data = []
        for data_item_data in self.data:
            data_item = data_item_data.to_dict()
            data.append(data_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "success": success,
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.faq_article_resource import FaqArticleResource
        d = dict(src_dict)
        success = d.pop("success")

        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            data_item = FaqArticleResource.from_dict(data_item_data)



            data.append(data_item)


        faq_article_support_response_200 = cls(
            success=success,
            data=data,
        )


        faq_article_support_response_200.additional_properties = d
        return faq_article_support_response_200

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
