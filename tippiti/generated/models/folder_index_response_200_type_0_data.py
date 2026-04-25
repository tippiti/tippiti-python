from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.folder_resource import FolderResource





T = TypeVar("T", bound="FolderIndexResponse200Type0Data")



@_attrs_define
class FolderIndexResponse200Type0Data:
    """ 
        Attributes:
            folders (list[FolderResource]):
            permission_folders (list[FolderResource]):
     """

    folders: list[FolderResource]
    permission_folders: list[FolderResource]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.folder_resource import FolderResource
        folders = []
        for folders_item_data in self.folders:
            folders_item = folders_item_data.to_dict()
            folders.append(folders_item)



        permission_folders = []
        for permission_folders_item_data in self.permission_folders:
            permission_folders_item = permission_folders_item_data.to_dict()
            permission_folders.append(permission_folders_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "folders": folders,
            "permission_folders": permission_folders,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.folder_resource import FolderResource
        d = dict(src_dict)
        folders = []
        _folders = d.pop("folders")
        for folders_item_data in (_folders):
            folders_item = FolderResource.from_dict(folders_item_data)



            folders.append(folders_item)


        permission_folders = []
        _permission_folders = d.pop("permission_folders")
        for permission_folders_item_data in (_permission_folders):
            permission_folders_item = FolderResource.from_dict(permission_folders_item_data)



            permission_folders.append(permission_folders_item)


        folder_index_response_200_type_0_data = cls(
            folders=folders,
            permission_folders=permission_folders,
        )


        folder_index_response_200_type_0_data.additional_properties = d
        return folder_index_response_200_type_0_data

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
