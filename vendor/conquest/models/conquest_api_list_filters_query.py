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


class ConquestApiListFiltersQuery(object):
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
        'context': 'str',
        'filter_type': 'ConquestApiFilterType',
        'for_mobile': 'bool'
    }

    attribute_map = {
        'context': 'Context',
        'filter_type': 'FilterType',
        'for_mobile': 'ForMobile'
    }

    def __init__(self, context=None, filter_type=None, for_mobile=None, _configuration=None):  # noqa: E501
        """ConquestApiListFiltersQuery - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._context = None
        self._filter_type = None
        self._for_mobile = None
        self.discriminator = None

        if context is not None:
            self.context = context
        if filter_type is not None:
            self.filter_type = filter_type
        if for_mobile is not None:
            self.for_mobile = for_mobile

    @property
    def context(self):
        """Gets the context of this ConquestApiListFiltersQuery.  # noqa: E501


        :return: The context of this ConquestApiListFiltersQuery.  # noqa: E501
        :rtype: str
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this ConquestApiListFiltersQuery.


        :param context: The context of this ConquestApiListFiltersQuery.  # noqa: E501
        :type: str
        """

        self._context = context

    @property
    def filter_type(self):
        """Gets the filter_type of this ConquestApiListFiltersQuery.  # noqa: E501


        :return: The filter_type of this ConquestApiListFiltersQuery.  # noqa: E501
        :rtype: ConquestApiFilterType
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """Sets the filter_type of this ConquestApiListFiltersQuery.


        :param filter_type: The filter_type of this ConquestApiListFiltersQuery.  # noqa: E501
        :type: ConquestApiFilterType
        """

        self._filter_type = filter_type

    @property
    def for_mobile(self):
        """Gets the for_mobile of this ConquestApiListFiltersQuery.  # noqa: E501


        :return: The for_mobile of this ConquestApiListFiltersQuery.  # noqa: E501
        :rtype: bool
        """
        return self._for_mobile

    @for_mobile.setter
    def for_mobile(self, for_mobile):
        """Sets the for_mobile of this ConquestApiListFiltersQuery.


        :param for_mobile: The for_mobile of this ConquestApiListFiltersQuery.  # noqa: E501
        :type: bool
        """

        self._for_mobile = for_mobile

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
        if issubclass(ConquestApiListFiltersQuery, dict):
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
        if not isinstance(other, ConquestApiListFiltersQuery):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiListFiltersQuery):
            return True

        return self.to_dict() != other.to_dict()
