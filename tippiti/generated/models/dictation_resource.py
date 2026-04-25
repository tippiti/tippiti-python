from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.dictation_ai_log_resource import DictationAiLogResource
  from ..models.dictation_note_resource import DictationNoteResource
  from ..models.dictation_version_resource import DictationVersionResource
  from ..models.instruction_set import InstructionSet





T = TypeVar("T", bound="DictationResource")



@_attrs_define
class DictationResource:
    """ 
        Attributes:
            id (str):  Example: aid-xyz12345.
            title (None | str):
            client_name (None | str):
            status (str):
            status_detail (str):
            comment (None | str):
            character_count (int):
            audio_duration (int):
            user_cost (str):
            is_billed (bool):
            is_archived (bool):
            archived_at (str):
            billed_at (str):
            billed_price_per_1k_chars (None | str):
            instruction_set_id (str):  Example: aid-xyz12345.
            started_at (str):
            completed_at (str):
            error_message (None | str):
            created_at (str):
            updated_at (str):
            shares_count (str | Unset):
            notes_count (str | Unset):
            important_notes_count (str | Unset):
            notes_with_attachments_count (str | Unset):
            notes (list[DictationNoteResource] | Unset):
            folders (list[str] | Unset):
            shared_with (list[str] | Unset):
            versions (list[DictationVersionResource] | Unset):
            ai_logs (list[DictationAiLogResource] | Unset):
            instruction_set (InstructionSet | Unset):
            admin_url (str | Unset):
     """

    id: str
    title: None | str
    client_name: None | str
    status: str
    status_detail: str
    comment: None | str
    character_count: int
    audio_duration: int
    user_cost: str
    is_billed: bool
    is_archived: bool
    archived_at: str
    billed_at: str
    billed_price_per_1k_chars: None | str
    instruction_set_id: str
    started_at: str
    completed_at: str
    error_message: None | str
    created_at: str
    updated_at: str
    shares_count: str | Unset = UNSET
    notes_count: str | Unset = UNSET
    important_notes_count: str | Unset = UNSET
    notes_with_attachments_count: str | Unset = UNSET
    notes: list[DictationNoteResource] | Unset = UNSET
    folders: list[str] | Unset = UNSET
    shared_with: list[str] | Unset = UNSET
    versions: list[DictationVersionResource] | Unset = UNSET
    ai_logs: list[DictationAiLogResource] | Unset = UNSET
    instruction_set: InstructionSet | Unset = UNSET
    admin_url: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.dictation_ai_log_resource import DictationAiLogResource
        from ..models.dictation_note_resource import DictationNoteResource
        from ..models.dictation_version_resource import DictationVersionResource
        from ..models.instruction_set import InstructionSet
        id = self.id

        title: None | str
        title = self.title

        client_name: None | str
        client_name = self.client_name

        status = self.status

        status_detail = self.status_detail

        comment: None | str
        comment = self.comment

        character_count = self.character_count

        audio_duration = self.audio_duration

        user_cost = self.user_cost

        is_billed = self.is_billed

        is_archived = self.is_archived

        archived_at = self.archived_at

        billed_at = self.billed_at

        billed_price_per_1k_chars: None | str
        billed_price_per_1k_chars = self.billed_price_per_1k_chars

        instruction_set_id = self.instruction_set_id

        started_at = self.started_at

        completed_at = self.completed_at

        error_message: None | str
        error_message = self.error_message

        created_at = self.created_at

        updated_at = self.updated_at

        shares_count = self.shares_count

        notes_count = self.notes_count

        important_notes_count = self.important_notes_count

        notes_with_attachments_count = self.notes_with_attachments_count

        notes: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.notes, Unset):
            notes = []
            for notes_item_data in self.notes:
                notes_item = notes_item_data.to_dict()
                notes.append(notes_item)



        folders: list[str] | Unset = UNSET
        if not isinstance(self.folders, Unset):
            folders = self.folders



        shared_with: list[str] | Unset = UNSET
        if not isinstance(self.shared_with, Unset):
            shared_with = self.shared_with



        versions: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.versions, Unset):
            versions = []
            for versions_item_data in self.versions:
                versions_item = versions_item_data.to_dict()
                versions.append(versions_item)



        ai_logs: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.ai_logs, Unset):
            ai_logs = []
            for ai_logs_item_data in self.ai_logs:
                ai_logs_item = ai_logs_item_data.to_dict()
                ai_logs.append(ai_logs_item)



        instruction_set: dict[str, Any] | Unset = UNSET
        if not isinstance(self.instruction_set, Unset):
            instruction_set = self.instruction_set.to_dict()

        admin_url = self.admin_url


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "id": id,
            "title": title,
            "client_name": client_name,
            "status": status,
            "status_detail": status_detail,
            "comment": comment,
            "character_count": character_count,
            "audio_duration": audio_duration,
            "user_cost": user_cost,
            "is_billed": is_billed,
            "is_archived": is_archived,
            "archived_at": archived_at,
            "billed_at": billed_at,
            "billed_price_per_1k_chars": billed_price_per_1k_chars,
            "instruction_set_id": instruction_set_id,
            "started_at": started_at,
            "completed_at": completed_at,
            "error_message": error_message,
            "created_at": created_at,
            "updated_at": updated_at,
        })
        if shares_count is not UNSET:
            field_dict["shares_count"] = shares_count
        if notes_count is not UNSET:
            field_dict["notes_count"] = notes_count
        if important_notes_count is not UNSET:
            field_dict["important_notes_count"] = important_notes_count
        if notes_with_attachments_count is not UNSET:
            field_dict["notes_with_attachments_count"] = notes_with_attachments_count
        if notes is not UNSET:
            field_dict["notes"] = notes
        if folders is not UNSET:
            field_dict["folders"] = folders
        if shared_with is not UNSET:
            field_dict["shared_with"] = shared_with
        if versions is not UNSET:
            field_dict["versions"] = versions
        if ai_logs is not UNSET:
            field_dict["ai_logs"] = ai_logs
        if instruction_set is not UNSET:
            field_dict["instruction_set"] = instruction_set
        if admin_url is not UNSET:
            field_dict["admin_url"] = admin_url

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.dictation_ai_log_resource import DictationAiLogResource
        from ..models.dictation_note_resource import DictationNoteResource
        from ..models.dictation_version_resource import DictationVersionResource
        from ..models.instruction_set import InstructionSet
        d = dict(src_dict)
        id = d.pop("id")

        def _parse_title(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        title = _parse_title(d.pop("title"))


        def _parse_client_name(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        client_name = _parse_client_name(d.pop("client_name"))


        status = d.pop("status")

        status_detail = d.pop("status_detail")

        def _parse_comment(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        comment = _parse_comment(d.pop("comment"))


        character_count = d.pop("character_count")

        audio_duration = d.pop("audio_duration")

        user_cost = d.pop("user_cost")

        is_billed = d.pop("is_billed")

        is_archived = d.pop("is_archived")

        archived_at = d.pop("archived_at")

        billed_at = d.pop("billed_at")

        def _parse_billed_price_per_1k_chars(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        billed_price_per_1k_chars = _parse_billed_price_per_1k_chars(d.pop("billed_price_per_1k_chars"))


        instruction_set_id = d.pop("instruction_set_id")

        started_at = d.pop("started_at")

        completed_at = d.pop("completed_at")

        def _parse_error_message(data: object) -> None | str:
            if data is None:
                return data
            return cast(None | str, data)

        error_message = _parse_error_message(d.pop("error_message"))


        created_at = d.pop("created_at")

        updated_at = d.pop("updated_at")

        shares_count = d.pop("shares_count", UNSET)

        notes_count = d.pop("notes_count", UNSET)

        important_notes_count = d.pop("important_notes_count", UNSET)

        notes_with_attachments_count = d.pop("notes_with_attachments_count", UNSET)

        _notes = d.pop("notes", UNSET)
        notes: list[DictationNoteResource] | Unset = UNSET
        if _notes is not UNSET:
            notes = []
            for notes_item_data in _notes:
                notes_item = DictationNoteResource.from_dict(notes_item_data)



                notes.append(notes_item)


        folders = cast(list[str], d.pop("folders", UNSET))


        shared_with = cast(list[str], d.pop("shared_with", UNSET))


        _versions = d.pop("versions", UNSET)
        versions: list[DictationVersionResource] | Unset = UNSET
        if _versions is not UNSET:
            versions = []
            for versions_item_data in _versions:
                versions_item = DictationVersionResource.from_dict(versions_item_data)



                versions.append(versions_item)


        _ai_logs = d.pop("ai_logs", UNSET)
        ai_logs: list[DictationAiLogResource] | Unset = UNSET
        if _ai_logs is not UNSET:
            ai_logs = []
            for ai_logs_item_data in _ai_logs:
                ai_logs_item = DictationAiLogResource.from_dict(ai_logs_item_data)



                ai_logs.append(ai_logs_item)


        _instruction_set = d.pop("instruction_set", UNSET)
        instruction_set: InstructionSet | Unset
        if isinstance(_instruction_set,  Unset):
            instruction_set = UNSET
        else:
            instruction_set = InstructionSet.from_dict(_instruction_set)




        admin_url = d.pop("admin_url", UNSET)

        dictation_resource = cls(
            id=id,
            title=title,
            client_name=client_name,
            status=status,
            status_detail=status_detail,
            comment=comment,
            character_count=character_count,
            audio_duration=audio_duration,
            user_cost=user_cost,
            is_billed=is_billed,
            is_archived=is_archived,
            archived_at=archived_at,
            billed_at=billed_at,
            billed_price_per_1k_chars=billed_price_per_1k_chars,
            instruction_set_id=instruction_set_id,
            started_at=started_at,
            completed_at=completed_at,
            error_message=error_message,
            created_at=created_at,
            updated_at=updated_at,
            shares_count=shares_count,
            notes_count=notes_count,
            important_notes_count=important_notes_count,
            notes_with_attachments_count=notes_with_attachments_count,
            notes=notes,
            folders=folders,
            shared_with=shared_with,
            versions=versions,
            ai_logs=ai_logs,
            instruction_set=instruction_set,
            admin_url=admin_url,
        )


        dictation_resource.additional_properties = d
        return dictation_resource

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
