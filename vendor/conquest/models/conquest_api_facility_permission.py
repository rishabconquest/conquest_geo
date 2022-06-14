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


class ConquestApiFacilityPermission(object):
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
        'account_id': 'ConquestApiAccountID',
        'asset_description': 'str',
        'asset_id': 'int'
    }

    attribute_map = {
        'account_id': 'AccountID',
        'asset_description': 'AssetDescription',
        'asset_id': 'AssetID'
    }

    def __init__(self, account_id=None, asset_description=None, asset_id=None, _configuration=None):  # noqa: E501
        """ConquestApiFacilityPermission - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._account_id = None
        self._asset_description = None
        self._asset_id = None
        self.discriminator = None

        if account_id is not None:
            self.account_id = account_id
        if asset_description is not None:
            self.asset_description = asset_description
        if asset_id is not None:
            self.asset_id = asset_id

    @property
    def account_id(self):
        """Gets the account_id of this ConquestApiFacilityPermission.  # noqa: E501


        :return: The account_id of this ConquestApiFacilityPermission.  # noqa: E501
        :rtype: ConquestApiAccountID
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ConquestApiFacilityPermission.


        :param account_id: The account_id of this ConquestApiFacilityPermission.  # noqa: E501
        :type: ConquestApiAccountID
        """

        self._account_id = account_id

    @property
    def asset_description(self):
        """Gets the asset_description of this ConquestApiFacilityPermission.  # noqa: E501


        :return: The asset_description of this ConquestApiFacilityPermission.  # noqa: E501
        :rtype: str
        """
        return self._asset_description

    @asset_description.setter
    def asset_description(self, asset_description):
        """Sets the asset_description of this ConquestApiFacilityPermission.


        :param asset_description: The asset_description of this ConquestApiFacilityPermission.  # noqa: E501
        :type: str
        """

        self._asset_description = asset_description

    @property
    def asset_id(self):
        """Gets the asset_id of this ConquestApiFacilityPermission.  # noqa: E501


        :return: The asset_id of this ConquestApiFacilityPermission.  # noqa: E501
        :rtype: int
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this ConquestApiFacilityPermission.


        :param asset_id: The asset_id of this ConquestApiFacilityPermission.  # noqa: E501
        :type: int
        """

        self._asset_id = asset_id

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
        if issubclass(ConquestApiFacilityPermission, dict):
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
        if not isinstance(other, ConquestApiFacilityPermission):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiFacilityPermission):
            return True

        return self.to_dict() != other.to_dict()
