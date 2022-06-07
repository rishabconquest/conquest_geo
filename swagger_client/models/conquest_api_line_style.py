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

class ConquestApiLineStyle(object):
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
        'stroke_color': 'str',
        'stroke_opacity': 'float',
        'stroke_width': 'float'
    }

    attribute_map = {
        'stroke_color': 'StrokeColor',
        'stroke_opacity': 'StrokeOpacity',
        'stroke_width': 'StrokeWidth'
    }

    def __init__(self, stroke_color=None, stroke_opacity=None, stroke_width=None):  # noqa: E501
        """ConquestApiLineStyle - a model defined in Swagger"""  # noqa: E501
        self._stroke_color = None
        self._stroke_opacity = None
        self._stroke_width = None
        self.discriminator = None
        if stroke_color is not None:
            self.stroke_color = stroke_color
        if stroke_opacity is not None:
            self.stroke_opacity = stroke_opacity
        if stroke_width is not None:
            self.stroke_width = stroke_width

    @property
    def stroke_color(self):
        """Gets the stroke_color of this ConquestApiLineStyle.  # noqa: E501


        :return: The stroke_color of this ConquestApiLineStyle.  # noqa: E501
        :rtype: str
        """
        return self._stroke_color

    @stroke_color.setter
    def stroke_color(self, stroke_color):
        """Sets the stroke_color of this ConquestApiLineStyle.


        :param stroke_color: The stroke_color of this ConquestApiLineStyle.  # noqa: E501
        :type: str
        """

        self._stroke_color = stroke_color

    @property
    def stroke_opacity(self):
        """Gets the stroke_opacity of this ConquestApiLineStyle.  # noqa: E501


        :return: The stroke_opacity of this ConquestApiLineStyle.  # noqa: E501
        :rtype: float
        """
        return self._stroke_opacity

    @stroke_opacity.setter
    def stroke_opacity(self, stroke_opacity):
        """Sets the stroke_opacity of this ConquestApiLineStyle.


        :param stroke_opacity: The stroke_opacity of this ConquestApiLineStyle.  # noqa: E501
        :type: float
        """

        self._stroke_opacity = stroke_opacity

    @property
    def stroke_width(self):
        """Gets the stroke_width of this ConquestApiLineStyle.  # noqa: E501


        :return: The stroke_width of this ConquestApiLineStyle.  # noqa: E501
        :rtype: float
        """
        return self._stroke_width

    @stroke_width.setter
    def stroke_width(self, stroke_width):
        """Sets the stroke_width of this ConquestApiLineStyle.


        :param stroke_width: The stroke_width of this ConquestApiLineStyle.  # noqa: E501
        :type: float
        """

        self._stroke_width = stroke_width

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
        if issubclass(ConquestApiLineStyle, dict):
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
        if not isinstance(other, ConquestApiLineStyle):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
