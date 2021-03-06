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

class ConquestApiGetCopyDownFieldNamesResponse(object):
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
        'field_definitions': 'list[ConquestApiCopyDownFieldDefinition]',
        'has_children': 'bool'
    }

    attribute_map = {
        'field_definitions': 'FieldDefinitions',
        'has_children': 'hasChildren'
    }

    def __init__(self, field_definitions=None, has_children=None):  # noqa: E501
        """ConquestApiGetCopyDownFieldNamesResponse - a model defined in Swagger"""  # noqa: E501
        self._field_definitions = None
        self._has_children = None
        self.discriminator = None
        if field_definitions is not None:
            self.field_definitions = field_definitions
        if has_children is not None:
            self.has_children = has_children

    @property
    def field_definitions(self):
        """Gets the field_definitions of this ConquestApiGetCopyDownFieldNamesResponse.  # noqa: E501


        :return: The field_definitions of this ConquestApiGetCopyDownFieldNamesResponse.  # noqa: E501
        :rtype: list[ConquestApiCopyDownFieldDefinition]
        """
        return self._field_definitions

    @field_definitions.setter
    def field_definitions(self, field_definitions):
        """Sets the field_definitions of this ConquestApiGetCopyDownFieldNamesResponse.


        :param field_definitions: The field_definitions of this ConquestApiGetCopyDownFieldNamesResponse.  # noqa: E501
        :type: list[ConquestApiCopyDownFieldDefinition]
        """

        self._field_definitions = field_definitions

    @property
    def has_children(self):
        """Gets the has_children of this ConquestApiGetCopyDownFieldNamesResponse.  # noqa: E501


        :return: The has_children of this ConquestApiGetCopyDownFieldNamesResponse.  # noqa: E501
        :rtype: bool
        """
        return self._has_children

    @has_children.setter
    def has_children(self, has_children):
        """Sets the has_children of this ConquestApiGetCopyDownFieldNamesResponse.


        :param has_children: The has_children of this ConquestApiGetCopyDownFieldNamesResponse.  # noqa: E501
        :type: bool
        """

        self._has_children = has_children

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
        if issubclass(ConquestApiGetCopyDownFieldNamesResponse, dict):
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
        if not isinstance(other, ConquestApiGetCopyDownFieldNamesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
