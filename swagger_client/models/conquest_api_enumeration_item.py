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

class ConquestApiEnumerationItem(object):
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
        'display_value': 'str',
        'tag': 'str',
        'value': 'int'
    }

    attribute_map = {
        'display_value': 'displayValue',
        'tag': 'tag',
        'value': 'value'
    }

    def __init__(self, display_value=None, tag=None, value=None):  # noqa: E501
        """ConquestApiEnumerationItem - a model defined in Swagger"""  # noqa: E501
        self._display_value = None
        self._tag = None
        self._value = None
        self.discriminator = None
        if display_value is not None:
            self.display_value = display_value
        if tag is not None:
            self.tag = tag
        if value is not None:
            self.value = value

    @property
    def display_value(self):
        """Gets the display_value of this ConquestApiEnumerationItem.  # noqa: E501


        :return: The display_value of this ConquestApiEnumerationItem.  # noqa: E501
        :rtype: str
        """
        return self._display_value

    @display_value.setter
    def display_value(self, display_value):
        """Sets the display_value of this ConquestApiEnumerationItem.


        :param display_value: The display_value of this ConquestApiEnumerationItem.  # noqa: E501
        :type: str
        """

        self._display_value = display_value

    @property
    def tag(self):
        """Gets the tag of this ConquestApiEnumerationItem.  # noqa: E501


        :return: The tag of this ConquestApiEnumerationItem.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this ConquestApiEnumerationItem.


        :param tag: The tag of this ConquestApiEnumerationItem.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def value(self):
        """Gets the value of this ConquestApiEnumerationItem.  # noqa: E501


        :return: The value of this ConquestApiEnumerationItem.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ConquestApiEnumerationItem.


        :param value: The value of this ConquestApiEnumerationItem.  # noqa: E501
        :type: int
        """

        self._value = value

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
        if issubclass(ConquestApiEnumerationItem, dict):
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
        if not isinstance(other, ConquestApiEnumerationItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
