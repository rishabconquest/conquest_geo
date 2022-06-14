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

class ConquestApiGeographyCoordinates(object):
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
        'latitude': 'float',
        'longitude': 'float',
        'pin': 'bool'
    }

    attribute_map = {
        'latitude': 'latitude',
        'longitude': 'longitude',
        'pin': 'pin'
    }

    def __init__(self, latitude=None, longitude=None, pin=None):  # noqa: E501
        """ConquestApiGeographyCoordinates - a model defined in Swagger"""  # noqa: E501
        self._latitude = None
        self._longitude = None
        self._pin = None
        self.discriminator = None
        if latitude is not None:
            self.latitude = latitude
        if longitude is not None:
            self.longitude = longitude
        if pin is not None:
            self.pin = pin

    @property
    def latitude(self):
        """Gets the latitude of this ConquestApiGeographyCoordinates.  # noqa: E501


        :return: The latitude of this ConquestApiGeographyCoordinates.  # noqa: E501
        :rtype: float
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude):
        """Sets the latitude of this ConquestApiGeographyCoordinates.


        :param latitude: The latitude of this ConquestApiGeographyCoordinates.  # noqa: E501
        :type: float
        """

        self._latitude = latitude

    @property
    def longitude(self):
        """Gets the longitude of this ConquestApiGeographyCoordinates.  # noqa: E501


        :return: The longitude of this ConquestApiGeographyCoordinates.  # noqa: E501
        :rtype: float
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude):
        """Sets the longitude of this ConquestApiGeographyCoordinates.


        :param longitude: The longitude of this ConquestApiGeographyCoordinates.  # noqa: E501
        :type: float
        """

        self._longitude = longitude

    @property
    def pin(self):
        """Gets the pin of this ConquestApiGeographyCoordinates.  # noqa: E501


        :return: The pin of this ConquestApiGeographyCoordinates.  # noqa: E501
        :rtype: bool
        """
        return self._pin

    @pin.setter
    def pin(self, pin):
        """Sets the pin of this ConquestApiGeographyCoordinates.


        :param pin: The pin of this ConquestApiGeographyCoordinates.  # noqa: E501
        :type: bool
        """

        self._pin = pin

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
        if issubclass(ConquestApiGeographyCoordinates, dict):
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
        if not isinstance(other, ConquestApiGeographyCoordinates):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other