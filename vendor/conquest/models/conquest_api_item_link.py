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


class ConquestApiItemLink(object):
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
        'icon_address': 'str',
        'link_description': 'str',
        'object_key': 'ConquestApiObjectKey',
        'parameters': 'str'
    }

    attribute_map = {
        'icon_address': 'IconAddress',
        'link_description': 'LinkDescription',
        'object_key': 'ObjectKey',
        'parameters': 'Parameters'
    }

    def __init__(self, icon_address=None, link_description=None, object_key=None, parameters=None, _configuration=None):  # noqa: E501
        """ConquestApiItemLink - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._icon_address = None
        self._link_description = None
        self._object_key = None
        self._parameters = None
        self.discriminator = None

        if icon_address is not None:
            self.icon_address = icon_address
        if link_description is not None:
            self.link_description = link_description
        if object_key is not None:
            self.object_key = object_key
        if parameters is not None:
            self.parameters = parameters

    @property
    def icon_address(self):
        """Gets the icon_address of this ConquestApiItemLink.  # noqa: E501


        :return: The icon_address of this ConquestApiItemLink.  # noqa: E501
        :rtype: str
        """
        return self._icon_address

    @icon_address.setter
    def icon_address(self, icon_address):
        """Sets the icon_address of this ConquestApiItemLink.


        :param icon_address: The icon_address of this ConquestApiItemLink.  # noqa: E501
        :type: str
        """

        self._icon_address = icon_address

    @property
    def link_description(self):
        """Gets the link_description of this ConquestApiItemLink.  # noqa: E501


        :return: The link_description of this ConquestApiItemLink.  # noqa: E501
        :rtype: str
        """
        return self._link_description

    @link_description.setter
    def link_description(self, link_description):
        """Sets the link_description of this ConquestApiItemLink.


        :param link_description: The link_description of this ConquestApiItemLink.  # noqa: E501
        :type: str
        """

        self._link_description = link_description

    @property
    def object_key(self):
        """Gets the object_key of this ConquestApiItemLink.  # noqa: E501


        :return: The object_key of this ConquestApiItemLink.  # noqa: E501
        :rtype: ConquestApiObjectKey
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        """Sets the object_key of this ConquestApiItemLink.


        :param object_key: The object_key of this ConquestApiItemLink.  # noqa: E501
        :type: ConquestApiObjectKey
        """

        self._object_key = object_key

    @property
    def parameters(self):
        """Gets the parameters of this ConquestApiItemLink.  # noqa: E501


        :return: The parameters of this ConquestApiItemLink.  # noqa: E501
        :rtype: str
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ConquestApiItemLink.


        :param parameters: The parameters of this ConquestApiItemLink.  # noqa: E501
        :type: str
        """

        self._parameters = parameters

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
        if issubclass(ConquestApiItemLink, dict):
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
        if not isinstance(other, ConquestApiItemLink):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiItemLink):
            return True

        return self.to_dict() != other.to_dict()
