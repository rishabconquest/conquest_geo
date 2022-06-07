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

class ConquestApiCustomHyperlink(object):
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
        'custom_hyperlink_id': 'str',
        'is_available': 'bool',
        'is_enabled': 'bool',
        'link': 'str',
        'title': 'str'
    }

    attribute_map = {
        'custom_hyperlink_id': 'CustomHyperlinkID',
        'is_available': 'IsAvailable',
        'is_enabled': 'IsEnabled',
        'link': 'Link',
        'title': 'Title'
    }

    def __init__(self, custom_hyperlink_id=None, is_available=None, is_enabled=None, link=None, title=None):  # noqa: E501
        """ConquestApiCustomHyperlink - a model defined in Swagger"""  # noqa: E501
        self._custom_hyperlink_id = None
        self._is_available = None
        self._is_enabled = None
        self._link = None
        self._title = None
        self.discriminator = None
        if custom_hyperlink_id is not None:
            self.custom_hyperlink_id = custom_hyperlink_id
        if is_available is not None:
            self.is_available = is_available
        if is_enabled is not None:
            self.is_enabled = is_enabled
        if link is not None:
            self.link = link
        if title is not None:
            self.title = title

    @property
    def custom_hyperlink_id(self):
        """Gets the custom_hyperlink_id of this ConquestApiCustomHyperlink.  # noqa: E501


        :return: The custom_hyperlink_id of this ConquestApiCustomHyperlink.  # noqa: E501
        :rtype: str
        """
        return self._custom_hyperlink_id

    @custom_hyperlink_id.setter
    def custom_hyperlink_id(self, custom_hyperlink_id):
        """Sets the custom_hyperlink_id of this ConquestApiCustomHyperlink.


        :param custom_hyperlink_id: The custom_hyperlink_id of this ConquestApiCustomHyperlink.  # noqa: E501
        :type: str
        """

        self._custom_hyperlink_id = custom_hyperlink_id

    @property
    def is_available(self):
        """Gets the is_available of this ConquestApiCustomHyperlink.  # noqa: E501


        :return: The is_available of this ConquestApiCustomHyperlink.  # noqa: E501
        :rtype: bool
        """
        return self._is_available

    @is_available.setter
    def is_available(self, is_available):
        """Sets the is_available of this ConquestApiCustomHyperlink.


        :param is_available: The is_available of this ConquestApiCustomHyperlink.  # noqa: E501
        :type: bool
        """

        self._is_available = is_available

    @property
    def is_enabled(self):
        """Gets the is_enabled of this ConquestApiCustomHyperlink.  # noqa: E501


        :return: The is_enabled of this ConquestApiCustomHyperlink.  # noqa: E501
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """Sets the is_enabled of this ConquestApiCustomHyperlink.


        :param is_enabled: The is_enabled of this ConquestApiCustomHyperlink.  # noqa: E501
        :type: bool
        """

        self._is_enabled = is_enabled

    @property
    def link(self):
        """Gets the link of this ConquestApiCustomHyperlink.  # noqa: E501


        :return: The link of this ConquestApiCustomHyperlink.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this ConquestApiCustomHyperlink.


        :param link: The link of this ConquestApiCustomHyperlink.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def title(self):
        """Gets the title of this ConquestApiCustomHyperlink.  # noqa: E501


        :return: The title of this ConquestApiCustomHyperlink.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ConquestApiCustomHyperlink.


        :param title: The title of this ConquestApiCustomHyperlink.  # noqa: E501
        :type: str
        """

        self._title = title

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
        if issubclass(ConquestApiCustomHyperlink, dict):
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
        if not isinstance(other, ConquestApiCustomHyperlink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other