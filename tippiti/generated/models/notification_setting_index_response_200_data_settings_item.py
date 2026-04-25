from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast






T = TypeVar("T", bound="NotificationSettingIndexResponse200DataSettingsItem")



@_attrs_define
class NotificationSettingIndexResponse200DataSettingsItem:
    """ 
        Attributes:
            key (None | str):
            label (None | str):
            description (None | str):
            enabled (bool | None | str):
            force_enabled (bool):
            send_to_account (bool):
            additional_recipients (list[str]):
            hideable_fields (list[Any]):
            field_visibility (str):
            custom_options (list[Any]):
            options (str):
     """

    key: None | str
    label: None | str
    description: None | str
    enabled: bool | None | str
    force_enabled: bool
    send_to_account: bool
    additional_recipients: list[str]
    hideable_fields: list[Any]
    field_visibility: str
    custom_options: list[Any]
    options: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        key: None | str
        key = self.key

        label: None | str
        label = self.label

        description: None | str
        description = self.description

        enabled: bool | None | str
        enabled = self.enabled

        force_enabled = self.force_enabled

        send_to_account = self.send_to_account

        additional_recipients = self.additional_recipients



        hideable_fields = self.hideable_fields



        field_visibility = self.field_visibility

        custom_options = self.custom_options



        options = self.options


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "key": key,
            "label": label,
            "description": description,
            "enabled": enabled,
            "force_enabled": force_enabled,
            "send_to_account": send_to_account,
            "additional_recipients": additional_recipients,
            "hideable_fields": hideable_fields,
            "field_visibility": field_visibility,
            "custom_options": custom_options,
            "options": options,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        def _parse_key(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        key = _parse_key(d.pop("key"))


        def _parse_label(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        label = _parse_label(d.pop("label"))


        def _parse_description(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        description = _parse_description(d.pop("description"))


        def _parse_enabled(data: object) -> bool | None | str:
            if data is None:
                return data
            return cast(bool | None | str, data)

        enabled = _parse_enabled(d.pop("enabled"))


        force_enabled = d.pop("force_enabled")

        send_to_account = d.pop("send_to_account")

        additional_recipients = cast(list[str], d.pop("additional_recipients"))


        hideable_fields = cast(list[Any], d.pop("hideable_fields"))


        field_visibility = d.pop("field_visibility")

        custom_options = cast(list[Any], d.pop("custom_options"))


        options = d.pop("options")

        notification_setting_index_response_200_data_settings_item = cls(
            key=key,
            label=label,
            description=description,
            enabled=enabled,
            force_enabled=force_enabled,
            send_to_account=send_to_account,
            additional_recipients=additional_recipients,
            hideable_fields=hideable_fields,
            field_visibility=field_visibility,
            custom_options=custom_options,
            options=options,
        )


        notification_setting_index_response_200_data_settings_item.additional_properties = d
        return notification_setting_index_response_200_data_settings_item

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
