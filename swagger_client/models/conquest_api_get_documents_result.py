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

class ConquestApiGetDocumentsResult(object):
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
        'documents': 'list[ConquestApiDocument]'
    }

    attribute_map = {
        'documents': 'documents'
    }

    def __init__(self, documents=None):  # noqa: E501
        """ConquestApiGetDocumentsResult - a model defined in Swagger"""  # noqa: E501
        self._documents = None
        self.discriminator = None
        if documents is not None:
            self.documents = documents

    @property
    def documents(self):
        """Gets the documents of this ConquestApiGetDocumentsResult.  # noqa: E501


        :return: The documents of this ConquestApiGetDocumentsResult.  # noqa: E501
        :rtype: list[ConquestApiDocument]
        """
        return self._documents

    @documents.setter
    def documents(self, documents):
        """Sets the documents of this ConquestApiGetDocumentsResult.


        :param documents: The documents of this ConquestApiGetDocumentsResult.  # noqa: E501
        :type: list[ConquestApiDocument]
        """

        self._documents = documents

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
        if issubclass(ConquestApiGetDocumentsResult, dict):
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
        if not isinstance(other, ConquestApiGetDocumentsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
