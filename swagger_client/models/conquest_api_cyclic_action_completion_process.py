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

class ConquestApiCyclicActionCompletionProcess(object):
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
        'next_cycle_due_date': 'datetime'
    }

    attribute_map = {
        'next_cycle_due_date': 'NextCycleDueDate'
    }

    def __init__(self, next_cycle_due_date=None):  # noqa: E501
        """ConquestApiCyclicActionCompletionProcess - a model defined in Swagger"""  # noqa: E501
        self._next_cycle_due_date = None
        self.discriminator = None
        if next_cycle_due_date is not None:
            self.next_cycle_due_date = next_cycle_due_date

    @property
    def next_cycle_due_date(self):
        """Gets the next_cycle_due_date of this ConquestApiCyclicActionCompletionProcess.  # noqa: E501


        :return: The next_cycle_due_date of this ConquestApiCyclicActionCompletionProcess.  # noqa: E501
        :rtype: datetime
        """
        return self._next_cycle_due_date

    @next_cycle_due_date.setter
    def next_cycle_due_date(self, next_cycle_due_date):
        """Sets the next_cycle_due_date of this ConquestApiCyclicActionCompletionProcess.


        :param next_cycle_due_date: The next_cycle_due_date of this ConquestApiCyclicActionCompletionProcess.  # noqa: E501
        :type: datetime
        """

        self._next_cycle_due_date = next_cycle_due_date

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
        if issubclass(ConquestApiCyclicActionCompletionProcess, dict):
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
        if not isinstance(other, ConquestApiCyclicActionCompletionProcess):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
