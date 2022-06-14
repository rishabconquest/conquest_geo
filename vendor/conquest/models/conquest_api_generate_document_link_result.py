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


class ConquestApiGenerateDocumentLinkResult(object):
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
        'link': 'str',
        'link_expire_time': 'datetime'
    }

    attribute_map = {
        'link': 'Link',
        'link_expire_time': 'LinkExpireTime'
    }

    def __init__(self, link=None, link_expire_time=None, _configuration=None):  # noqa: E501
        """ConquestApiGenerateDocumentLinkResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._link = None
        self._link_expire_time = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if link_expire_time is not None:
            self.link_expire_time = link_expire_time

    @property
    def link(self):
        """Gets the link of this ConquestApiGenerateDocumentLinkResult.  # noqa: E501

        Link is is an authenticated link. When applicable, the \"/download/document?object_type=...&object_id=...&document_id=...\" endpoint redirects you to (address in the Location header) to this same value.  # noqa: E501

        :return: The link of this ConquestApiGenerateDocumentLinkResult.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this ConquestApiGenerateDocumentLinkResult.

        Link is is an authenticated link. When applicable, the \"/download/document?object_type=...&object_id=...&document_id=...\" endpoint redirects you to (address in the Location header) to this same value.  # noqa: E501

        :param link: The link of this ConquestApiGenerateDocumentLinkResult.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def link_expire_time(self):
        """Gets the link_expire_time of this ConquestApiGenerateDocumentLinkResult.  # noqa: E501

        Not implemented, tentative. Links do have an expiry, assume 1 hour.  # noqa: E501

        :return: The link_expire_time of this ConquestApiGenerateDocumentLinkResult.  # noqa: E501
        :rtype: datetime
        """
        return self._link_expire_time

    @link_expire_time.setter
    def link_expire_time(self, link_expire_time):
        """Sets the link_expire_time of this ConquestApiGenerateDocumentLinkResult.

        Not implemented, tentative. Links do have an expiry, assume 1 hour.  # noqa: E501

        :param link_expire_time: The link_expire_time of this ConquestApiGenerateDocumentLinkResult.  # noqa: E501
        :type: datetime
        """

        self._link_expire_time = link_expire_time

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
        if issubclass(ConquestApiGenerateDocumentLinkResult, dict):
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
        if not isinstance(other, ConquestApiGenerateDocumentLinkResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiGenerateDocumentLinkResult):
            return True

        return self.to_dict() != other.to_dict()
