from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.sub_user_resource import SubUserResource





T = TypeVar("T", bound="SubUserUpdateResponse200")



@_attrs_define
class SubUserUpdateResponse200:
    """ 
        Attributes:
            success (bool):
            data (SubUserResource):
     """

    success: bool
    data: SubUserResource
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.sub_user_resource import SubUserResource
        success = self.success

        data = self.data.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "success": success,
            "data": data,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.sub_user_resource import SubUserResource
        d = dict(src_dict)
        success = d.pop("success")

        data = SubUserResource.from_dict(d.pop("data"))




        sub_user_update_response_200 = cls(
            success=success,
            data=data,
        )


        sub_user_update_response_200.additional_properties = d
        return sub_user_update_response_200

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
