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


class ConquestApiAttributeSetWeightedValue(object):
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
        'code_list_description': 'str',
        'code_list_id': 'int',
        'weight': 'float'
    }

    attribute_map = {
        'code_list_description': 'CodeListDescription',
        'code_list_id': 'CodeListID',
        'weight': 'Weight'
    }

    def __init__(self, code_list_description=None, code_list_id=None, weight=None, _configuration=None):  # noqa: E501
        """ConquestApiAttributeSetWeightedValue - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._code_list_description = None
        self._code_list_id = None
        self._weight = None
        self.discriminator = None

        if code_list_description is not None:
            self.code_list_description = code_list_description
        if code_list_id is not None:
            self.code_list_id = code_list_id
        if weight is not None:
            self.weight = weight

    @property
    def code_list_description(self):
        """Gets the code_list_description of this ConquestApiAttributeSetWeightedValue.  # noqa: E501


        :return: The code_list_description of this ConquestApiAttributeSetWeightedValue.  # noqa: E501
        :rtype: str
        """
        return self._code_list_description

    @code_list_description.setter
    def code_list_description(self, code_list_description):
        """Sets the code_list_description of this ConquestApiAttributeSetWeightedValue.


        :param code_list_description: The code_list_description of this ConquestApiAttributeSetWeightedValue.  # noqa: E501
        :type: str
        """

        self._code_list_description = code_list_description

    @property
    def code_list_id(self):
        """Gets the code_list_id of this ConquestApiAttributeSetWeightedValue.  # noqa: E501


        :return: The code_list_id of this ConquestApiAttributeSetWeightedValue.  # noqa: E501
        :rtype: int
        """
        return self._code_list_id

    @code_list_id.setter
    def code_list_id(self, code_list_id):
        """Sets the code_list_id of this ConquestApiAttributeSetWeightedValue.


        :param code_list_id: The code_list_id of this ConquestApiAttributeSetWeightedValue.  # noqa: E501
        :type: int
        """

        self._code_list_id = code_list_id

    @property
    def weight(self):
        """Gets the weight of this ConquestApiAttributeSetWeightedValue.  # noqa: E501


        :return: The weight of this ConquestApiAttributeSetWeightedValue.  # noqa: E501
        :rtype: float
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this ConquestApiAttributeSetWeightedValue.


        :param weight: The weight of this ConquestApiAttributeSetWeightedValue.  # noqa: E501
        :type: float
        """

        self._weight = weight

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
        if issubclass(ConquestApiAttributeSetWeightedValue, dict):
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
        if not isinstance(other, ConquestApiAttributeSetWeightedValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiAttributeSetWeightedValue):
            return True

        return self.to_dict() != other.to_dict()
