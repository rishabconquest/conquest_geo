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

class ConquestApiActionCompletionDetails(object):
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
        'action': 'ConquestApiObjectHeader',
        'action_type': 'ConquestApiActionType',
        'actual_cost': 'ConquestApiDecimal',
        'asset': 'ConquestApiObjectHeader',
        'cost_type': 'ConquestApiCostType',
        'estimated_cost': 'ConquestApiDecimal',
        'is_repeatable': 'bool',
        'other_cost': 'ConquestApiDecimal'
    }

    attribute_map = {
        'action': 'Action',
        'action_type': 'ActionType',
        'actual_cost': 'ActualCost',
        'asset': 'Asset',
        'cost_type': 'CostType',
        'estimated_cost': 'EstimatedCost',
        'is_repeatable': 'IsRepeatable',
        'other_cost': 'OtherCost'
    }

    def __init__(self, action=None, action_type=None, actual_cost=None, asset=None, cost_type=None, estimated_cost=None, is_repeatable=None, other_cost=None):  # noqa: E501
        """ConquestApiActionCompletionDetails - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._action_type = None
        self._actual_cost = None
        self._asset = None
        self._cost_type = None
        self._estimated_cost = None
        self._is_repeatable = None
        self._other_cost = None
        self.discriminator = None
        if action is not None:
            self.action = action
        if action_type is not None:
            self.action_type = action_type
        if actual_cost is not None:
            self.actual_cost = actual_cost
        if asset is not None:
            self.asset = asset
        if cost_type is not None:
            self.cost_type = cost_type
        if estimated_cost is not None:
            self.estimated_cost = estimated_cost
        if is_repeatable is not None:
            self.is_repeatable = is_repeatable
        if other_cost is not None:
            self.other_cost = other_cost

    @property
    def action(self):
        """Gets the action of this ConquestApiActionCompletionDetails.  # noqa: E501


        :return: The action of this ConquestApiActionCompletionDetails.  # noqa: E501
        :rtype: ConquestApiObjectHeader
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ConquestApiActionCompletionDetails.


        :param action: The action of this ConquestApiActionCompletionDetails.  # noqa: E501
        :type: ConquestApiObjectHeader
        """

        self._action = action

    @property
    def action_type(self):
        """Gets the action_type of this ConquestApiActionCompletionDetails.  # noqa: E501


        :return: The action_type of this ConquestApiActionCompletionDetails.  # noqa: E501
        :rtype: ConquestApiActionType
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this ConquestApiActionCompletionDetails.


        :param action_type: The action_type of this ConquestApiActionCompletionDetails.  # noqa: E501
        :type: ConquestApiActionType
        """

        self._action_type = action_type

    @property
    def actual_cost(self):
        """Gets the actual_cost of this ConquestApiActionCompletionDetails.  # noqa: E501


        :return: The actual_cost of this ConquestApiActionCompletionDetails.  # noqa: E501
        :rtype: ConquestApiDecimal
        """
        return self._actual_cost

    @actual_cost.setter
    def actual_cost(self, actual_cost):
        """Sets the actual_cost of this ConquestApiActionCompletionDetails.


        :param actual_cost: The actual_cost of this ConquestApiActionCompletionDetails.  # noqa: E501
        :type: ConquestApiDecimal
        """

        self._actual_cost = actual_cost

    @property
    def asset(self):
        """Gets the asset of this ConquestApiActionCompletionDetails.  # noqa: E501


        :return: The asset of this ConquestApiActionCompletionDetails.  # noqa: E501
        :rtype: ConquestApiObjectHeader
        """
        return self._asset

    @asset.setter
    def asset(self, asset):
        """Sets the asset of this ConquestApiActionCompletionDetails.


        :param asset: The asset of this ConquestApiActionCompletionDetails.  # noqa: E501
        :type: ConquestApiObjectHeader
        """

        self._asset = asset

    @property
    def cost_type(self):
        """Gets the cost_type of this ConquestApiActionCompletionDetails.  # noqa: E501


        :return: The cost_type of this ConquestApiActionCompletionDetails.  # noqa: E501
        :rtype: ConquestApiCostType
        """
        return self._cost_type

    @cost_type.setter
    def cost_type(self, cost_type):
        """Sets the cost_type of this ConquestApiActionCompletionDetails.


        :param cost_type: The cost_type of this ConquestApiActionCompletionDetails.  # noqa: E501
        :type: ConquestApiCostType
        """

        self._cost_type = cost_type

    @property
    def estimated_cost(self):
        """Gets the estimated_cost of this ConquestApiActionCompletionDetails.  # noqa: E501


        :return: The estimated_cost of this ConquestApiActionCompletionDetails.  # noqa: E501
        :rtype: ConquestApiDecimal
        """
        return self._estimated_cost

    @estimated_cost.setter
    def estimated_cost(self, estimated_cost):
        """Sets the estimated_cost of this ConquestApiActionCompletionDetails.


        :param estimated_cost: The estimated_cost of this ConquestApiActionCompletionDetails.  # noqa: E501
        :type: ConquestApiDecimal
        """

        self._estimated_cost = estimated_cost

    @property
    def is_repeatable(self):
        """Gets the is_repeatable of this ConquestApiActionCompletionDetails.  # noqa: E501


        :return: The is_repeatable of this ConquestApiActionCompletionDetails.  # noqa: E501
        :rtype: bool
        """
        return self._is_repeatable

    @is_repeatable.setter
    def is_repeatable(self, is_repeatable):
        """Sets the is_repeatable of this ConquestApiActionCompletionDetails.


        :param is_repeatable: The is_repeatable of this ConquestApiActionCompletionDetails.  # noqa: E501
        :type: bool
        """

        self._is_repeatable = is_repeatable

    @property
    def other_cost(self):
        """Gets the other_cost of this ConquestApiActionCompletionDetails.  # noqa: E501


        :return: The other_cost of this ConquestApiActionCompletionDetails.  # noqa: E501
        :rtype: ConquestApiDecimal
        """
        return self._other_cost

    @other_cost.setter
    def other_cost(self, other_cost):
        """Sets the other_cost of this ConquestApiActionCompletionDetails.


        :param other_cost: The other_cost of this ConquestApiActionCompletionDetails.  # noqa: E501
        :type: ConquestApiDecimal
        """

        self._other_cost = other_cost

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
        if issubclass(ConquestApiActionCompletionDetails, dict):
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
        if not isinstance(other, ConquestApiActionCompletionDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
