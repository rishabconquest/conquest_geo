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


class ConquestApiAddDocumentResults(object):
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
        'add_document_results_list': 'list[ConquestApiAddDocumentResult]'
    }

    attribute_map = {
        'add_document_results_list': 'AddDocumentResultsList'
    }

    def __init__(self, add_document_results_list=None, _configuration=None):  # noqa: E501
        """ConquestApiAddDocumentResults - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._add_document_results_list = None
        self.discriminator = None

        if add_document_results_list is not None:
            self.add_document_results_list = add_document_results_list

    @property
    def add_document_results_list(self):
        """Gets the add_document_results_list of this ConquestApiAddDocumentResults.  # noqa: E501


        :return: The add_document_results_list of this ConquestApiAddDocumentResults.  # noqa: E501
        :rtype: list[ConquestApiAddDocumentResult]
        """
        return self._add_document_results_list

    @add_document_results_list.setter
    def add_document_results_list(self, add_document_results_list):
        """Sets the add_document_results_list of this ConquestApiAddDocumentResults.


        :param add_document_results_list: The add_document_results_list of this ConquestApiAddDocumentResults.  # noqa: E501
        :type: list[ConquestApiAddDocumentResult]
        """

        self._add_document_results_list = add_document_results_list

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
        if issubclass(ConquestApiAddDocumentResults, dict):
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
        if not isinstance(other, ConquestApiAddDocumentResults):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiAddDocumentResults):
            return True

        return self.to_dict() != other.to_dict()
