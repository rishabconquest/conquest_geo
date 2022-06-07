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

class ConquestApiObjectPermission(object):
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
        'object_description': 'str',
        'object_type': 'ConquestApiObjectType',
        'permission': 'ConquestApiPermission'
    }

    attribute_map = {
        'account_id': 'AccountID',
        'object_description': 'ObjectDescription',
        'object_type': 'ObjectType',
        'permission': 'Permission'
    }

    def __init__(self, account_id=None, object_description=None, object_type=None, permission=None):  # noqa: E501
        """ConquestApiObjectPermission - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._object_description = None
        self._object_type = None
        self._permission = None
        self.discriminator = None
        if account_id is not None:
            self.account_id = account_id
        if object_description is not None:
            self.object_description = object_description
        if object_type is not None:
            self.object_type = object_type
        if permission is not None:
            self.permission = permission

    @property
    def account_id(self):
        """Gets the account_id of this ConquestApiObjectPermission.  # noqa: E501


        :return: The account_id of this ConquestApiObjectPermission.  # noqa: E501
        :rtype: ConquestApiAccountID
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this ConquestApiObjectPermission.


        :param account_id: The account_id of this ConquestApiObjectPermission.  # noqa: E501
        :type: ConquestApiAccountID
        """

        self._account_id = account_id

    @property
    def object_description(self):
        """Gets the object_description of this ConquestApiObjectPermission.  # noqa: E501


        :return: The object_description of this ConquestApiObjectPermission.  # noqa: E501
        :rtype: str
        """
        return self._object_description

    @object_description.setter
    def object_description(self, object_description):
        """Sets the object_description of this ConquestApiObjectPermission.


        :param object_description: The object_description of this ConquestApiObjectPermission.  # noqa: E501
        :type: str
        """

        self._object_description = object_description

    @property
    def object_type(self):
        """Gets the object_type of this ConquestApiObjectPermission.  # noqa: E501


        :return: The object_type of this ConquestApiObjectPermission.  # noqa: E501
        :rtype: ConquestApiObjectType
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this ConquestApiObjectPermission.


        :param object_type: The object_type of this ConquestApiObjectPermission.  # noqa: E501
        :type: ConquestApiObjectType
        """

        self._object_type = object_type

    @property
    def permission(self):
        """Gets the permission of this ConquestApiObjectPermission.  # noqa: E501


        :return: The permission of this ConquestApiObjectPermission.  # noqa: E501
        :rtype: ConquestApiPermission
        """
        return self._permission

    @permission.setter
    def permission(self, permission):
        """Sets the permission of this ConquestApiObjectPermission.


        :param permission: The permission of this ConquestApiObjectPermission.  # noqa: E501
        :type: ConquestApiPermission
        """

        self._permission = permission

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
        if issubclass(ConquestApiObjectPermission, dict):
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
        if not isinstance(other, ConquestApiObjectPermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other