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


class ConquestApiListStandardActionsResult(object):
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
        'standard_actions': 'list[ConquestApiStandardActionEntity]'
    }

    attribute_map = {
        'standard_actions': 'StandardActions'
    }

    def __init__(self, standard_actions=None, _configuration=None):  # noqa: E501
        """ConquestApiListStandardActionsResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._standard_actions = None
        self.discriminator = None

        if standard_actions is not None:
            self.standard_actions = standard_actions

    @property
    def standard_actions(self):
        """Gets the standard_actions of this ConquestApiListStandardActionsResult.  # noqa: E501


        :return: The standard_actions of this ConquestApiListStandardActionsResult.  # noqa: E501
        :rtype: list[ConquestApiStandardActionEntity]
        """
        return self._standard_actions

    @standard_actions.setter
    def standard_actions(self, standard_actions):
        """Sets the standard_actions of this ConquestApiListStandardActionsResult.


        :param standard_actions: The standard_actions of this ConquestApiListStandardActionsResult.  # noqa: E501
        :type: list[ConquestApiStandardActionEntity]
        """

        self._standard_actions = standard_actions

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
        if issubclass(ConquestApiListStandardActionsResult, dict):
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
        if not isinstance(other, ConquestApiListStandardActionsResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiListStandardActionsResult):
            return True

        return self.to_dict() != other.to_dict()
