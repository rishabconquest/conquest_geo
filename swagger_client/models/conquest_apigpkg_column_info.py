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

class ConquestApigpkgColumnInfo(object):
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
        'column_name': 'str',
        'data_type': 'str',
        'primary_key': 'bool',
        'table_name': 'str'
    }

    attribute_map = {
        'column_name': 'column_name',
        'data_type': 'data_type',
        'primary_key': 'primary_key',
        'table_name': 'table_name'
    }

    def __init__(self, column_name=None, data_type=None, primary_key=None, table_name=None):  # noqa: E501
        """ConquestApigpkgColumnInfo - a model defined in Swagger"""  # noqa: E501
        self._column_name = None
        self._data_type = None
        self._primary_key = None
        self._table_name = None
        self.discriminator = None
        if column_name is not None:
            self.column_name = column_name
        if data_type is not None:
            self.data_type = data_type
        if primary_key is not None:
            self.primary_key = primary_key
        if table_name is not None:
            self.table_name = table_name

    @property
    def column_name(self):
        """Gets the column_name of this ConquestApigpkgColumnInfo.  # noqa: E501


        :return: The column_name of this ConquestApigpkgColumnInfo.  # noqa: E501
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this ConquestApigpkgColumnInfo.


        :param column_name: The column_name of this ConquestApigpkgColumnInfo.  # noqa: E501
        :type: str
        """

        self._column_name = column_name

    @property
    def data_type(self):
        """Gets the data_type of this ConquestApigpkgColumnInfo.  # noqa: E501


        :return: The data_type of this ConquestApigpkgColumnInfo.  # noqa: E501
        :rtype: str
        """
        return self._data_type

    @data_type.setter
    def data_type(self, data_type):
        """Sets the data_type of this ConquestApigpkgColumnInfo.


        :param data_type: The data_type of this ConquestApigpkgColumnInfo.  # noqa: E501
        :type: str
        """

        self._data_type = data_type

    @property
    def primary_key(self):
        """Gets the primary_key of this ConquestApigpkgColumnInfo.  # noqa: E501


        :return: The primary_key of this ConquestApigpkgColumnInfo.  # noqa: E501
        :rtype: bool
        """
        return self._primary_key

    @primary_key.setter
    def primary_key(self, primary_key):
        """Sets the primary_key of this ConquestApigpkgColumnInfo.


        :param primary_key: The primary_key of this ConquestApigpkgColumnInfo.  # noqa: E501
        :type: bool
        """

        self._primary_key = primary_key

    @property
    def table_name(self):
        """Gets the table_name of this ConquestApigpkgColumnInfo.  # noqa: E501


        :return: The table_name of this ConquestApigpkgColumnInfo.  # noqa: E501
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this ConquestApigpkgColumnInfo.


        :param table_name: The table_name of this ConquestApigpkgColumnInfo.  # noqa: E501
        :type: str
        """

        self._table_name = table_name

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
        if issubclass(ConquestApigpkgColumnInfo, dict):
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
        if not isinstance(other, ConquestApigpkgColumnInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
