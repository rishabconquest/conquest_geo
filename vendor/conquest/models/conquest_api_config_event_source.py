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


class ConquestApiConfigEventSource(object):
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
        'id': 'str',
        'properties': 'dict(str, str)',
        'type': 'str'
    }

    attribute_map = {
        'description': 'description',
        'enabled': 'enabled',
        'id': 'id',
        'properties': 'properties',
        'type': 'type'
    }

    def __init__(self, description=None, enabled=None, id=None, properties=None, type=None, _configuration=None):  # noqa: E501
        """ConquestApiConfigEventSource - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._enabled = None
        self._id = None
        self._properties = None
        self._type = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if enabled is not None:
            self.enabled = enabled
        if id is not None:
            self.id = id
        if properties is not None:
            self.properties = properties
        if type is not None:
            self.type = type

    @property
    def description(self):
        """Gets the description of this ConquestApiConfigEventSource.  # noqa: E501


        :return: The description of this ConquestApiConfigEventSource.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ConquestApiConfigEventSource.


        :param description: The description of this ConquestApiConfigEventSource.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def enabled(self):
        """Gets the enabled of this ConquestApiConfigEventSource.  # noqa: E501


        :return: The enabled of this ConquestApiConfigEventSource.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ConquestApiConfigEventSource.


        :param enabled: The enabled of this ConquestApiConfigEventSource.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def id(self):
        """Gets the id of this ConquestApiConfigEventSource.  # noqa: E501


        :return: The id of this ConquestApiConfigEventSource.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConquestApiConfigEventSource.


        :param id: The id of this ConquestApiConfigEventSource.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def properties(self):
        """Gets the properties of this ConquestApiConfigEventSource.  # noqa: E501


        :return: The properties of this ConquestApiConfigEventSource.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this ConquestApiConfigEventSource.


        :param properties: The properties of this ConquestApiConfigEventSource.  # noqa: E501
        :type: dict(str, str)
        """

        self._properties = properties

    @property
    def type(self):
        """Gets the type of this ConquestApiConfigEventSource.  # noqa: E501


        :return: The type of this ConquestApiConfigEventSource.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConquestApiConfigEventSource.


        :param type: The type of this ConquestApiConfigEventSource.  # noqa: E501
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
        if issubclass(ConquestApiConfigEventSource, dict):
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
        if not isinstance(other, ConquestApiConfigEventSource):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiConfigEventSource):
            return True

        return self.to_dict() != other.to_dict()