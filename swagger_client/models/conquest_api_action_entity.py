# coding: utf-8

"""
    Conquest API v4

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ConquestApiActionEntity(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'action_id': 'int',
        'approval_requested': 'ConquestApiTimestampValue',
        'asset_id': 'int',
        'attribute_id': 'int',
        'completed': 'bool',
        'completion_date': 'ConquestApiTimestampValue',
        'created_by': 'str',
        'document_location': 'str',
        'edit_date': 'datetime',
        'editor': 'str',
        'issue_date': 'ConquestApiTimestampValue',
        'map_style': 'ConquestApiStyle',
        'permission': 'ConquestApiPermission',
        'previous_action': 'int',
        'record': 'ConquestApiActionRecord',
        'reference_id': 'str',
        'type_id': 'int',
        'lock': 'ConquestApiLock'
    }

    attribute_map = {
        'action_id': 'ActionID',
        'approval_requested': 'ApprovalRequested',
        'asset_id': 'AssetID',
        'attribute_id': 'AttributeID',
        'completed': 'Completed',
        'completion_date': 'CompletionDate',
        'created_by': 'CreatedBy',
        'document_location': 'DocumentLocation',
        'edit_date': 'EditDate',
        'editor': 'Editor',
        'issue_date': 'IssueDate',
        'map_style': 'MapStyle',
        'permission': 'Permission',
        'previous_action': 'PreviousAction',
        'record': 'Record',
        'reference_id': 'ReferenceID',
        'type_id': 'TypeID',
        'lock': 'lock'
    }

    def __init__(self, action_id=None, approval_requested=None, asset_id=None, attribute_id=None, completed=None, completion_date=None, created_by=None, document_location=None, edit_date=None, editor=None, issue_date=None, map_style=None, permission=None, previous_action=None, record=None, reference_id=None, type_id=None, lock=None):  # noqa: E501
        """ConquestApiActionEntity - a model defined in Swagger"""  # noqa: E501
        self._action_id = None
        self._approval_requested = None
        self._asset_id = None
        self._attribute_id = None
        self._completed = None
        self._completion_date = None
        self._created_by = None
        self._document_location = None
        self._edit_date = None
        self._editor = None
        self._issue_date = None
        self._map_style = None
        self._permission = None
        self._previous_action = None
        self._record = None
        self._reference_id = None
        self._type_id = None
        self._lock = None
        self.discriminator = None
        if action_id is not None:
            self.action_id = action_id
        if approval_requested is not None:
            self.approval_requested = approval_requested
        if asset_id is not None:
            self.asset_id = asset_id
        if attribute_id is not None:
            self.attribute_id = attribute_id
        if completed is not None:
            self.completed = completed
        if completion_date is not None:
            self.completion_date = completion_date
        if created_by is not None:
            self.created_by = created_by
        if document_location is not None:
            self.document_location = document_location
        if edit_date is not None:
            self.edit_date = edit_date
        if editor is not None:
            self.editor = editor
        if issue_date is not None:
            self.issue_date = issue_date
        if map_style is not None:
            self.map_style = map_style
        if permission is not None:
            self.permission = permission
        if previous_action is not None:
            self.previous_action = previous_action
        if record is not None:
            self.record = record
        if reference_id is not None:
            self.reference_id = reference_id
        if type_id is not None:
            self.type_id = type_id
        if lock is not None:
            self.lock = lock

    @property
    def action_id(self):
        """Gets the action_id of this ConquestApiActionEntity.  # noqa: E501


        :return: The action_id of this ConquestApiActionEntity.  # noqa: E501
        :rtype: int
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        """Sets the action_id of this ConquestApiActionEntity.


        :param action_id: The action_id of this ConquestApiActionEntity.  # noqa: E501
        :type: int
        """

        self._action_id = action_id

    @property
    def approval_requested(self):
        """Gets the approval_requested of this ConquestApiActionEntity.  # noqa: E501


        :return: The approval_requested of this ConquestApiActionEntity.  # noqa: E501
        :rtype: ConquestApiTimestampValue
        """
        return self._approval_requested

    @approval_requested.setter
    def approval_requested(self, approval_requested):
        """Sets the approval_requested of this ConquestApiActionEntity.


        :param approval_requested: The approval_requested of this ConquestApiActionEntity.  # noqa: E501
        :type: ConquestApiTimestampValue
        """

        self._approval_requested = approval_requested

    @property
    def asset_id(self):
        """Gets the asset_id of this ConquestApiActionEntity.  # noqa: E501


        :return: The asset_id of this ConquestApiActionEntity.  # noqa: E501
        :rtype: int
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this ConquestApiActionEntity.


        :param asset_id: The asset_id of this ConquestApiActionEntity.  # noqa: E501
        :type: int
        """

        self._asset_id = asset_id

    @property
    def attribute_id(self):
        """Gets the attribute_id of this ConquestApiActionEntity.  # noqa: E501


        :return: The attribute_id of this ConquestApiActionEntity.  # noqa: E501
        :rtype: int
        """
        return self._attribute_id

    @attribute_id.setter
    def attribute_id(self, attribute_id):
        """Sets the attribute_id of this ConquestApiActionEntity.


        :param attribute_id: The attribute_id of this ConquestApiActionEntity.  # noqa: E501
        :type: int
        """

        self._attribute_id = attribute_id

    @property
    def completed(self):
        """Gets the completed of this ConquestApiActionEntity.  # noqa: E501


        :return: The completed of this ConquestApiActionEntity.  # noqa: E501
        :rtype: bool
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this ConquestApiActionEntity.


        :param completed: The completed of this ConquestApiActionEntity.  # noqa: E501
        :type: bool
        """

        self._completed = completed

    @property
    def completion_date(self):
        """Gets the completion_date of this ConquestApiActionEntity.  # noqa: E501


        :return: The completion_date of this ConquestApiActionEntity.  # noqa: E501
        :rtype: ConquestApiTimestampValue
        """
        return self._completion_date

    @completion_date.setter
    def completion_date(self, completion_date):
        """Sets the completion_date of this ConquestApiActionEntity.


        :param completion_date: The completion_date of this ConquestApiActionEntity.  # noqa: E501
        :type: ConquestApiTimestampValue
        """

        self._completion_date = completion_date

    @property
    def created_by(self):
        """Gets the created_by of this ConquestApiActionEntity.  # noqa: E501


        :return: The created_by of this ConquestApiActionEntity.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ConquestApiActionEntity.


        :param created_by: The created_by of this ConquestApiActionEntity.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def document_location(self):
        """Gets the document_location of this ConquestApiActionEntity.  # noqa: E501


        :return: The document_location of this ConquestApiActionEntity.  # noqa: E501
        :rtype: str
        """
        return self._document_location

    @document_location.setter
    def document_location(self, document_location):
        """Sets the document_location of this ConquestApiActionEntity.


        :param document_location: The document_location of this ConquestApiActionEntity.  # noqa: E501
        :type: str
        """

        self._document_location = document_location

    @property
    def edit_date(self):
        """Gets the edit_date of this ConquestApiActionEntity.  # noqa: E501


        :return: The edit_date of this ConquestApiActionEntity.  # noqa: E501
        :rtype: datetime
        """
        return self._edit_date

    @edit_date.setter
    def edit_date(self, edit_date):
        """Sets the edit_date of this ConquestApiActionEntity.


        :param edit_date: The edit_date of this ConquestApiActionEntity.  # noqa: E501
        :type: datetime
        """

        self._edit_date = edit_date

    @property
    def editor(self):
        """Gets the editor of this ConquestApiActionEntity.  # noqa: E501


        :return: The editor of this ConquestApiActionEntity.  # noqa: E501
        :rtype: str
        """
        return self._editor

    @editor.setter
    def editor(self, editor):
        """Sets the editor of this ConquestApiActionEntity.


        :param editor: The editor of this ConquestApiActionEntity.  # noqa: E501
        :type: str
        """

        self._editor = editor

    @property
    def issue_date(self):
        """Gets the issue_date of this ConquestApiActionEntity.  # noqa: E501


        :return: The issue_date of this ConquestApiActionEntity.  # noqa: E501
        :rtype: ConquestApiTimestampValue
        """
        return self._issue_date

    @issue_date.setter
    def issue_date(self, issue_date):
        """Sets the issue_date of this ConquestApiActionEntity.


        :param issue_date: The issue_date of this ConquestApiActionEntity.  # noqa: E501
        :type: ConquestApiTimestampValue
        """

        self._issue_date = issue_date

    @property
    def map_style(self):
        """Gets the map_style of this ConquestApiActionEntity.  # noqa: E501


        :return: The map_style of this ConquestApiActionEntity.  # noqa: E501
        :rtype: ConquestApiStyle
        """
        return self._map_style

    @map_style.setter
    def map_style(self, map_style):
        """Sets the map_style of this ConquestApiActionEntity.


        :param map_style: The map_style of this ConquestApiActionEntity.  # noqa: E501
        :type: ConquestApiStyle
        """

        self._map_style = map_style

    @property
    def permission(self):
        """Gets the permission of this ConquestApiActionEntity.  # noqa: E501


        :return: The permission of this ConquestApiActionEntity.  # noqa: E501
        :rtype: ConquestApiPermission
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this ConquestApiActionEntity.


        :param permission: The permission of this ConquestApiActionEntity.  # noqa: E501
        :type: ConquestApiPermission
        """

        self._permission = permission

    @property
    def previous_action(self):
        """Gets the previous_action of this ConquestApiActionEntity.  # noqa: E501


        :return: The previous_action of this ConquestApiActionEntity.  # noqa: E501
        :rtype: int
        """
        return self._previous_action

    @previous_action.setter
    def previous_action(self, previous_action):
        """Sets the previous_action of this ConquestApiActionEntity.


        :param previous_action: The previous_action of this ConquestApiActionEntity.  # noqa: E501
        :type: int
        """

        self._previous_action = previous_action

    @property
    def record(self):
        """Gets the record of this ConquestApiActionEntity.  # noqa: E501


        :return: The record of this ConquestApiActionEntity.  # noqa: E501
        :rtype: ConquestApiActionRecord
        """
        return self._record

    @record.setter
    def record(self, record):
        """Sets the record of this ConquestApiActionEntity.


        :param record: The record of this ConquestApiActionEntity.  # noqa: E501
        :type: ConquestApiActionRecord
        """

        self._record = record

    @property
    def reference_id(self):
        """Gets the reference_id of this ConquestApiActionEntity.  # noqa: E501


        :return: The reference_id of this ConquestApiActionEntity.  # noqa: E501
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """Sets the reference_id of this ConquestApiActionEntity.


        :param reference_id: The reference_id of this ConquestApiActionEntity.  # noqa: E501
        :type: str
        """

        self._reference_id = reference_id

    @property
    def type_id(self):
        """Gets the type_id of this ConquestApiActionEntity.  # noqa: E501


        :return: The type_id of this ConquestApiActionEntity.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this ConquestApiActionEntity.


        :param type_id: The type_id of this ConquestApiActionEntity.  # noqa: E501
        :type: int
        """

        self._type_id = type_id

    @property
    def lock(self):
        """Gets the lock of this ConquestApiActionEntity.  # noqa: E501


        :return: The lock of this ConquestApiActionEntity.  # noqa: E501
        :rtype: ConquestApiLock
        """
        return self._lock

    @lock.setter
    def lock(self, lock):
        """Sets the lock of this ConquestApiActionEntity.


        :param lock: The lock of this ConquestApiActionEntity.  # noqa: E501
        :type: ConquestApiLock
        """

        self._lock = lock

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ConquestApiActionEntity, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ConquestApiActionEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
