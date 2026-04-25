from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="AffiliateChartDataResponse200Data")



@_attrs_define
class AffiliateChartDataResponse200Data:
    """ 
        Attributes:
            labels (list[str]):
            total_clicks (list[int]):
            unique_clicks (list[int]):
            registrations (list[int]):
            commissions (list[float]):
     """

    labels: list[str]
    total_clicks: list[int]
    unique_clicks: list[int]
    registrations: list[int]
    commissions: list[float]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        labels = self.labels



        total_clicks = self.total_clicks



        unique_clicks = self.unique_clicks



        registrations = self.registrations



        commissions = self.commissions




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "labels": labels,
            "total_clicks": total_clicks,
            "unique_clicks": unique_clicks,
            "registrations": registrations,
            "commissions": commissions,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        labels = cast(list[str], d.pop("labels"))


        total_clicks = cast(list[int], d.pop("total_clicks"))


        unique_clicks = cast(list[int], d.pop("unique_clicks"))


        registrations = cast(list[int], d.pop("registrations"))


        commissions = cast(list[float], d.pop("commissions"))


        affiliate_chart_data_response_200_data = cls(
            labels=labels,
            total_clicks=total_clicks,
            unique_clicks=unique_clicks,
            registrations=registrations,
            commissions=commissions,
        )


        affiliate_chart_data_response_200_data.additional_properties = d
        return affiliate_chart_data_response_200_data

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
