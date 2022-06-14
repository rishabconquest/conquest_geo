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


class ConquestApiAttributeSetDimensionValue(object):
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
        'code_description': 'str',
        'code_id': 'int'
    }

    attribute_map = {
        'code_description': 'CodeDescription',
        'code_id': 'CodeID'
    }

    def __init__(self, code_description=None, code_id=None, _configuration=None):  # noqa: E501
        """ConquestApiAttributeSetDimensionValue - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._code_description = None
        self._code_id = None
        self.discriminator = None

        if code_description is not None:
            self.code_description = code_description
        if code_id is not None:
            self.code_id = code_id

    @property
    def code_description(self):
        """Gets the code_description of this ConquestApiAttributeSetDimensionValue.  # noqa: E501


        :return: The code_description of this ConquestApiAttributeSetDimensionValue.  # noqa: E501
        :rtype: str
        """
        return self._code_description

    @code_description.setter
    def code_description(self, code_description):
        """Sets the code_description of this ConquestApiAttributeSetDimensionValue.


        :param code_description: The code_description of this ConquestApiAttributeSetDimensionValue.  # noqa: E501
        :type: str
        """

        self._code_description = code_description

    @property
    def code_id(self):
        """Gets the code_id of this ConquestApiAttributeSetDimensionValue.  # noqa: E501


        :return: The code_id of this ConquestApiAttributeSetDimensionValue.  # noqa: E501
        :rtype: int
        """
        return self._code_id

    @code_id.setter
    def code_id(self, code_id):
        """Sets the code_id of this ConquestApiAttributeSetDimensionValue.


        :param code_id: The code_id of this ConquestApiAttributeSetDimensionValue.  # noqa: E501
        :type: int
        """

        self._code_id = code_id

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
        if issubclass(ConquestApiAttributeSetDimensionValue, dict):
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
        if not isinstance(other, ConquestApiAttributeSetDimensionValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiAttributeSetDimensionValue):
            return True

        return self.to_dict() != other.to_dict()
