from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.dictation_ai_log_resource_result_type_1 import DictationAiLogResourceResultType1
from ..models.dictation_ai_log_resource_result_type_2_type_1 import DictationAiLogResourceResultType2Type1
from ..models.dictation_ai_log_resource_result_type_3_type_1 import DictationAiLogResourceResultType3Type1
from typing import cast






T = TypeVar("T", bound="DictationAiLogResource")



@_attrs_define
class DictationAiLogResource:
    """ 
        Attributes:
            id (str):  Example: aid-xyz12345.
            dictation_id (str):  Example: aid-xyz12345.
            step_name (str):
            step_order (int):
            status (str):
            result (DictationAiLogResourceResultType1 | DictationAiLogResourceResultType2Type1 |
                DictationAiLogResourceResultType3Type1 | None):
            duration_ms (int):
            created_at (str):
     """

    id: str
    dictation_id: str
    step_name: str
    step_order: int
    status: str
    result: DictationAiLogResourceResultType1 | DictationAiLogResourceResultType2Type1 | DictationAiLogResourceResultType3Type1 | None
    duration_ms: int
    created_at: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        id = self.id

        dictation_id = self.dictation_id

        step_name = self.step_name

        step_order = self.step_order

        status = self.status

        result: None | str
        if isinstance(self.result, DictationAiLogResourceResultType1):
            result = self.result.value
        elif isinstance(self.result, DictationAiLogResourceResultType2Type1):
            result = self.result.value
        elif isinstance(self.result, DictationAiLogResourceResultType3Type1):
            result = self.result.value
        else:
            result = self.result

        duration_ms = self.duration_ms

        created_at = self.created_at


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "dictation_id": dictation_id,
            "step_name": step_name,
            "step_order": step_order,
            "status": status,
            "result": result,
            "duration_ms": duration_ms,
            "created_at": created_at,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        dictation_id = d.pop("dictation_id")

        step_name = d.pop("step_name")

        step_order = d.pop("step_order")

        status = d.pop("status")

        def _parse_result(data: object) -> DictationAiLogResourceResultType1 | DictationAiLogResourceResultType2Type1 | DictationAiLogResourceResultType3Type1 | None:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                result_type_1 = DictationAiLogResourceResultType1(data)



                return result_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                result_type_2_type_1 = DictationAiLogResourceResultType2Type1(data)



                return result_type_2_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            try:
                if not isinstance(data, str):
                    raise TypeError()
                result_type_3_type_1 = DictationAiLogResourceResultType3Type1(data)



                return result_type_3_type_1
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(DictationAiLogResourceResultType1 | DictationAiLogResourceResultType2Type1 | DictationAiLogResourceResultType3Type1 | None, data)

        result = _parse_result(d.pop("result"))


        duration_ms = d.pop("duration_ms")

        created_at = d.pop("created_at")

        dictation_ai_log_resource = cls(
            id=id,
            dictation_id=dictation_id,
            step_name=step_name,
            step_order=step_order,
            status=status,
            result=result,
            duration_ms=duration_ms,
            created_at=created_at,
        )


        dictation_ai_log_resource.additional_properties = d
        return dictation_ai_log_resource

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
