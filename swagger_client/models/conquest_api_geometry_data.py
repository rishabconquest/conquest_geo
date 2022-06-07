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

class ConquestApiGeometryData(object):
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
        'srs_id': 'int',
        'wkt': 'str'
    }

    attribute_map = {
        'srs_id': 'srs_id',
        'wkt': 'wkt'
    }

    def __init__(self, srs_id=None, wkt=None):  # noqa: E501
        """ConquestApiGeometryData - a model defined in Swagger"""  # noqa: E501
        self._srs_id = None
        self._wkt = None
        self.discriminator = None
        if srs_id is not None:
            self.srs_id = srs_id
        if wkt is not None:
            self.wkt = wkt

    @property
    def srs_id(self):
        """Gets the srs_id of this ConquestApiGeometryData.  # noqa: E501


        :return: The srs_id of this ConquestApiGeometryData.  # noqa: E501
        :rtype: int
        """
        return self._srs_id

    @srs_id.setter
    def srs_id(self, srs_id):
        """Sets the srs_id of this ConquestApiGeometryData.


        :param srs_id: The srs_id of this ConquestApiGeometryData.  # noqa: E501
        :type: int
        """

        self._srs_id = srs_id

    @property
    def wkt(self):
        """Gets the wkt of this ConquestApiGeometryData.  # noqa: E501


        :return: The wkt of this ConquestApiGeometryData.  # noqa: E501
        :rtype: str
        """
        return self._wkt

    @wkt.setter
    def wkt(self, wkt):
        """Sets the wkt of this ConquestApiGeometryData.


        :param wkt: The wkt of this ConquestApiGeometryData.  # noqa: E501
        :type: str
        """

        self._wkt = wkt

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
        if issubclass(ConquestApiGeometryData, dict):
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
        if not isinstance(other, ConquestApiGeometryData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
