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

class ConquestApiDefectRecordChangeSet(object):
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
        'changes': 'list[str]',
        'defect_id': 'int',
        'last_edit': 'datetime',
        'original': 'ConquestApiDefectRecord',
        'updated': 'ConquestApiDefectRecord'
    }

    attribute_map = {
        'changes': 'Changes',
        'defect_id': 'DefectID',
        'last_edit': 'LastEdit',
        'original': 'Original',
        'updated': 'Updated'
    }

    def __init__(self, changes=None, defect_id=None, last_edit=None, original=None, updated=None):  # noqa: E501
        """ConquestApiDefectRecordChangeSet - a model defined in Swagger"""  # noqa: E501
        self._changes = None
        self._defect_id = None
        self._last_edit = None
        self._original = None
        self._updated = None
        self.discriminator = None
        if changes is not None:
            self.changes = changes
        if defect_id is not None:
            self.defect_id = defect_id
        if last_edit is not None:
            self.last_edit = last_edit
        if original is not None:
            self.original = original
        if updated is not None:
            self.updated = updated

    @property
    def changes(self):
        """Gets the changes of this ConquestApiDefectRecordChangeSet.  # noqa: E501


        :return: The changes of this ConquestApiDefectRecordChangeSet.  # noqa: E501
        :rtype: list[str]
        """
        return self._changes

    @changes.setter
    def changes(self, changes):
        """Sets the changes of this ConquestApiDefectRecordChangeSet.


        :param changes: The changes of this ConquestApiDefectRecordChangeSet.  # noqa: E501
        :type: list[str]
        """

        self._changes = changes

    @property
    def defect_id(self):
        """Gets the defect_id of this ConquestApiDefectRecordChangeSet.  # noqa: E501


        :return: The defect_id of this ConquestApiDefectRecordChangeSet.  # noqa: E501
        :rtype: int
        """
        return self._defect_id

    @defect_id.setter
    def defect_id(self, defect_id):
        """Sets the defect_id of this ConquestApiDefectRecordChangeSet.


        :param defect_id: The defect_id of this ConquestApiDefectRecordChangeSet.  # noqa: E501
        :type: int
        """

        self._defect_id = defect_id

    @property
    def last_edit(self):
        """Gets the last_edit of this ConquestApiDefectRecordChangeSet.  # noqa: E501


        :return: The last_edit of this ConquestApiDefectRecordChangeSet.  # noqa: E501
        :rtype: datetime
        """
        return self._last_edit

    @last_edit.setter
    def last_edit(self, last_edit):
        """Sets the last_edit of this ConquestApiDefectRecordChangeSet.


        :param last_edit: The last_edit of this ConquestApiDefectRecordChangeSet.  # noqa: E501
        :type: datetime
        """

        self._last_edit = last_edit

    @property
    def original(self):
        """Gets the original of this ConquestApiDefectRecordChangeSet.  # noqa: E501


        :return: The original of this ConquestApiDefectRecordChangeSet.  # noqa: E501
        :rtype: ConquestApiDefectRecord
        """
        return self._original

    @original.setter
    def original(self, original):
        """Sets the original of this ConquestApiDefectRecordChangeSet.


        :param original: The original of this ConquestApiDefectRecordChangeSet.  # noqa: E501
        :type: ConquestApiDefectRecord
        """

        self._original = original

    @property
    def updated(self):
        """Gets the updated of this ConquestApiDefectRecordChangeSet.  # noqa: E501


        :return: The updated of this ConquestApiDefectRecordChangeSet.  # noqa: E501
        :rtype: ConquestApiDefectRecord
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        """Sets the updated of this ConquestApiDefectRecordChangeSet.


        :param updated: The updated of this ConquestApiDefectRecordChangeSet.  # noqa: E501
        :type: ConquestApiDefectRecord
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
        if issubclass(ConquestApiDefectRecordChangeSet, dict):
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
        if not isinstance(other, ConquestApiDefectRecordChangeSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
