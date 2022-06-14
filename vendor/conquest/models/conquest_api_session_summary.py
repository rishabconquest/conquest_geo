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


class ConquestApiSessionSummary(object):
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
        'api_version': 'str',
        'application_database': 'str',
        'application_full_name': 'str',
        'application_username': 'str',
        'is_admin': 'bool',
        'is_production_application': 'bool',
        'is_production_database': 'bool',
        'licence_type': 'str',
        'username': 'str'
    }

    attribute_map = {
        'api_version': 'ApiVersion',
        'application_database': 'ApplicationDatabase',
        'application_full_name': 'ApplicationFullName',
        'application_username': 'ApplicationUsername',
        'is_admin': 'IsAdmin',
        'is_production_application': 'IsProductionApplication',
        'is_production_database': 'IsProductionDatabase',
        'licence_type': 'LicenceType',
        'username': 'Username'
    }

    def __init__(self, api_version=None, application_database=None, application_full_name=None, application_username=None, is_admin=None, is_production_application=None, is_production_database=None, licence_type=None, username=None, _configuration=None):  # noqa: E501
        """ConquestApiSessionSummary - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._api_version = None
        self._application_database = None
        self._application_full_name = None
        self._application_username = None
        self._is_admin = None
        self._is_production_application = None
        self._is_production_database = None
        self._licence_type = None
        self._username = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        if application_database is not None:
            self.application_database = application_database
        if application_full_name is not None:
            self.application_full_name = application_full_name
        if application_username is not None:
            self.application_username = application_username
        if is_admin is not None:
            self.is_admin = is_admin
        if is_production_application is not None:
            self.is_production_application = is_production_application
        if is_production_database is not None:
            self.is_production_database = is_production_database
        if licence_type is not None:
            self.licence_type = licence_type
        if username is not None:
            self.username = username

    @property
    def api_version(self):
        """Gets the api_version of this ConquestApiSessionSummary.  # noqa: E501


        :return: The api_version of this ConquestApiSessionSummary.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this ConquestApiSessionSummary.


        :param api_version: The api_version of this ConquestApiSessionSummary.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def application_database(self):
        """Gets the application_database of this ConquestApiSessionSummary.  # noqa: E501


        :return: The application_database of this ConquestApiSessionSummary.  # noqa: E501
        :rtype: str
        """
        return self._application_database

    @application_database.setter
    def application_database(self, application_database):
        """Sets the application_database of this ConquestApiSessionSummary.


        :param application_database: The application_database of this ConquestApiSessionSummary.  # noqa: E501
        :type: str
        """

        self._application_database = application_database

    @property
    def application_full_name(self):
        """Gets the application_full_name of this ConquestApiSessionSummary.  # noqa: E501


        :return: The application_full_name of this ConquestApiSessionSummary.  # noqa: E501
        :rtype: str
        """
        return self._application_full_name

    @application_full_name.setter
    def application_full_name(self, application_full_name):
        """Sets the application_full_name of this ConquestApiSessionSummary.


        :param application_full_name: The application_full_name of this ConquestApiSessionSummary.  # noqa: E501
        :type: str
        """

        self._application_full_name = application_full_name

    @property
    def application_username(self):
        """Gets the application_username of this ConquestApiSessionSummary.  # noqa: E501


        :return: The application_username of this ConquestApiSessionSummary.  # noqa: E501
        :rtype: str
        """
        return self._application_username

    @application_username.setter
    def application_username(self, application_username):
        """Sets the application_username of this ConquestApiSessionSummary.


        :param application_username: The application_username of this ConquestApiSessionSummary.  # noqa: E501
        :type: str
        """

        self._application_username = application_username

    @property
    def is_admin(self):
        """Gets the is_admin of this ConquestApiSessionSummary.  # noqa: E501


        :return: The is_admin of this ConquestApiSessionSummary.  # noqa: E501
        :rtype: bool
        """
        return self._is_admin

    @is_admin.setter
    def is_admin(self, is_admin):
        """Sets the is_admin of this ConquestApiSessionSummary.


        :param is_admin: The is_admin of this ConquestApiSessionSummary.  # noqa: E501
        :type: bool
        """

        self._is_admin = is_admin

    @property
    def is_production_application(self):
        """Gets the is_production_application of this ConquestApiSessionSummary.  # noqa: E501


        :return: The is_production_application of this ConquestApiSessionSummary.  # noqa: E501
        :rtype: bool
        """
        return self._is_production_application

    @is_production_application.setter
    def is_production_application(self, is_production_application):
        """Sets the is_production_application of this ConquestApiSessionSummary.


        :param is_production_application: The is_production_application of this ConquestApiSessionSummary.  # noqa: E501
        :type: bool
        """

        self._is_production_application = is_production_application

    @property
    def is_production_database(self):
        """Gets the is_production_database of this ConquestApiSessionSummary.  # noqa: E501


        :return: The is_production_database of this ConquestApiSessionSummary.  # noqa: E501
        :rtype: bool
        """
        return self._is_production_database

    @is_production_database.setter
    def is_production_database(self, is_production_database):
        """Sets the is_production_database of this ConquestApiSessionSummary.


        :param is_production_database: The is_production_database of this ConquestApiSessionSummary.  # noqa: E501
        :type: bool
        """

        self._is_production_database = is_production_database

    @property
    def licence_type(self):
        """Gets the licence_type of this ConquestApiSessionSummary.  # noqa: E501


        :return: The licence_type of this ConquestApiSessionSummary.  # noqa: E501
        :rtype: str
        """
        return self._licence_type

    @licence_type.setter
    def licence_type(self, licence_type):
        """Sets the licence_type of this ConquestApiSessionSummary.


        :param licence_type: The licence_type of this ConquestApiSessionSummary.  # noqa: E501
        :type: str
        """

        self._licence_type = licence_type

    @property
    def username(self):
        """Gets the username of this ConquestApiSessionSummary.  # noqa: E501


        :return: The username of this ConquestApiSessionSummary.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this ConquestApiSessionSummary.


        :param username: The username of this ConquestApiSessionSummary.  # noqa: E501
        :type: str
        """

        self._username = username

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
        if issubclass(ConquestApiSessionSummary, dict):
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
        if not isinstance(other, ConquestApiSessionSummary):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiSessionSummary):
            return True

        return self.to_dict() != other.to_dict()
