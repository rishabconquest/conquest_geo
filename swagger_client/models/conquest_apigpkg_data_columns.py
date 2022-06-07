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

class ConquestApigpkgDataColumns(object):
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
        'constraint_name': 'str',
        'description': 'str',
        'mime_type': 'str',
        'name': 'str',
        'table_name': 'str',
        'title': 'str'
    }

    attribute_map = {
        'column_name': 'column_name',
        'constraint_name': 'constraint_name',
        'description': 'description',
        'mime_type': 'mime_type',
        'name': 'name',
        'table_name': 'table_name',
        'title': 'title'
    }

    def __init__(self, column_name=None, constraint_name=None, description=None, mime_type=None, name=None, table_name=None, title=None):  # noqa: E501
        """ConquestApigpkgDataColumns - a model defined in Swagger"""  # noqa: E501
        self._column_name = None
        self._constraint_name = None
        self._description = None
        self._mime_type = None
        self._name = None
        self._table_name = None
        self._title = None
        self.discriminator = None
        if column_name is not None:
            self.column_name = column_name
        if constraint_name is not None:
            self.constraint_name = constraint_name
        if description is not None:
            self.description = description
        if mime_type is not None:
            self.mime_type = mime_type
        if name is not None:
            self.name = name
        if table_name is not None:
            self.table_name = table_name
        if title is not None:
            self.title = title

    @property
    def column_name(self):
        """Gets the column_name of this ConquestApigpkgDataColumns.  # noqa: E501


        :return: The column_name of this ConquestApigpkgDataColumns.  # noqa: E501
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this ConquestApigpkgDataColumns.


        :param column_name: The column_name of this ConquestApigpkgDataColumns.  # noqa: E501
        :type: str
        """

        self._column_name = column_name

    @property
    def constraint_name(self):
        """Gets the constraint_name of this ConquestApigpkgDataColumns.  # noqa: E501


        :return: The constraint_name of this ConquestApigpkgDataColumns.  # noqa: E501
        :rtype: str
        """
        return self._constraint_name

    @constraint_name.setter
    def constraint_name(self, constraint_name):
        """Sets the constraint_name of this ConquestApigpkgDataColumns.


        :param constraint_name: The constraint_name of this ConquestApigpkgDataColumns.  # noqa: E501
        :type: str
        """

        self._constraint_name = constraint_name

    @property
    def description(self):
        """Gets the description of this ConquestApigpkgDataColumns.  # noqa: E501


        :return: The description of this ConquestApigpkgDataColumns.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConquestApigpkgDataColumns.


        :param description: The description of this ConquestApigpkgDataColumns.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def mime_type(self):
        """Gets the mime_type of this ConquestApigpkgDataColumns.  # noqa: E501


        :return: The mime_type of this ConquestApigpkgDataColumns.  # noqa: E501
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this ConquestApigpkgDataColumns.


        :param mime_type: The mime_type of this ConquestApigpkgDataColumns.  # noqa: E501
        :type: str
        """

        self._mime_type = mime_type

    @property
    def name(self):
        """Gets the name of this ConquestApigpkgDataColumns.  # noqa: E501


        :return: The name of this ConquestApigpkgDataColumns.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ConquestApigpkgDataColumns.


        :param name: The name of this ConquestApigpkgDataColumns.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def table_name(self):
        """Gets the table_name of this ConquestApigpkgDataColumns.  # noqa: E501


        :return: The table_name of this ConquestApigpkgDataColumns.  # noqa: E501
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this ConquestApigpkgDataColumns.


        :param table_name: The table_name of this ConquestApigpkgDataColumns.  # noqa: E501
        :type: str
        """

        self._table_name = table_name

    @property
    def title(self):
        """Gets the title of this ConquestApigpkgDataColumns.  # noqa: E501


        :return: The title of this ConquestApigpkgDataColumns.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ConquestApigpkgDataColumns.


        :param title: The title of this ConquestApigpkgDataColumns.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(ConquestApigpkgDataColumns, dict):
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
        if not isinstance(other, ConquestApigpkgDataColumns):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
