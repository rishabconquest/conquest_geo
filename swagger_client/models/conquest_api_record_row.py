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

class ConquestApiRecordRow(object):
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
        'columns': 'list[ConquestApiAnyValue]',
        'group': 'int'
    }

    attribute_map = {
        'columns': 'columns',
        'group': 'group'
    }

    def __init__(self, columns=None, group=None):  # noqa: E501
        """ConquestApiRecordRow - a model defined in Swagger"""  # noqa: E501
        self._columns = None
        self._group = None
        self.discriminator = None
        if columns is not None:
            self.columns = columns
        if group is not None:
            self.group = group

    @property
    def columns(self):
        """Gets the columns of this ConquestApiRecordRow.  # noqa: E501


        :return: The columns of this ConquestApiRecordRow.  # noqa: E501
        :rtype: list[ConquestApiAnyValue]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this ConquestApiRecordRow.


        :param columns: The columns of this ConquestApiRecordRow.  # noqa: E501
        :type: list[ConquestApiAnyValue]
        """

        self._columns = columns

    @property
    def group(self):
        """Gets the group of this ConquestApiRecordRow.  # noqa: E501


        :return: The group of this ConquestApiRecordRow.  # noqa: E501
        :rtype: int
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ConquestApiRecordRow.


        :param group: The group of this ConquestApiRecordRow.  # noqa: E501
        :type: int
        """

        self._group = group

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
        if issubclass(ConquestApiRecordRow, dict):
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
        if not isinstance(other, ConquestApiRecordRow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
