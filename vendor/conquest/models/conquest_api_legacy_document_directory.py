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


class ConquestApiLegacyDocumentDirectory(object):
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
        'description': 'str',
        'enabled': 'bool',
        'mount': 'str',
        'path': 'str',
        'token': 'str'
    }

    attribute_map = {
        'description': 'description',
        'enabled': 'enabled',
        'mount': 'mount',
        'path': 'path',
        'token': 'token'
    }

    def __init__(self, description=None, enabled=None, mount=None, path=None, token=None, _configuration=None):  # noqa: E501
        """ConquestApiLegacyDocumentDirectory - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._enabled = None
        self._mount = None
        self._path = None
        self._token = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if mount is not None:
            self.mount = mount
        if path is not None:
            self.path = path
        if token is not None:
            self.token = token

    @property
    def description(self):
        """Gets the description of this ConquestApiLegacyDocumentDirectory.  # noqa: E501


        :return: The description of this ConquestApiLegacyDocumentDirectory.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConquestApiLegacyDocumentDirectory.


        :param description: The description of this ConquestApiLegacyDocumentDirectory.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this ConquestApiLegacyDocumentDirectory.  # noqa: E501


        :return: The enabled of this ConquestApiLegacyDocumentDirectory.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ConquestApiLegacyDocumentDirectory.


        :param enabled: The enabled of this ConquestApiLegacyDocumentDirectory.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def mount(self):
        """Gets the mount of this ConquestApiLegacyDocumentDirectory.  # noqa: E501


        :return: The mount of this ConquestApiLegacyDocumentDirectory.  # noqa: E501
        :rtype: str
        """
        return self._mount

    @mount.setter
    def mount(self, mount):
        """Sets the mount of this ConquestApiLegacyDocumentDirectory.


        :param mount: The mount of this ConquestApiLegacyDocumentDirectory.  # noqa: E501
        :type: str
        """

        self._mount = mount

    @property
    def path(self):
        """Gets the path of this ConquestApiLegacyDocumentDirectory.  # noqa: E501


        :return: The path of this ConquestApiLegacyDocumentDirectory.  # noqa: E501
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ConquestApiLegacyDocumentDirectory.


        :param path: The path of this ConquestApiLegacyDocumentDirectory.  # noqa: E501
        :type: str
        """

        self._path = path

    @property
    def token(self):
        """Gets the token of this ConquestApiLegacyDocumentDirectory.  # noqa: E501


        :return: The token of this ConquestApiLegacyDocumentDirectory.  # noqa: E501
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this ConquestApiLegacyDocumentDirectory.


        :param token: The token of this ConquestApiLegacyDocumentDirectory.  # noqa: E501
        :type: str
        """

        self._token = token

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
        if issubclass(ConquestApiLegacyDocumentDirectory, dict):
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
        if not isinstance(other, ConquestApiLegacyDocumentDirectory):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiLegacyDocumentDirectory):
            return True

        return self.to_dict() != other.to_dict()