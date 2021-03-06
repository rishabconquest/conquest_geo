# coding: utf-8

# flake8: noqa
"""
    Conquest API v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


# from __future__ import absolute_import

# import models into model package
from ..models.conquest_api_account_id import ConquestApiAccountID
from ..models.conquest_api_account_permissions import ConquestApiAccountPermissions
from ..models.conquest_api_account_type import ConquestApiAccountType
from ..models.conquest_api_action_completion_details import ConquestApiActionCompletionDetails
from ..models.conquest_api_action_completion_options import ConquestApiActionCompletionOptions
from ..models.conquest_api_action_entity import ConquestApiActionEntity
from ..models.conquest_api_action_record import ConquestApiActionRecord
from ..models.conquest_api_action_record_change_set import ConquestApiActionRecordChangeSet
from ..models.conquest_api_action_type import ConquestApiActionType
from ..models.conquest_api_add_diary_result import ConquestApiAddDiaryResult
from ..models.conquest_api_add_document_command import ConquestApiAddDocumentCommand
from ..models.conquest_api_add_document_result import ConquestApiAddDocumentResult
from ..models.conquest_api_add_document_results import ConquestApiAddDocumentResults
from ..models.conquest_api_add_geo_update_command import ConquestApiAddGeoUpdateCommand
from ..models.conquest_api_add_new_csv_import_command import ConquestApiAddNewCsvImportCommand
from ..models.conquest_api_add_new_geo_package_import_command import ConquestApiAddNewGeoPackageImportCommand
from ..models.conquest_api_any_value import ConquestApiAnyValue
from ..models.conquest_api_apply_standard_action_command import ConquestApiApplyStandardActionCommand
from ..models.conquest_api_apply_standard_action_overwrite_options import ConquestApiApplyStandardActionOverwriteOptions
from ..models.conquest_api_asset_entity import ConquestApiAssetEntity
from ..models.conquest_api_asset_inspection_entity import ConquestApiAssetInspectionEntity
from ..models.conquest_api_asset_inspection_record import ConquestApiAssetInspectionRecord
from ..models.conquest_api_asset_inspection_record_change_set import ConquestApiAssetInspectionRecordChangeSet
from ..models.conquest_api_asset_record import ConquestApiAssetRecord
from ..models.conquest_api_asset_record_change_set import ConquestApiAssetRecordChangeSet
from ..models.conquest_api_asset_type_entity import ConquestApiAssetTypeEntity
from ..models.conquest_api_asset_type_record import ConquestApiAssetTypeRecord
from ..models.conquest_api_attribute_set import ConquestApiAttributeSet
from ..models.conquest_api_attribute_set_dimension_value import ConquestApiAttributeSetDimensionValue
from ..models.conquest_api_attribute_set_field import ConquestApiAttributeSetField
from ..models.conquest_api_attribute_set_field_names import ConquestApiAttributeSetFieldNames
from ..models.conquest_api_attribute_set_hierarchy_value import ConquestApiAttributeSetHierarchyValue
from ..models.conquest_api_attribute_set_list_value import ConquestApiAttributeSetListValue
from ..models.conquest_api_attribute_set_weighted_value import ConquestApiAttributeSetWeightedValue
from ..models.conquest_api_attribute_sets_result import ConquestApiAttributeSetsResult
from ..models.conquest_api_auth_token_response import ConquestApiAuthTokenResponse
from ..models.conquest_api_base_layer_configuration import ConquestApiBaseLayerConfiguration
from ..models.conquest_api_calculate_defect_response_date_parameters import ConquestApiCalculateDefectResponseDateParameters
from ..models.conquest_api_calculate_defect_response_date_request import ConquestApiCalculateDefectResponseDateRequest
from ..models.conquest_api_calculate_defect_response_date_response import ConquestApiCalculateDefectResponseDateResponse
from ..models.conquest_api_calculate_defect_response_date_result import ConquestApiCalculateDefectResponseDateResult
from ..models.conquest_api_calendar_duration_unit import ConquestApiCalendarDurationUnit
from ..models.conquest_api_change_asset_type_command import ConquestApiChangeAssetTypeCommand
from ..models.conquest_api_change_document_content_command import ConquestApiChangeDocumentContentCommand
from ..models.conquest_api_change_set_result import ConquestApiChangeSetResult
from ..models.conquest_api_code_list import ConquestApiCodeList
from ..models.conquest_api_code_list_item import ConquestApiCodeListItem
from ..models.conquest_api_code_list_type import ConquestApiCodeListType
from ..models.conquest_api_compare_operator import ConquestApiCompareOperator
from ..models.conquest_api_complete_action_command import ConquestApiCompleteActionCommand
from ..models.conquest_api_complete_action_result import ConquestApiCompleteActionResult
from ..models.conquest_api_complete_defect_command import ConquestApiCompleteDefectCommand
from ..models.conquest_api_condition_type import ConquestApiConditionType
from ..models.conquest_api_config_azure_search_address_api import ConquestApiConfigAzureSearchAddressApi
from ..models.conquest_api_config_blob_store import ConquestApiConfigBlobStore
from ..models.conquest_api_config_blob_store_mode import ConquestApiConfigBlobStoreMode
from ..models.conquest_api_config_conquest_development_staff_configuration_options import ConquestApiConfigConquestDevelopmentStaffConfigurationOptions
from ..models.conquest_api_config_database_connection import ConquestApiConfigDatabaseConnection
from ..models.conquest_api_config_event_source import ConquestApiConfigEventSource
from ..models.conquest_api_config_leaflet_map_connection import ConquestApiConfigLeafletMapConnection
from ..models.conquest_api_config_logging import ConquestApiConfigLogging
from ..models.conquest_api_config_services_client_credentials import ConquestApiConfigServicesClientCredentials
from ..models.conquest_api_context_descriptor import ConquestApiContextDescriptor
from ..models.conquest_api_contractor_email_metadata import ConquestApiContractorEmailMetadata
from ..models.conquest_api_copy_asset_command import ConquestApiCopyAssetCommand
from ..models.conquest_api_copy_asset_result import ConquestApiCopyAssetResult
from ..models.conquest_api_copy_asset_type_result import ConquestApiCopyAssetTypeResult
from ..models.conquest_api_copy_down_field_definition import ConquestApiCopyDownFieldDefinition
from ..models.conquest_api_cost_type import ConquestApiCostType
from ..models.conquest_api_create_action_for_asset_command import ConquestApiCreateActionForAssetCommand
from ..models.conquest_api_create_action_for_defect_command import ConquestApiCreateActionForDefectCommand
from ..models.conquest_api_create_asset_command import ConquestApiCreateAssetCommand
from ..models.conquest_api_create_asset_inspection_command import ConquestApiCreateAssetInspectionCommand
from ..models.conquest_api_create_defect_for_asset_command import ConquestApiCreateDefectForAssetCommand
from ..models.conquest_api_create_defect_for_asset_inspection_command import ConquestApiCreateDefectForAssetInspectionCommand
from ..models.conquest_api_create_request_command import ConquestApiCreateRequestCommand
from ..models.conquest_api_create_session_grant_type import ConquestApiCreateSessionGrantType
from ..models.conquest_api_create_session_response import ConquestApiCreateSessionResponse
from ..models.conquest_api_create_succeeding_action_command import ConquestApiCreateSucceedingActionCommand
from ..models.conquest_api_criteria import ConquestApiCriteria
from ..models.conquest_api_criteria_item import ConquestApiCriteriaItem
from ..models.conquest_api_csv_import_state_response import ConquestApiCsvImportStateResponse
from ..models.conquest_api_cyclic_action_completion_process import ConquestApiCyclicActionCompletionProcess
from ..models.conquest_api_database_connection_names_response import ConquestApiDatabaseConnectionNamesResponse
from ..models.conquest_api_decimal import ConquestApiDecimal
from ..models.conquest_api_decimal_value import ConquestApiDecimalValue
from ..models.conquest_api_defect_entity import ConquestApiDefectEntity
from ..models.conquest_api_defect_record import ConquestApiDefectRecord
from ..models.conquest_api_defect_record_change_set import ConquestApiDefectRecordChangeSet
from ..models.conquest_api_delete_action_command import ConquestApiDeleteActionCommand
from ..models.conquest_api_delete_asset_command import ConquestApiDeleteAssetCommand
from ..models.conquest_api_delete_asset_inspection_command import ConquestApiDeleteAssetInspectionCommand
from ..models.conquest_api_delete_defect_command import ConquestApiDeleteDefectCommand
from ..models.conquest_api_delete_request_command import ConquestApiDeleteRequestCommand
from ..models.conquest_api_describe_enumeration_request import ConquestApiDescribeEnumerationRequest
from ..models.conquest_api_describe_enumeration_result import ConquestApiDescribeEnumerationResult
from ..models.conquest_api_disposal_action_completion_process import ConquestApiDisposalActionCompletionProcess
from ..models.conquest_api_document import ConquestApiDocument
from ..models.conquest_api_document_container import ConquestApiDocumentContainer
from ..models.conquest_api_document_migration_work_load import ConquestApiDocumentMigrationWorkLoad
from ..models.conquest_api_document_type_migration_progress import ConquestApiDocumentTypeMigrationProgress
from ..models.conquest_api_document_upload_job_item import ConquestApiDocumentUploadJobItem
from ..models.conquest_api_effective_permission import ConquestApiEffectivePermission
from ..models.conquest_api_enumeration import ConquestApiEnumeration
from ..models.conquest_api_enumeration_item import ConquestApiEnumerationItem
from ..models.conquest_api_enumeration_type import ConquestApiEnumerationType
from ..models.conquest_api_environment_properties import ConquestApiEnvironmentProperties
from ..models.conquest_api_error_response import ConquestApiErrorResponse
from ..models.conquest_api_facility_permission import ConquestApiFacilityPermission
from ..models.conquest_api_fetch_document_migration_items_to_upload_response import ConquestApiFetchDocumentMigrationItemsToUploadResponse
from ..models.conquest_api_field_criterion import ConquestApiFieldCriterion
from ..models.conquest_api_field_criterion_list import ConquestApiFieldCriterionList
from ..models.conquest_api_filter import ConquestApiFilter
from ..models.conquest_api_filter_type import ConquestApiFilterType
from ..models.conquest_api_find_contexts_result import ConquestApiFindContextsResult
from ..models.conquest_api_find_query import ConquestApiFindQuery
from ..models.conquest_api_find_result import ConquestApiFindResult
from ..models.conquest_api_font_style import ConquestApiFontStyle
from ..models.conquest_api_generate_document_link_command import ConquestApiGenerateDocumentLinkCommand
from ..models.conquest_api_generate_document_link_result import ConquestApiGenerateDocumentLinkResult
from ..models.conquest_api_geo_package_description import ConquestApiGeoPackageDescription
from ..models.conquest_api_geo_package_key_column_description_option import ConquestApiGeoPackageKeyColumnDescriptionOption
from ..models.conquest_api_geo_package_table_description import ConquestApiGeoPackageTableDescription
from ..models.conquest_api_geo_package_table_description_options import ConquestApiGeoPackageTableDescriptionOptions
from ..models.conquest_api_geography_data import ConquestApiGeographyData
from ..models.conquest_api_geography_data_value import ConquestApiGeographyDataValue
from ..models.conquest_api_geometry_data import ConquestApiGeometryData
from ..models.conquest_api_geometry_data_value import ConquestApiGeometryDataValue
from ..models.conquest_api_get_action_completion_details_request import ConquestApiGetActionCompletionDetailsRequest
from ..models.conquest_api_get_action_completion_details_response import ConquestApiGetActionCompletionDetailsResponse
from ..models.conquest_api_get_attribute_set_field_names_response import ConquestApiGetAttributeSetFieldNamesResponse
from ..models.conquest_api_get_azure_search_for_address_api_end_point_result import ConquestApiGetAzureSearchForAddressApiEndPointResult
from ..models.conquest_api_get_base_layer_configurations_result import ConquestApiGetBaseLayerConfigurationsResult
from ..models.conquest_api_get_code_lists_query import ConquestApiGetCodeListsQuery
from ..models.conquest_api_get_code_lists_result import ConquestApiGetCodeListsResult
from ..models.conquest_api_get_copy_down_field_names_response import ConquestApiGetCopyDownFieldNamesResponse
from ..models.conquest_api_get_document_location_result import ConquestApiGetDocumentLocationResult
from ..models.conquest_api_get_documents_query import ConquestApiGetDocumentsQuery
from ..models.conquest_api_get_documents_result import ConquestApiGetDocumentsResult
from ..models.conquest_api_get_history_items_result import ConquestApiGetHistoryItemsResult
from ..models.conquest_api_get_job_state_query import ConquestApiGetJobStateQuery
from ..models.conquest_api_get_job_state_response import ConquestApiGetJobStateResponse
from ..models.conquest_api_get_system_settings_result import ConquestApiGetSystemSettingsResult
from ..models.conquest_api_get_upload_token_reponse import ConquestApiGetUploadTokenReponse
from ..models.conquest_api_get_user_preferences_result import ConquestApiGetUserPreferencesResult
from ..models.conquest_api_get_view_response import ConquestApiGetViewResponse
from ..models.conquest_api_inspection_record import ConquestApiInspectionRecord
from ..models.conquest_api_inspections_for_asset_query import ConquestApiInspectionsForAssetQuery
from ..models.conquest_api_inspections_for_asset_response import ConquestApiInspectionsForAssetResponse
from ..models.conquest_api_issue_by import ConquestApiIssueBy
from ..models.conquest_api_issue_work_order_result import ConquestApiIssueWorkOrderResult
from ..models.conquest_api_item_link import ConquestApiItemLink
from ..models.conquest_api_job_creation_details import ConquestApiJobCreationDetails
from ..models.conquest_api_job_error import ConquestApiJobError
from ..models.conquest_api_job_key import ConquestApiJobKey
from ..models.conquest_api_job_progress_info import ConquestApiJobProgressInfo
from ..models.conquest_api_job_result import ConquestApiJobResult
from ..models.conquest_api_job_state import ConquestApiJobState
from ..models.conquest_api_job_status import ConquestApiJobStatus
from ..models.conquest_api_job_type import ConquestApiJobType
from ..models.conquest_api_legacy_document_directory import ConquestApiLegacyDocumentDirectory
from ..models.conquest_api_line_style import ConquestApiLineStyle
from ..models.conquest_api_list_attribute_sets_query import ConquestApiListAttributeSetsQuery
from ..models.conquest_api_list_document_locations_query import ConquestApiListDocumentLocationsQuery
from ..models.conquest_api_list_document_locations_response import ConquestApiListDocumentLocationsResponse
from ..models.conquest_api_list_filters_query import ConquestApiListFiltersQuery
from ..models.conquest_api_list_filters_result import ConquestApiListFiltersResult
from ..models.conquest_api_list_hierarchy_nodes_query import ConquestApiListHierarchyNodesQuery
from ..models.conquest_api_list_standard_actions_result import ConquestApiListStandardActionsResult
from ..models.conquest_api_list_standard_defect_responses_query import ConquestApiListStandardDefectResponsesQuery
from ..models.conquest_api_list_standard_defect_responses_result import ConquestApiListStandardDefectResponsesResult
from ..models.conquest_api_list_view_fields_query import ConquestApiListViewFieldsQuery
from ..models.conquest_api_load_work_order_report_result import ConquestApiLoadWorkOrderReportResult
from ..models.conquest_api_lock import ConquestApiLock
from ..models.conquest_api_log_book_action_completion_process import ConquestApiLogBookActionCompletionProcess
from ..models.conquest_api_map_view_record import ConquestApiMapViewRecord
from ..models.conquest_api_master_action_completion_process import ConquestApiMasterActionCompletionProcess
from ..models.conquest_api_move_action_command import ConquestApiMoveActionCommand
from ..models.conquest_api_move_asset_command import ConquestApiMoveAssetCommand
from ..models.conquest_api_new_condition_inspection_command import ConquestApiNewConditionInspectionCommand
from ..models.conquest_api_object_attribute import ConquestApiObjectAttribute
from ..models.conquest_api_object_attribute_kind import ConquestApiObjectAttributeKind
from ..models.conquest_api_object_attribute_parameter_type import ConquestApiObjectAttributeParameterType
from ..models.conquest_api_object_header import ConquestApiObjectHeader
from ..models.conquest_api_object_headers_result import ConquestApiObjectHeadersResult
from ..models.conquest_api_object_key import ConquestApiObjectKey
from ..models.conquest_api_object_key_value import ConquestApiObjectKeyValue
from ..models.conquest_api_object_permission import ConquestApiObjectPermission
from ..models.conquest_api_object_relation import ConquestApiObjectRelation
from ..models.conquest_api_object_type import ConquestApiObjectType
from ..models.conquest_api_permission import ConquestApiPermission
from ..models.conquest_api_predefined_context_criteria import ConquestApiPredefinedContextCriteria
from ..models.conquest_api_record_column import ConquestApiRecordColumn
from ..models.conquest_api_record_row import ConquestApiRecordRow
from ..models.conquest_api_record_set import ConquestApiRecordSet
from ..models.conquest_api_record_set_cursor import ConquestApiRecordSetCursor
from ..models.conquest_api_relate_result import ConquestApiRelateResult
from ..models.conquest_api_related_document import ConquestApiRelatedDocument
from ..models.conquest_api_relation import ConquestApiRelation
from ..models.conquest_api_remove_document_command import ConquestApiRemoveDocumentCommand
from ..models.conquest_api_report_definition import ConquestApiReportDefinition
from ..models.conquest_api_request_entity import ConquestApiRequestEntity
from ..models.conquest_api_request_record import ConquestApiRequestRecord
from ..models.conquest_api_request_record_change_set import ConquestApiRequestRecordChangeSet
from ..models.conquest_api_reverse_action_completion_command import ConquestApiReverseActionCompletionCommand
from ..models.conquest_api_reverse_action_completion_result import ConquestApiReverseActionCompletionResult
from ..models.conquest_api_session_summary import ConquestApiSessionSummary
from ..models.conquest_api_shape_style import ConquestApiShapeStyle
from ..models.conquest_api_simple_action_completion_process import ConquestApiSimpleActionCompletionProcess
from ..models.conquest_api_standard_action_entity import ConquestApiStandardActionEntity
from ..models.conquest_api_standard_action_record import ConquestApiStandardActionRecord
from ..models.conquest_api_standard_defect_entity import ConquestApiStandardDefectEntity
from ..models.conquest_api_standard_defect_record import ConquestApiStandardDefectRecord
from ..models.conquest_api_standard_defect_response import ConquestApiStandardDefectResponse
from ..models.conquest_api_standard_defect_severity import ConquestApiStandardDefectSeverity
from ..models.conquest_api_standard_inspection_entity import ConquestApiStandardInspectionEntity
from ..models.conquest_api_standard_inspection_record import ConquestApiStandardInspectionRecord
from ..models.conquest_api_style import ConquestApiStyle
from ..models.conquest_api_system_setting import ConquestApiSystemSetting
from ..models.conquest_api_system_version_response import ConquestApiSystemVersionResponse
from ..models.conquest_api_tag_as_inspected_command import ConquestApiTagAsInspectedCommand
from ..models.conquest_api_timestamp_value import ConquestApiTimestampValue
from ..models.conquest_api_type_permission import ConquestApiTypePermission
from ..models.conquest_api_update_document_migration_status_response import ConquestApiUpdateDocumentMigrationStatusResponse
from ..models.conquest_api_upload_status import ConquestApiUploadStatus
from ..models.conquest_api_upload_token import ConquestApiUploadToken
from ..models.conquest_api_user_history_item import ConquestApiUserHistoryItem
from ..models.conquest_api_user_preference import ConquestApiUserPreference
from ..models.conquest_api_user_view_filter import ConquestApiUserViewFilter
from ..models.conquest_api_value_type import ConquestApiValueType
from ..models.conquest_api_view_context import ConquestApiViewContext
from ..models.conquest_api_view_field import ConquestApiViewField
from ..models.conquest_api_who_am_i_response import ConquestApiWhoAmIResponse
from ..models.conquest_apigpkg_column_info import ConquestApigpkgColumnInfo
from ..models.conquest_apigpkg_contents import ConquestApigpkgContents
from ..models.conquest_apigpkg_data_columns import ConquestApigpkgDataColumns
from ..models.conquest_apigpkg_geometry_columns import ConquestApigpkgGeometryColumns
from ..models.protobuf_any import ProtobufAny
from ..models.runtime_error import RuntimeError
