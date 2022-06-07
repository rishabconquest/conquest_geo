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

class ConquestApiFontStyle(object):
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
        'code_point': 'int',
        'color': 'str',
        'font_family': 'str',
        'font_package': 'str',
        'size': 'float'
    }

    attribute_map = {
        'code_point': 'CodePoint',
        'color': 'Color',
        'font_family': 'FontFamily',
        'font_package': 'FontPackage',
        'size': 'Size'
    }

    def __init__(self, code_point=None, color=None, font_family=None, font_package=None, size=None):  # noqa: E501
        """ConquestApiFontStyle - a model defined in Swagger"""  # noqa: E501
        self._code_point = None
        self._color = None
        self._font_family = None
        self._font_package = None
        self._size = None
        self.discriminator = None
        if code_point is not None:
            self.code_point = code_point
        if color is not None:
            self.color = color
        if font_family is not None:
            self.font_family = font_family
        if font_package is not None:
            self.font_package = font_package
        if size is not None:
            self.size = size

    @property
    def code_point(self):
        """Gets the code_point of this ConquestApiFontStyle.  # noqa: E501


        :return: The code_point of this ConquestApiFontStyle.  # noqa: E501
        :rtype: int
        """
        return self._code_point

    @code_point.setter
    def code_point(self, code_point):
        """Sets the code_point of this ConquestApiFontStyle.


        :param code_point: The code_point of this ConquestApiFontStyle.  # noqa: E501
        :type: int
        """

        self._code_point = code_point

    @property
    def color(self):
        """Gets the color of this ConquestApiFontStyle.  # noqa: E501


        :return: The color of this ConquestApiFontStyle.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this ConquestApiFontStyle.


        :param color: The color of this ConquestApiFontStyle.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def font_family(self):
        """Gets the font_family of this ConquestApiFontStyle.  # noqa: E501


        :return: The font_family of this ConquestApiFontStyle.  # noqa: E501
        :rtype: str
        """
        return self._font_family

    @font_family.setter
    def font_family(self, font_family):
        """Sets the font_family of this ConquestApiFontStyle.


        :param font_family: The font_family of this ConquestApiFontStyle.  # noqa: E501
        :type: str
        """

        self._font_family = font_family

    @property
    def font_package(self):
        """Gets the font_package of this ConquestApiFontStyle.  # noqa: E501


        :return: The font_package of this ConquestApiFontStyle.  # noqa: E501
        :rtype: str
        """
        return self._font_package

    @font_package.setter
    def font_package(self, font_package):
        """Sets the font_package of this ConquestApiFontStyle.


        :param font_package: The font_package of this ConquestApiFontStyle.  # noqa: E501
        :type: str
        """

        self._font_package = font_package

    @property
    def size(self):
        """Gets the size of this ConquestApiFontStyle.  # noqa: E501


        :return: The size of this ConquestApiFontStyle.  # noqa: E501
        :rtype: float
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ConquestApiFontStyle.


        :param size: The size of this ConquestApiFontStyle.  # noqa: E501
        :type: float
        """

        self._size = size

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
        if issubclass(ConquestApiFontStyle, dict):
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
        if not isinstance(other, ConquestApiFontStyle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other