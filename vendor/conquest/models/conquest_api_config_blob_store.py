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


class ConquestApiConfigBlobStore(object):
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
        'blob_store_mode': 'ConquestApiConfigBlobStoreMode',
        'description': 'str',
        'enabled': 'bool',
        'mount': 'str',
        'permissions': 'list[str]',
        'properties': 'dict(str, str)',
        'type': 'str'
    }

    attribute_map = {
        'blob_store_mode': 'blob_store_mode',
        'description': 'description',
        'enabled': 'enabled',
        'mount': 'mount',
        'permissions': 'permissions',
        'properties': 'properties',
        'type': 'type'
    }

    def __init__(self, blob_store_mode=None, description=None, enabled=None, mount=None, permissions=None, properties=None, type=None, _configuration=None):  # noqa: E501
        """ConquestApiConfigBlobStore - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._blob_store_mode = None
        self._description = None
        self._enabled = None
        self._mount = None
        self._permissions = None
        self._properties = None
        self._type = None
        self.discriminator = None

        if blob_store_mode is not None:
            self.blob_store_mode = blob_store_mode
        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if mount is not None:
            self.mount = mount
        if permissions is not None:
            self.permissions = permissions
        if properties is not None:
            self.properties = properties
        if type is not None:
            self.type = type

    @property
    def blob_store_mode(self):
        """Gets the blob_store_mode of this ConquestApiConfigBlobStore.  # noqa: E501


        :return: The blob_store_mode of this ConquestApiConfigBlobStore.  # noqa: E501
        :rtype: ConquestApiConfigBlobStoreMode
        """
        return self._blob_store_mode

    @blob_store_mode.setter
    def blob_store_mode(self, blob_store_mode):
        """Sets the blob_store_mode of this ConquestApiConfigBlobStore.


        :param blob_store_mode: The blob_store_mode of this ConquestApiConfigBlobStore.  # noqa: E501
        :type: ConquestApiConfigBlobStoreMode
        """

        self._blob_store_mode = blob_store_mode

    @property
    def description(self):
        """Gets the description of this ConquestApiConfigBlobStore.  # noqa: E501


        :return: The description of this ConquestApiConfigBlobStore.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConquestApiConfigBlobStore.


        :param description: The description of this ConquestApiConfigBlobStore.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this ConquestApiConfigBlobStore.  # noqa: E501


        :return: The enabled of this ConquestApiConfigBlobStore.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ConquestApiConfigBlobStore.


        :param enabled: The enabled of this ConquestApiConfigBlobStore.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def mount(self):
        """Gets the mount of this ConquestApiConfigBlobStore.  # noqa: E501


        :return: The mount of this ConquestApiConfigBlobStore.  # noqa: E501
        :rtype: str
        """
        return self._mount

    @mount.setter
    def mount(self, mount):
        """Sets the mount of this ConquestApiConfigBlobStore.


        :param mount: The mount of this ConquestApiConfigBlobStore.  # noqa: E501
        :type: str
        """

        self._mount = mount

    @property
    def permissions(self):
        """Gets the permissions of this ConquestApiConfigBlobStore.  # noqa: E501


        :return: The permissions of this ConquestApiConfigBlobStore.  # noqa: E501
        :rtype: list[str]
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this ConquestApiConfigBlobStore.


        :param permissions: The permissions of this ConquestApiConfigBlobStore.  # noqa: E501
        :type: list[str]
        """

        self._permissions = permissions

    @property
    def properties(self):
        """Gets the properties of this ConquestApiConfigBlobStore.  # noqa: E501


        :return: The properties of this ConquestApiConfigBlobStore.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ConquestApiConfigBlobStore.


        :param properties: The properties of this ConquestApiConfigBlobStore.  # noqa: E501
        :type: dict(str, str)
        """

        self._properties = properties

    @property
    def type(self):
        """Gets the type of this ConquestApiConfigBlobStore.  # noqa: E501


        :return: The type of this ConquestApiConfigBlobStore.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConquestApiConfigBlobStore.


        :param type: The type of this ConquestApiConfigBlobStore.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(ConquestApiConfigBlobStore, dict):
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
        if not isinstance(other, ConquestApiConfigBlobStore):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiConfigBlobStore):
            return True

        return self.to_dict() != other.to_dict()
