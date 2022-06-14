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


class ConquestApiShapeStyle(object):
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
        'fill_color': 'str',
        'fill_opacity': 'float'
    }

    attribute_map = {
        'fill_color': 'FillColor',
        'fill_opacity': 'FillOpacity'
    }

    def __init__(self, fill_color=None, fill_opacity=None, _configuration=None):  # noqa: E501
        """ConquestApiShapeStyle - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._fill_color = None
        self._fill_opacity = None
        self.discriminator = None

        if fill_color is not None:
            self.fill_color = fill_color
        if fill_opacity is not None:
            self.fill_opacity = fill_opacity

    @property
    def fill_color(self):
        """Gets the fill_color of this ConquestApiShapeStyle.  # noqa: E501


        :return: The fill_color of this ConquestApiShapeStyle.  # noqa: E501
        :rtype: str
        """
        return self._fill_color

    @fill_color.setter
    def fill_color(self, fill_color):
        """Sets the fill_color of this ConquestApiShapeStyle.


        :param fill_color: The fill_color of this ConquestApiShapeStyle.  # noqa: E501
        :type: str
        """

        self._fill_color = fill_color

    @property
    def fill_opacity(self):
        """Gets the fill_opacity of this ConquestApiShapeStyle.  # noqa: E501


        :return: The fill_opacity of this ConquestApiShapeStyle.  # noqa: E501
        :rtype: float
        """
        return self._fill_opacity

    @fill_opacity.setter
    def fill_opacity(self, fill_opacity):
        """Sets the fill_opacity of this ConquestApiShapeStyle.


        :param fill_opacity: The fill_opacity of this ConquestApiShapeStyle.  # noqa: E501
        :type: float
        """

        self._fill_opacity = fill_opacity

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
        if issubclass(ConquestApiShapeStyle, dict):
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
        if not isinstance(other, ConquestApiShapeStyle):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiShapeStyle):
            return True

        return self.to_dict() != other.to_dict()
