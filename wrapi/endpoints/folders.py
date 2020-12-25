from __future__ import annotations

from datetime import date
from typing import (
    Literal,
    Optional,
    Sequence,
)

from pydantic import Field
from pydantic.types import StrictBool

from ..api import (
    BodyParams,
    EndpointData,
    Methods,
    WrApiQueryParams,
)
from ..types_.endpoint import BaseEndpoint
from ..types_.enums import BillingType
from ..types_.inputs import (
    CustomField,
    CustomFieldFilter,
    DateRange,
    FolderOptionalFields,
    Metadata,
    Project,
    TaskReschedulingMode,
)
from ..types_.scalar import (
    ContactId,
    CustomFieldId,
    FolderId,
    SpaceId,
)


class _FoldersTreeBase(BaseEndpoint):
    permalink: Optional[str]
    descendants: Optional[StrictBool]
    project: Optional[StrictBool]
    custom_field: Optional[CustomFieldFilter]
    updated_date: Optional[DateRange]
    contract_types: Optional[BillingType]
    metadata: Optional[Metadata]
    fields_: Optional[Sequence[FolderOptionalFields]] = Field(None, alias="fields")

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url=self._url,
            query_params=self._query_params,
        )

    @property
    def _url(self) -> str:
        raise NotImplementedError()

    @property
    def _query_params(self) -> WrApiQueryParams:
        params = WrApiQueryParams()

        if self.permalink:
            params["permalink"] = self.permalink

        if self.metadata:
            params["metadata"] = self._convert_input(self.metadata)

        if self.descendants is not None:
            params["descendants"] = self._convert_bool(self.descendants)

        if self.fields_:
            params["fields"] = self._convert_seq(self.fields_)

        if self.custom_field:
            params["customField"] = self._convert_input(self.custom_field)

        if self.updated_date:
            params["updatedDate"] = self._convert_input(self.updated_date)

        if self.contract_types:
            params["contractTypes"] = self.contract_types.value

        return params


class FoldersTree(_FoldersTreeBase):
    deleted: Optional[StrictBool]

    @property
    def _url(self) -> str:
        return "/folders"

    @property
    def _query_params(self) -> WrApiQueryParams:
        qp = super()._query_params

        if self.deleted is not None:
            qp["deleted"] = self._convert_bool(self.deleted)

        return qp


class FoldersTreeInFolder(_FoldersTreeBase):
    folder_id: FolderId

    @property
    def _url(self) -> str:
        return f"/folders/{self.folder_id}/folders"


class FoldersTreeInSpace(_FoldersTreeBase):
    space_id: SpaceId
    deleted: Optional[StrictBool]

    @property
    def _url(self) -> str:
        return f"/spaces/{self.space_id}/folders"

    @property
    def _query_params(self) -> WrApiQueryParams:
        qp = super()._query_params

        if self.deleted is not None:
            qp["deleted"] = self._convert_bool(self.deleted)

        return qp


class FoldersByIds(BaseEndpoint):
    folder_ids: Sequence[FolderId] = Field(..., max_length=100)
    fields_: Optional[Sequence[FolderOptionalFields]] = Field(None, alias="fields")

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="GET",
            url=f"/folders/{','.join(self.folder_ids)}",
            query_params=self._query_params,
        )

    @property
    def _query_params(self) -> WrApiQueryParams:
        params = WrApiQueryParams()

        if self.fields_:
            params["fields"] = self._convert_seq(self.fields_)

        return params


class _CreateOrModifyFolder(BaseEndpoint):
    folder_id: FolderId
    description: Optional[str]
    metadata: Optional[Sequence[Metadata]]
    custom_fields: Optional[Sequence[CustomField]]
    custom_columns: Optional[Sequence[CustomFieldId]]
    project: Optional[Project]
    fields_: Optional[Sequence[Literal[FolderOptionalFields.CONTRACT_TYPE]]] = Field(None, alias="fields")

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method=self._method,
            url=self._url,
            body_params=self._body_params,
        )

    @property
    def _method(self) -> Methods:
        raise NotImplementedError()

    @property
    def _url(self) -> str:
        raise NotImplementedError()

    @property
    def _body_params(self) -> BodyParams:
        params = {}

        if self.description is not None:
            params["description"] = self.description

        if self.metadata:
            params["metadata"] = self._convert_input_seq(self.metadata)

        if self.custom_fields is not None:
            params["customFields"] = self._convert_input_seq(self.custom_fields)

        if self.custom_columns is not None:
            params["customColumns"] = self._convert_seq(self.custom_columns)

        if self.project:
            params["project"] = self._convert_input(self.project)

        if self.fields_:
            params["fields"] = self._convert_seq(self.fields_)

        return params


class CreateFolder(_CreateOrModifyFolder):
    title: str
    shareds: Optional[Sequence[ContactId]]

    @property
    def _method(self) -> Methods:
        return "POST"

    @property
    def _url(self) -> str:
        return f"/folders/{self.folder_id}/folders"

    @property
    def _body_params(self) -> BodyParams:
        params = super()._body_params
        params["title"] = self.title

        if self.shareds is not None:
            params["shareds"] = self._convert_seq(self.shareds)

        return params


class ModifyFolder(_CreateOrModifyFolder):
    title: Optional[str]
    add_parents: Optional[Sequence[FolderId]]
    remove_parents: Optional[Sequence[FolderId]]
    add_shareds: Optional[Sequence[ContactId]]
    remove_shareds: Optional[Sequence[ContactId]]
    restore: Optional[StrictBool]

    @property
    def _method(self) -> Methods:
        return "PUT"

    @property
    def _url(self) -> str:
        return f"/folders/{self.folder_id}"

    @property
    def _body_params(self) -> BodyParams:
        params = super()._body_params

        if self.title:
            params["title"] = self.title

        if self.add_parents:
            params["addParents"] = self._convert_seq(self.add_parents)

        if self.remove_parents:
            params["removeParents"] = self._convert_seq(self.remove_parents)

        if self.add_shareds:
            params["addShareds"] = self._convert_seq(self.add_shareds)

        if self.remove_shareds:
            params["removeShareds"] = self._convert_seq(self.remove_shareds)

        if self.restore is not None:
            params["restore"] = self._convert_bool(self.restore)

        return params


class _BaseCopyFolder(BaseEndpoint):
    folder_id: FolderId
    parent: FolderId
    title: str
    title_prefix: Optional[str]
    copy_descriptions: Optional[StrictBool]
    copy_responsibles: Optional[StrictBool]
    add_responsibles: Optional[Sequence[ContactId]]
    remove_responsibles: Optional[Sequence[ContactId]]
    copy_custom_fields: Optional[StrictBool]
    copy_custom_statuses: Optional[StrictBool]
    copy_statuses: Optional[StrictBool]
    copy_parents: Optional[StrictBool]
    reschedule_date: Optional[date]
    reschedule_mode: Optional[TaskReschedulingMode]
    entry_limit: Optional[int] = Field(..., gt=0, le=250)

    @property
    def _body_params(self) -> BodyParams:
        body_params: BodyParams = {"parent": self.parent, "title": self.title}

        if self.title_prefix is not None:
            body_params["titlePrefix"] = self.title_prefix

        if self.copy_descriptions is not None:
            body_params["copyDescriptions"] = self._convert_bool(self.copy_descriptions)

        if self.copy_responsibles is not None:
            body_params["copyResponsibles"] = self._convert_bool(self.copy_responsibles)

        if self.add_responsibles is not None:
            body_params["addResponsibles"] = self._convert_seq(self.add_responsibles)

        if self.remove_responsibles is not None:
            body_params["removeResponsibles"] = self._convert_seq(self.remove_responsibles)

        if self.copy_custom_fields is not None:
            body_params["copyCustomFields"] = self._convert_bool(self.copy_custom_fields)

        if self.copy_custom_statuses is not None:
            body_params["copyCustomStatuses"] = self._convert_bool(self.copy_custom_statuses)

        if self.copy_statuses is not None:
            body_params["copyStatuses"] = self._convert_bool(self.copy_statuses)

        if self.copy_parents is not None:
            body_params["copyParents"] = self._convert_bool(self.copy_parents)

        if self.reschedule_date:
            body_params["rescheduleDate"] = self.reschedule_date.isoformat()

        if self.reschedule_mode:
            body_params["rescheduleMode"] = self.reschedule_mode.value

        if self.entry_limit is not None:
            body_params["entryLimit"] = str(self.entry_limit)

        return body_params


class CopyFolder(_BaseCopyFolder):
    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="POST",
            url=f"/copy_folder/{self.folder_id}",
            body_params=self._body_params,
        )


class AsyncCopyFolder(_BaseCopyFolder):
    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="POST",
            url=f"/copy_folder_async/{self.folder_id}",
            body_params=self._body_params,
        )


class DeleteFolder(BaseEndpoint):
    folder_id: FolderId

    @property
    def endpoint_data(self) -> EndpointData:
        return EndpointData(
            method="DELETE",
            url=f"/folders/{self.folder_id}",
        )
