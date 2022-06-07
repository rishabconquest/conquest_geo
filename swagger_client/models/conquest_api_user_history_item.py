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

class ConquestApiUserHistoryItem(object):
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
        'last_used': 'datetime',
        'link': 'ConquestApiItemLink',
        'order': 'int'
    }

    attribute_map = {
        'last_used': 'LastUsed',
        'link': 'Link',
        'order': 'Order'
    }

    def __init__(self, last_used=None, link=None, order=None):  # noqa: E501
        """ConquestApiUserHistoryItem - a model defined in Swagger"""  # noqa: E501
        self._last_used = None
        self._link = None
        self._order = None
        self.discriminator = None
        if last_used is not None:
            self.last_used = last_used
        if link is not None:
            self.link = link
        if order is not None:
            self.order = order

    @property
    def last_used(self):
        """Gets the last_used of this ConquestApiUserHistoryItem.  # noqa: E501


        :return: The last_used of this ConquestApiUserHistoryItem.  # noqa: E501
        :rtype: datetime
        """
        return self._last_used

    @last_used.setter
    def last_used(self, last_used):
        """Sets the last_used of this ConquestApiUserHistoryItem.


        :param last_used: The last_used of this ConquestApiUserHistoryItem.  # noqa: E501
        :type: datetime
        """

        self._last_used = last_used

    @property
    def link(self):
        """Gets the link of this ConquestApiUserHistoryItem.  # noqa: E501


        :return: The link of this ConquestApiUserHistoryItem.  # noqa: E501
        :rtype: ConquestApiItemLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this ConquestApiUserHistoryItem.


        :param link: The link of this ConquestApiUserHistoryItem.  # noqa: E501
        :type: ConquestApiItemLink
        """

        self._link = link

    @property
    def order(self):
        """Gets the order of this ConquestApiUserHistoryItem.  # noqa: E501


        :return: The order of this ConquestApiUserHistoryItem.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ConquestApiUserHistoryItem.


        :param order: The order of this ConquestApiUserHistoryItem.  # noqa: E501
        :type: int
        """

        self._order = order

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
        if issubclass(ConquestApiUserHistoryItem, dict):
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
        if not isinstance(other, ConquestApiUserHistoryItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
