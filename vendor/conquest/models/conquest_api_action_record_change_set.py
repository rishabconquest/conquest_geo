# coding: utf-8

"""
    Conquest API v2

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from ..configuration import Configuration


class ConquestApiActionRecordChangeSet(object):
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
        'changes': 'list[str]',
        'last_edit': 'datetime',
        'original': 'ConquestApiActionRecord',
        'updated': 'ConquestApiActionRecord'
    }

    attribute_map = {
        'action_id': 'ActionID',
        'changes': 'Changes',
        'last_edit': 'LastEdit',
        'original': 'Original',
        'updated': 'Updated'
    }

    def __init__(self, action_id=None, changes=None, last_edit=None, original=None, updated=None, _configuration=None):  # noqa: E501
        """ConquestApiActionRecordChangeSet - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._action_id = None
        self._changes = None
        self._last_edit = None
        self._original = None
        self._updated = None
        self.discriminator = None

        if action_id is not None:
            self.action_id = action_id
        if changes is not None:
            self.changes = changes
        if last_edit is not None:
            self.last_edit = last_edit
        if original is not None:
            self.original = original
        if updated is not None:
            self.updated = updated

    @property
    def action_id(self):
        """Gets the action_id of this ConquestApiActionRecordChangeSet.  # noqa: E501


        :return: The action_id of this ConquestApiActionRecordChangeSet.  # noqa: E501
        :rtype: int
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        """Sets the action_id of this ConquestApiActionRecordChangeSet.


        :param action_id: The action_id of this ConquestApiActionRecordChangeSet.  # noqa: E501
        :type: int
        """

        self._action_id = action_id

    @property
    def changes(self):
        """Gets the changes of this ConquestApiActionRecordChangeSet.  # noqa: E501


        :return: The changes of this ConquestApiActionRecordChangeSet.  # noqa: E501
        :rtype: list[str]
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """Sets the changes of this ConquestApiActionRecordChangeSet.


        :param changes: The changes of this ConquestApiActionRecordChangeSet.  # noqa: E501
        :type: list[str]
        """

        self._changes = changes

    @property
    def last_edit(self):
        """Gets the last_edit of this ConquestApiActionRecordChangeSet.  # noqa: E501


        :return: The last_edit of this ConquestApiActionRecordChangeSet.  # noqa: E501
        :rtype: datetime
        """
        return self._last_edit

    @last_edit.setter
    def last_edit(self, last_edit):
        """Sets the last_edit of this ConquestApiActionRecordChangeSet.


        :param last_edit: The last_edit of this ConquestApiActionRecordChangeSet.  # noqa: E501
        :type: datetime
        """

        self._last_edit = last_edit

    @property
    def original(self):
        """Gets the original of this ConquestApiActionRecordChangeSet.  # noqa: E501


        :return: The original of this ConquestApiActionRecordChangeSet.  # noqa: E501
        :rtype: ConquestApiActionRecord
        """
        return self._original

    @original.setter
    def original(self, original):
        """Sets the original of this ConquestApiActionRecordChangeSet.


        :param original: The original of this ConquestApiActionRecordChangeSet.  # noqa: E501
        :type: ConquestApiActionRecord
        """

        self._original = original

    @property
    def updated(self):
        """Gets the updated of this ConquestApiActionRecordChangeSet.  # noqa: E501


        :return: The updated of this ConquestApiActionRecordChangeSet.  # noqa: E501
        :rtype: ConquestApiActionRecord
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ConquestApiActionRecordChangeSet.


        :param updated: The updated of this ConquestApiActionRecordChangeSet.  # noqa: E501
        :type: ConquestApiActionRecord
        """

        self._updated = updated

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
        if issubclass(ConquestApiActionRecordChangeSet, dict):
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
        if not isinstance(other, ConquestApiActionRecordChangeSet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiActionRecordChangeSet):
            return True

        return self.to_dict() != other.to_dict()
