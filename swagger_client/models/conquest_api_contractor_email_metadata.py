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

class ConquestApiContractorEmailMetadata(object):
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
        'email_address': 'str',
        'email_message': 'str',
        'email_subject': 'str'
    }

    attribute_map = {
        'email_address': 'EmailAddress',
        'email_message': 'EmailMessage',
        'email_subject': 'EmailSubject'
    }

    def __init__(self, email_address=None, email_message=None, email_subject=None):  # noqa: E501
        """ConquestApiContractorEmailMetadata - a model defined in Swagger"""  # noqa: E501
        self._email_address = None
        self._email_message = None
        self._email_subject = None
        self.discriminator = None
        if email_address is not None:
            self.email_address = email_address
        if email_message is not None:
            self.email_message = email_message
        if email_subject is not None:
            self.email_subject = email_subject

    @property
    def email_address(self):
        """Gets the email_address of this ConquestApiContractorEmailMetadata.  # noqa: E501


        :return: The email_address of this ConquestApiContractorEmailMetadata.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this ConquestApiContractorEmailMetadata.


        :param email_address: The email_address of this ConquestApiContractorEmailMetadata.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def email_message(self):
        """Gets the email_message of this ConquestApiContractorEmailMetadata.  # noqa: E501


        :return: The email_message of this ConquestApiContractorEmailMetadata.  # noqa: E501
        :rtype: str
        """
        return self._email_message

    @email_message.setter
    def email_message(self, email_message):
        """Sets the email_message of this ConquestApiContractorEmailMetadata.


        :param email_message: The email_message of this ConquestApiContractorEmailMetadata.  # noqa: E501
        :type: str
        """

        self._email_message = email_message

    @property
    def email_subject(self):
        """Gets the email_subject of this ConquestApiContractorEmailMetadata.  # noqa: E501


        :return: The email_subject of this ConquestApiContractorEmailMetadata.  # noqa: E501
        :rtype: str
        """
        return self._email_subject

    @email_subject.setter
    def email_subject(self, email_subject):
        """Sets the email_subject of this ConquestApiContractorEmailMetadata.


        :param email_subject: The email_subject of this ConquestApiContractorEmailMetadata.  # noqa: E501
        :type: str
        """

        self._email_subject = email_subject

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
        if issubclass(ConquestApiContractorEmailMetadata, dict):
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
        if not isinstance(other, ConquestApiContractorEmailMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
