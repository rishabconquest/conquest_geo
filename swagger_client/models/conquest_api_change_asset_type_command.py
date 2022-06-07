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

class ConquestApiChangeAssetTypeCommand(object):
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
        'asset_id': 'int',
        'expiry_date': 'ConquestApiTimestampValue',
        'original_type_id': 'int',
        'transaction_date': 'ConquestApiTimestampValue',
        'type_id': 'int'
    }

    attribute_map = {
        'asset_id': 'AssetID',
        'expiry_date': 'ExpiryDate',
        'original_type_id': 'OriginalTypeID',
        'transaction_date': 'TransactionDate',
        'type_id': 'TypeID'
    }

    def __init__(self, asset_id=None, expiry_date=None, original_type_id=None, transaction_date=None, type_id=None):  # noqa: E501
        """ConquestApiChangeAssetTypeCommand - a model defined in Swagger"""  # noqa: E501
        self._asset_id = None
        self._expiry_date = None
        self._original_type_id = None
        self._transaction_date = None
        self._type_id = None
        self.discriminator = None
        if asset_id is not None:
            self.asset_id = asset_id
        if expiry_date is not None:
            self.expiry_date = expiry_date
        if original_type_id is not None:
            self.original_type_id = original_type_id
        if transaction_date is not None:
            self.transaction_date = transaction_date
        if type_id is not None:
            self.type_id = type_id

    @property
    def asset_id(self):
        """Gets the asset_id of this ConquestApiChangeAssetTypeCommand.  # noqa: E501


        :return: The asset_id of this ConquestApiChangeAssetTypeCommand.  # noqa: E501
        :rtype: int
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        """Sets the asset_id of this ConquestApiChangeAssetTypeCommand.


        :param asset_id: The asset_id of this ConquestApiChangeAssetTypeCommand.  # noqa: E501
        :type: int
        """

        self._asset_id = asset_id

    @property
    def expiry_date(self):
        """Gets the expiry_date of this ConquestApiChangeAssetTypeCommand.  # noqa: E501


        :return: The expiry_date of this ConquestApiChangeAssetTypeCommand.  # noqa: E501
        :rtype: ConquestApiTimestampValue
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this ConquestApiChangeAssetTypeCommand.


        :param expiry_date: The expiry_date of this ConquestApiChangeAssetTypeCommand.  # noqa: E501
        :type: ConquestApiTimestampValue
        """

        self._expiry_date = expiry_date

    @property
    def original_type_id(self):
        """Gets the original_type_id of this ConquestApiChangeAssetTypeCommand.  # noqa: E501


        :return: The original_type_id of this ConquestApiChangeAssetTypeCommand.  # noqa: E501
        :rtype: int
        """
        return self._original_type_id

    @original_type_id.setter
    def original_type_id(self, original_type_id):
        """Sets the original_type_id of this ConquestApiChangeAssetTypeCommand.


        :param original_type_id: The original_type_id of this ConquestApiChangeAssetTypeCommand.  # noqa: E501
        :type: int
        """

        self._original_type_id = original_type_id

    @property
    def transaction_date(self):
        """Gets the transaction_date of this ConquestApiChangeAssetTypeCommand.  # noqa: E501


        :return: The transaction_date of this ConquestApiChangeAssetTypeCommand.  # noqa: E501
        :rtype: ConquestApiTimestampValue
        """
        return self._transaction_date

    @transaction_date.setter
    def transaction_date(self, transaction_date):
        """Sets the transaction_date of this ConquestApiChangeAssetTypeCommand.


        :param transaction_date: The transaction_date of this ConquestApiChangeAssetTypeCommand.  # noqa: E501
        :type: ConquestApiTimestampValue
        """

        self._transaction_date = transaction_date

    @property
    def type_id(self):
        """Gets the type_id of this ConquestApiChangeAssetTypeCommand.  # noqa: E501


        :return: The type_id of this ConquestApiChangeAssetTypeCommand.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this ConquestApiChangeAssetTypeCommand.


        :param type_id: The type_id of this ConquestApiChangeAssetTypeCommand.  # noqa: E501
        :type: int
        """

        self._type_id = type_id

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
        if issubclass(ConquestApiChangeAssetTypeCommand, dict):
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
        if not isinstance(other, ConquestApiChangeAssetTypeCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
