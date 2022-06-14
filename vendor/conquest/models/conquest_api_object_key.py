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


class ConquestApiObjectKey(object):
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
        'int32_value': 'int',
        'object_type': 'ConquestApiObjectType',
        'string_value': 'str',
        'timestamp_value': 'datetime'
    }

    attribute_map = {
        'int32_value': 'int32Value',
        'object_type': 'objectType',
        'string_value': 'stringValue',
        'timestamp_value': 'timestampValue'
    }

    def __init__(self, int32_value=None, object_type=None, string_value=None, timestamp_value=None, _configuration=None):  # noqa: E501
        """ConquestApiObjectKey - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._int32_value = None
        self._object_type = None
        self._string_value = None
        self._timestamp_value = None
        self.discriminator = None

        if int32_value is not None:
            self.int32_value = int32_value
        if object_type is not None:
            self.object_type = object_type
        if string_value is not None:
            self.string_value = string_value
        if timestamp_value is not None:
            self.timestamp_value = timestamp_value

    @property
    def int32_value(self):
        """Gets the int32_value of this ConquestApiObjectKey.  # noqa: E501

        Choose one of 'int32Value', 'stringValue' and 'timestampValue'.  Typically, an id is a unary key with the int type and only this needs to be provided.  # noqa: E501

        :return: The int32_value of this ConquestApiObjectKey.  # noqa: E501
        :rtype: int
        """
        return self._int32_value

    @int32_value.setter
    def int32_value(self, int32_value):
        """Sets the int32_value of this ConquestApiObjectKey.

        Choose one of 'int32Value', 'stringValue' and 'timestampValue'.  Typically, an id is a unary key with the int type and only this needs to be provided.  # noqa: E501

        :param int32_value: The int32_value of this ConquestApiObjectKey.  # noqa: E501
        :type: int
        """

        self._int32_value = int32_value

    @property
    def object_type(self):
        """Gets the object_type of this ConquestApiObjectKey.  # noqa: E501


        :return: The object_type of this ConquestApiObjectKey.  # noqa: E501
        :rtype: ConquestApiObjectType
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this ConquestApiObjectKey.


        :param object_type: The object_type of this ConquestApiObjectKey.  # noqa: E501
        :type: ConquestApiObjectType
        """

        self._object_type = object_type

    @property
    def string_value(self):
        """Gets the string_value of this ConquestApiObjectKey.  # noqa: E501

        Choose one of 'int32Value', 'stringValue' and 'timestampValue'.  Not every id can be an integer, in the odd case, a 'stringValue' will be used instead.  A guid, string like a uri, or an encoded composite key, eg \"(DefectID,InspectionID)\" when the ObjectType is DefectHistory  # noqa: E501

        :return: The string_value of this ConquestApiObjectKey.  # noqa: E501
        :rtype: str
        """
        return self._string_value

    @string_value.setter
    def string_value(self, string_value):
        """Sets the string_value of this ConquestApiObjectKey.

        Choose one of 'int32Value', 'stringValue' and 'timestampValue'.  Not every id can be an integer, in the odd case, a 'stringValue' will be used instead.  A guid, string like a uri, or an encoded composite key, eg \"(DefectID,InspectionID)\" when the ObjectType is DefectHistory  # noqa: E501

        :param string_value: The string_value of this ConquestApiObjectKey.  # noqa: E501
        :type: str
        """

        self._string_value = string_value

    @property
    def timestamp_value(self):
        """Gets the timestamp_value of this ConquestApiObjectKey.  # noqa: E501

        Choose one of 'int32Value', 'stringValue' and 'timestampValue'.  Timestamp as an id is typically used to reference a new object that does not yet have an id.  NOTE: Although 'oneof' should mean JSON clients do not serialize this if it's not set.       Unfortunately, this is not always the case, so please make sure you JSON client       doesn't serialize this when not set.  # noqa: E501

        :return: The timestamp_value of this ConquestApiObjectKey.  # noqa: E501
        :rtype: datetime
        """
        return self._timestamp_value

    @timestamp_value.setter
    def timestamp_value(self, timestamp_value):
        """Sets the timestamp_value of this ConquestApiObjectKey.

        Choose one of 'int32Value', 'stringValue' and 'timestampValue'.  Timestamp as an id is typically used to reference a new object that does not yet have an id.  NOTE: Although 'oneof' should mean JSON clients do not serialize this if it's not set.       Unfortunately, this is not always the case, so please make sure you JSON client       doesn't serialize this when not set.  # noqa: E501

        :param timestamp_value: The timestamp_value of this ConquestApiObjectKey.  # noqa: E501
        :type: datetime
        """

        self._timestamp_value = timestamp_value

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
        if issubclass(ConquestApiObjectKey, dict):
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
        if not isinstance(other, ConquestApiObjectKey):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiObjectKey):
            return True

        return self.to_dict() != other.to_dict()
