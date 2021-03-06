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


class ConquestApiStandardActionEntity(object):
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
        'deleted': 'bool',
        'record': 'ConquestApiStandardActionRecord',
        'std_action_id': 'int',
        'type_id': 'int'
    }

    attribute_map = {
        'deleted': 'Deleted',
        'record': 'Record',
        'std_action_id': 'StdActionID',
        'type_id': 'TypeID'
    }

    def __init__(self, deleted=None, record=None, std_action_id=None, type_id=None, _configuration=None):  # noqa: E501
        """ConquestApiStandardActionEntity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._deleted = None
        self._record = None
        self._std_action_id = None
        self._type_id = None
        self.discriminator = None

        if deleted is not None:
            self.deleted = deleted
        if record is not None:
            self.record = record
        if std_action_id is not None:
            self.std_action_id = std_action_id
        if type_id is not None:
            self.type_id = type_id

    @property
    def deleted(self):
        """Gets the deleted of this ConquestApiStandardActionEntity.  # noqa: E501


        :return: The deleted of this ConquestApiStandardActionEntity.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this ConquestApiStandardActionEntity.


        :param deleted: The deleted of this ConquestApiStandardActionEntity.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def record(self):
        """Gets the record of this ConquestApiStandardActionEntity.  # noqa: E501


        :return: The record of this ConquestApiStandardActionEntity.  # noqa: E501
        :rtype: ConquestApiStandardActionRecord
        """
        return self._record

    @record.setter
    def record(self, record):
        """Sets the record of this ConquestApiStandardActionEntity.


        :param record: The record of this ConquestApiStandardActionEntity.  # noqa: E501
        :type: ConquestApiStandardActionRecord
        """

        self._record = record

    @property
    def std_action_id(self):
        """Gets the std_action_id of this ConquestApiStandardActionEntity.  # noqa: E501


        :return: The std_action_id of this ConquestApiStandardActionEntity.  # noqa: E501
        :rtype: int
        """
        return self._std_action_id

    @std_action_id.setter
    def std_action_id(self, std_action_id):
        """Sets the std_action_id of this ConquestApiStandardActionEntity.


        :param std_action_id: The std_action_id of this ConquestApiStandardActionEntity.  # noqa: E501
        :type: int
        """

        self._std_action_id = std_action_id

    @property
    def type_id(self):
        """Gets the type_id of this ConquestApiStandardActionEntity.  # noqa: E501


        :return: The type_id of this ConquestApiStandardActionEntity.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this ConquestApiStandardActionEntity.


        :param type_id: The type_id of this ConquestApiStandardActionEntity.  # noqa: E501
        :type: int
        """

        self._type_id = type_id

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
        if issubclass(ConquestApiStandardActionEntity, dict):
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
        if not isinstance(other, ConquestApiStandardActionEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiStandardActionEntity):
            return True

        return self.to_dict() != other.to_dict()
