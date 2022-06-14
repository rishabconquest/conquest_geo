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


class ConquestApiMasterActionCompletionProcess(object):
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
        'create_master_for_repeatable_sub_actions': 'bool',
        'next_repeatable_date': 'datetime'
    }

    attribute_map = {
        'create_master_for_repeatable_sub_actions': 'CreateMasterForRepeatableSubActions',
        'next_repeatable_date': 'NextRepeatableDate'
    }

    def __init__(self, create_master_for_repeatable_sub_actions=None, next_repeatable_date=None, _configuration=None):  # noqa: E501
        """ConquestApiMasterActionCompletionProcess - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._create_master_for_repeatable_sub_actions = None
        self._next_repeatable_date = None
        self.discriminator = None

        if create_master_for_repeatable_sub_actions is not None:
            self.create_master_for_repeatable_sub_actions = create_master_for_repeatable_sub_actions
        if next_repeatable_date is not None:
            self.next_repeatable_date = next_repeatable_date

    @property
    def create_master_for_repeatable_sub_actions(self):
        """Gets the create_master_for_repeatable_sub_actions of this ConquestApiMasterActionCompletionProcess.  # noqa: E501


        :return: The create_master_for_repeatable_sub_actions of this ConquestApiMasterActionCompletionProcess.  # noqa: E501
        :rtype: bool
        """
        return self._create_master_for_repeatable_sub_actions

    @create_master_for_repeatable_sub_actions.setter
    def create_master_for_repeatable_sub_actions(self, create_master_for_repeatable_sub_actions):
        """Sets the create_master_for_repeatable_sub_actions of this ConquestApiMasterActionCompletionProcess.


        :param create_master_for_repeatable_sub_actions: The create_master_for_repeatable_sub_actions of this ConquestApiMasterActionCompletionProcess.  # noqa: E501
        :type: bool
        """

        self._create_master_for_repeatable_sub_actions = create_master_for_repeatable_sub_actions

    @property
    def next_repeatable_date(self):
        """Gets the next_repeatable_date of this ConquestApiMasterActionCompletionProcess.  # noqa: E501


        :return: The next_repeatable_date of this ConquestApiMasterActionCompletionProcess.  # noqa: E501
        :rtype: datetime
        """
        return self._next_repeatable_date

    @next_repeatable_date.setter
    def next_repeatable_date(self, next_repeatable_date):
        """Sets the next_repeatable_date of this ConquestApiMasterActionCompletionProcess.


        :param next_repeatable_date: The next_repeatable_date of this ConquestApiMasterActionCompletionProcess.  # noqa: E501
        :type: datetime
        """

        self._next_repeatable_date = next_repeatable_date

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
        if issubclass(ConquestApiMasterActionCompletionProcess, dict):
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
        if not isinstance(other, ConquestApiMasterActionCompletionProcess):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiMasterActionCompletionProcess):
            return True

        return self.to_dict() != other.to_dict()
