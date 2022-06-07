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

class ConquestApiFieldDescriptions(object):
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
        'field_descriptions': 'list[ConquestApiFieldDescription]'
    }

    attribute_map = {
        'field_descriptions': 'FieldDescriptions'
    }

    def __init__(self, field_descriptions=None):  # noqa: E501
        """ConquestApiFieldDescriptions - a model defined in Swagger"""  # noqa: E501
        self._field_descriptions = None
        self.discriminator = None
        if field_descriptions is not None:
            self.field_descriptions = field_descriptions

    @property
    def field_descriptions(self):
        """Gets the field_descriptions of this ConquestApiFieldDescriptions.  # noqa: E501


        :return: The field_descriptions of this ConquestApiFieldDescriptions.  # noqa: E501
        :rtype: list[ConquestApiFieldDescription]
        """
        return self._field_descriptions

    @field_descriptions.setter
    def field_descriptions(self, field_descriptions):
        """Sets the field_descriptions of this ConquestApiFieldDescriptions.


        :param field_descriptions: The field_descriptions of this ConquestApiFieldDescriptions.  # noqa: E501
        :type: list[ConquestApiFieldDescription]
        """

        self._field_descriptions = field_descriptions

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
        if issubclass(ConquestApiFieldDescriptions, dict):
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
        if not isinstance(other, ConquestApiFieldDescriptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other