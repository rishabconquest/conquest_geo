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

class ConquestApiCompleteActionCommand(object):
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
        'completion_options': 'ConquestApiActionCompletionOptions',
        'sub_action_completion_options': 'list[ConquestApiActionCompletionOptions]'
    }

    attribute_map = {
        'completion_options': 'CompletionOptions',
        'sub_action_completion_options': 'SubActionCompletionOptions'
    }

    def __init__(self, completion_options=None, sub_action_completion_options=None):  # noqa: E501
        """ConquestApiCompleteActionCommand - a model defined in Swagger"""  # noqa: E501
        self._completion_options = None
        self._sub_action_completion_options = None
        self.discriminator = None
        if completion_options is not None:
            self.completion_options = completion_options
        if sub_action_completion_options is not None:
            self.sub_action_completion_options = sub_action_completion_options

    @property
    def completion_options(self):
        """Gets the completion_options of this ConquestApiCompleteActionCommand.  # noqa: E501


        :return: The completion_options of this ConquestApiCompleteActionCommand.  # noqa: E501
        :rtype: ConquestApiActionCompletionOptions
        """
        return self._completion_options

    @completion_options.setter
    def completion_options(self, completion_options):
        """Sets the completion_options of this ConquestApiCompleteActionCommand.


        :param completion_options: The completion_options of this ConquestApiCompleteActionCommand.  # noqa: E501
        :type: ConquestApiActionCompletionOptions
        """

        self._completion_options = completion_options

    @property
    def sub_action_completion_options(self):
        """Gets the sub_action_completion_options of this ConquestApiCompleteActionCommand.  # noqa: E501


        :return: The sub_action_completion_options of this ConquestApiCompleteActionCommand.  # noqa: E501
        :rtype: list[ConquestApiActionCompletionOptions]
        """
        return self._sub_action_completion_options

    @sub_action_completion_options.setter
    def sub_action_completion_options(self, sub_action_completion_options):
        """Sets the sub_action_completion_options of this ConquestApiCompleteActionCommand.


        :param sub_action_completion_options: The sub_action_completion_options of this ConquestApiCompleteActionCommand.  # noqa: E501
        :type: list[ConquestApiActionCompletionOptions]
        """

        self._sub_action_completion_options = sub_action_completion_options

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
        if issubclass(ConquestApiCompleteActionCommand, dict):
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
        if not isinstance(other, ConquestApiCompleteActionCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
