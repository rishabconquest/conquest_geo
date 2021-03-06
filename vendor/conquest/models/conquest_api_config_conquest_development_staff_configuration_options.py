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


class ConquestApiConfigConquestDevelopmentStaffConfigurationOptions(object):
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
        'login_server_address': 'str',
        'rules_engine_address': 'str',
        'rules_engine_address_for_data_connector': 'str',
        'services_address': 'str'
    }

    attribute_map = {
        'login_server_address': 'login_server_address',
        'rules_engine_address': 'rules_engine_address',
        'rules_engine_address_for_data_connector': 'rules_engine_address_for_data_connector',
        'services_address': 'services_address'
    }

    def __init__(self, login_server_address=None, rules_engine_address=None, rules_engine_address_for_data_connector=None, services_address=None, _configuration=None):  # noqa: E501
        """ConquestApiConfigConquestDevelopmentStaffConfigurationOptions - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._login_server_address = None
        self._rules_engine_address = None
        self._rules_engine_address_for_data_connector = None
        self._services_address = None
        self.discriminator = None

        if login_server_address is not None:
            self.login_server_address = login_server_address
        if rules_engine_address is not None:
            self.rules_engine_address = rules_engine_address
        if rules_engine_address_for_data_connector is not None:
            self.rules_engine_address_for_data_connector = rules_engine_address_for_data_connector
        if services_address is not None:
            self.services_address = services_address

    @property
    def login_server_address(self):
        """Gets the login_server_address of this ConquestApiConfigConquestDevelopmentStaffConfigurationOptions.  # noqa: E501


        :return: The login_server_address of this ConquestApiConfigConquestDevelopmentStaffConfigurationOptions.  # noqa: E501
        :rtype: str
        """
        return self._login_server_address

    @login_server_address.setter
    def login_server_address(self, login_server_address):
        """Sets the login_server_address of this ConquestApiConfigConquestDevelopmentStaffConfigurationOptions.


        :param login_server_address: The login_server_address of this ConquestApiConfigConquestDevelopmentStaffConfigurationOptions.  # noqa: E501
        :type: str
        """

        self._login_server_address = login_server_address

    @property
    def rules_engine_address(self):
        """Gets the rules_engine_address of this ConquestApiConfigConquestDevelopmentStaffConfigurationOptions.  # noqa: E501

        rulesEngineAddress: (default = localhost:9090)   The address of the Conquest API Rules Engine. The Gateway forwards requests to this port.   !!IMPORTANT!! DO NOT EXPOSE THIS PORT TO THE INTERNET IT IS PRIVATE TO THE MACHINE  # noqa: E501

        :return: The rules_engine_address of this ConquestApiConfigConquestDevelopmentStaffConfigurationOptions.  # noqa: E501
        :rtype: str
        """
        return self._rules_engine_address

    @rules_engine_address.setter
    def rules_engine_address(self, rules_engine_address):
        """Sets the rules_engine_address of this ConquestApiConfigConquestDevelopmentStaffConfigurationOptions.

        rulesEngineAddress: (default = localhost:9090)   The address of the Conquest API Rules Engine. The Gateway forwards requests to this port.   !!IMPORTANT!! DO NOT EXPOSE THIS PORT TO THE INTERNET IT IS PRIVATE TO THE MACHINE  # noqa: E501

        :param rules_engine_address: The rules_engine_address of this ConquestApiConfigConquestDevelopmentStaffConfigurationOptions.  # noqa: E501
        :type: str
        """

        self._rules_engine_address = rules_engine_address

    @property
    def rules_engine_address_for_data_connector(self):
        """Gets the rules_engine_address_for_data_connector of this ConquestApiConfigConquestDevelopmentStaffConfigurationOptions.  # noqa: E501

        rulesEngineAddressForDataConnector: (default = localhost:9091)   The address of the Conquest API Rules Engine for DataConnector Service. The Gateway forwards requests to this port.   !!IMPORTANT!! DO NOT EXPOSE THIS PORT TO THE INTERNET IT IS PRIVATE TO THE MACHINE  # noqa: E501

        :return: The rules_engine_address_for_data_connector of this ConquestApiConfigConquestDevelopmentStaffConfigurationOptions.  # noqa: E501
        :rtype: str
        """
        return self._rules_engine_address_for_data_connector

    @rules_engine_address_for_data_connector.setter
    def rules_engine_address_for_data_connector(self, rules_engine_address_for_data_connector):
        """Sets the rules_engine_address_for_data_connector of this ConquestApiConfigConquestDevelopmentStaffConfigurationOptions.

        rulesEngineAddressForDataConnector: (default = localhost:9091)   The address of the Conquest API Rules Engine for DataConnector Service. The Gateway forwards requests to this port.   !!IMPORTANT!! DO NOT EXPOSE THIS PORT TO THE INTERNET IT IS PRIVATE TO THE MACHINE  # noqa: E501

        :param rules_engine_address_for_data_connector: The rules_engine_address_for_data_connector of this ConquestApiConfigConquestDevelopmentStaffConfigurationOptions.  # noqa: E501
        :type: str
        """

        self._rules_engine_address_for_data_connector = rules_engine_address_for_data_connector

    @property
    def services_address(self):
        """Gets the services_address of this ConquestApiConfigConquestDevelopmentStaffConfigurationOptions.  # noqa: E501


        :return: The services_address of this ConquestApiConfigConquestDevelopmentStaffConfigurationOptions.  # noqa: E501
        :rtype: str
        """
        return self._services_address

    @services_address.setter
    def services_address(self, services_address):
        """Sets the services_address of this ConquestApiConfigConquestDevelopmentStaffConfigurationOptions.


        :param services_address: The services_address of this ConquestApiConfigConquestDevelopmentStaffConfigurationOptions.  # noqa: E501
        :type: str
        """

        self._services_address = services_address

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
        if issubclass(ConquestApiConfigConquestDevelopmentStaffConfigurationOptions, dict):
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
        if not isinstance(other, ConquestApiConfigConquestDevelopmentStaffConfigurationOptions):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiConfigConquestDevelopmentStaffConfigurationOptions):
            return True

        return self.to_dict() != other.to_dict()
