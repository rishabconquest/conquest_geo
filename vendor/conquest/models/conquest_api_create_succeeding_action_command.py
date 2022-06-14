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


class ConquestApiCreateSucceedingActionCommand(object):
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
        'action_description': 'str',
        'action_id': 'int',
        'std_action_id': 'int'
    }

    attribute_map = {
        'action_description': 'ActionDescription',
        'action_id': 'ActionID',
        'std_action_id': 'StdActionID'
    }

    def __init__(self, action_description=None, action_id=None, std_action_id=None, _configuration=None):  # noqa: E501
        """ConquestApiCreateSucceedingActionCommand - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._action_description = None
        self._action_id = None
        self._std_action_id = None
        self.discriminator = None

        if action_description is not None:
            self.action_description = action_description
        if action_id is not None:
            self.action_id = action_id
        if std_action_id is not None:
            self.std_action_id = std_action_id

    @property
    def action_description(self):
        """Gets the action_description of this ConquestApiCreateSucceedingActionCommand.  # noqa: E501


        :return: The action_description of this ConquestApiCreateSucceedingActionCommand.  # noqa: E501
        :rtype: str
        """
        return self._action_description

    @action_description.setter
    def action_description(self, action_description):
        """Sets the action_description of this ConquestApiCreateSucceedingActionCommand.


        :param action_description: The action_description of this ConquestApiCreateSucceedingActionCommand.  # noqa: E501
        :type: str
        """

        self._action_description = action_description

    @property
    def action_id(self):
        """Gets the action_id of this ConquestApiCreateSucceedingActionCommand.  # noqa: E501


        :return: The action_id of this ConquestApiCreateSucceedingActionCommand.  # noqa: E501
        :rtype: int
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        """Sets the action_id of this ConquestApiCreateSucceedingActionCommand.


        :param action_id: The action_id of this ConquestApiCreateSucceedingActionCommand.  # noqa: E501
        :type: int
        """

        self._action_id = action_id

    @property
    def std_action_id(self):
        """Gets the std_action_id of this ConquestApiCreateSucceedingActionCommand.  # noqa: E501


        :return: The std_action_id of this ConquestApiCreateSucceedingActionCommand.  # noqa: E501
        :rtype: int
        """
        return self._std_action_id

    @std_action_id.setter
    def std_action_id(self, std_action_id):
        """Sets the std_action_id of this ConquestApiCreateSucceedingActionCommand.


        :param std_action_id: The std_action_id of this ConquestApiCreateSucceedingActionCommand.  # noqa: E501
        :type: int
        """

        self._std_action_id = std_action_id

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
        if issubclass(ConquestApiCreateSucceedingActionCommand, dict):
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
        if not isinstance(other, ConquestApiCreateSucceedingActionCommand):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiCreateSucceedingActionCommand):
            return True

        return self.to_dict() != other.to_dict()