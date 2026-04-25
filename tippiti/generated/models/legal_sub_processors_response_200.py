from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.legal_sub_processors_response_200_data_item_type_0 import LegalSubProcessorsResponse200DataItemType0
  from ..models.legal_sub_processors_response_200_data_item_type_1 import LegalSubProcessorsResponse200DataItemType1
  from ..models.legal_sub_processors_response_200_data_item_type_2 import LegalSubProcessorsResponse200DataItemType2
  from ..models.legal_sub_processors_response_200_data_item_type_3 import LegalSubProcessorsResponse200DataItemType3
  from ..models.legal_sub_processors_response_200_data_item_type_4 import LegalSubProcessorsResponse200DataItemType4
  from ..models.legal_sub_processors_response_200_data_item_type_5 import LegalSubProcessorsResponse200DataItemType5





T = TypeVar("T", bound="LegalSubProcessorsResponse200")



@_attrs_define
class LegalSubProcessorsResponse200:
    """ 
        Attributes:
            success (bool):
            data (list[LegalSubProcessorsResponse200DataItemType0 | LegalSubProcessorsResponse200DataItemType1 |
                LegalSubProcessorsResponse200DataItemType2 | LegalSubProcessorsResponse200DataItemType3 |
                LegalSubProcessorsResponse200DataItemType4 | LegalSubProcessorsResponse200DataItemType5]):
     """

    success: bool
    data: list[LegalSubProcessorsResponse200DataItemType0 | LegalSubProcessorsResponse200DataItemType1 | LegalSubProcessorsResponse200DataItemType2 | LegalSubProcessorsResponse200DataItemType3 | LegalSubProcessorsResponse200DataItemType4 | LegalSubProcessorsResponse200DataItemType5]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.legal_sub_processors_response_200_data_item_type_0 import LegalSubProcessorsResponse200DataItemType0
        from ..models.legal_sub_processors_response_200_data_item_type_1 import LegalSubProcessorsResponse200DataItemType1
        from ..models.legal_sub_processors_response_200_data_item_type_2 import LegalSubProcessorsResponse200DataItemType2
        from ..models.legal_sub_processors_response_200_data_item_type_3 import LegalSubProcessorsResponse200DataItemType3
        from ..models.legal_sub_processors_response_200_data_item_type_4 import LegalSubProcessorsResponse200DataItemType4
        from ..models.legal_sub_processors_response_200_data_item_type_5 import LegalSubProcessorsResponse200DataItemType5
        success = self.success

        data = []
        for data_item_data in self.data:
            data_item: dict[str, Any]
            if isinstance(data_item_data, LegalSubProcessorsResponse200DataItemType0):
                data_item = data_item_data.to_dict()
            elif isinstance(data_item_data, LegalSubProcessorsResponse200DataItemType1):
                data_item = data_item_data.to_dict()
            elif isinstance(data_item_data, LegalSubProcessorsResponse200DataItemType2):
                data_item = data_item_data.to_dict()
            elif isinstance(data_item_data, LegalSubProcessorsResponse200DataItemType3):
                data_item = data_item_data.to_dict()
            elif isinstance(data_item_data, LegalSubProcessorsResponse200DataItemType4):
                data_item = data_item_data.to_dict()
            else:
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
        from ..models.legal_sub_processors_response_200_data_item_type_0 import LegalSubProcessorsResponse200DataItemType0
        from ..models.legal_sub_processors_response_200_data_item_type_1 import LegalSubProcessorsResponse200DataItemType1
        from ..models.legal_sub_processors_response_200_data_item_type_2 import LegalSubProcessorsResponse200DataItemType2
        from ..models.legal_sub_processors_response_200_data_item_type_3 import LegalSubProcessorsResponse200DataItemType3
        from ..models.legal_sub_processors_response_200_data_item_type_4 import LegalSubProcessorsResponse200DataItemType4
        from ..models.legal_sub_processors_response_200_data_item_type_5 import LegalSubProcessorsResponse200DataItemType5
        d = dict(src_dict)
        success = d.pop("success")

        data = []
        _data = d.pop("data")
        for data_item_data in (_data):
            def _parse_data_item(data: object) -> LegalSubProcessorsResponse200DataItemType0 | LegalSubProcessorsResponse200DataItemType1 | LegalSubProcessorsResponse200DataItemType2 | LegalSubProcessorsResponse200DataItemType3 | LegalSubProcessorsResponse200DataItemType4 | LegalSubProcessorsResponse200DataItemType5:
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_0 = LegalSubProcessorsResponse200DataItemType0.from_dict(data)



                    return data_item_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_1 = LegalSubProcessorsResponse200DataItemType1.from_dict(data)



                    return data_item_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_2 = LegalSubProcessorsResponse200DataItemType2.from_dict(data)



                    return data_item_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_3 = LegalSubProcessorsResponse200DataItemType3.from_dict(data)



                    return data_item_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    data_item_type_4 = LegalSubProcessorsResponse200DataItemType4.from_dict(data)



                    return data_item_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                data_item_type_5 = LegalSubProcessorsResponse200DataItemType5.from_dict(data)



                return data_item_type_5

            data_item = _parse_data_item(data_item_data)

            data.append(data_item)


        legal_sub_processors_response_200 = cls(
            success=success,
            data=data,
        )


        legal_sub_processors_response_200.additional_properties = d
        return legal_sub_processors_response_200

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
