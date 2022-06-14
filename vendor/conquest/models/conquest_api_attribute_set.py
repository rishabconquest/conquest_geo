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


class ConquestApiAttributeSet(object):
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
        'attribute_description': 'str',
        'attribute_id': 'int',
        'attribute_notes': 'str',
        'attribute_type': 'ConquestApiObjectType',
        'condition_type': 'ConquestApiConditionType',
        'fields': 'list[ConquestApiAttributeSetField]'
    }

    attribute_map = {
        'attribute_description': 'AttributeDescription',
        'attribute_id': 'AttributeID',
        'attribute_notes': 'AttributeNotes',
        'attribute_type': 'AttributeType',
        'condition_type': 'ConditionType',
        'fields': 'Fields'
    }

    def __init__(self, attribute_description=None, attribute_id=None, attribute_notes=None, attribute_type=None, condition_type=None, fields=None, _configuration=None):  # noqa: E501
        """ConquestApiAttributeSet - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._attribute_description = None
        self._attribute_id = None
        self._attribute_notes = None
        self._attribute_type = None
        self._condition_type = None
        self._fields = None
        self.discriminator = None

        if attribute_description is not None:
            self.attribute_description = attribute_description
        if attribute_id is not None:
            self.attribute_id = attribute_id
        if attribute_notes is not None:
            self.attribute_notes = attribute_notes
        if attribute_type is not None:
            self.attribute_type = attribute_type
        if condition_type is not None:
            self.condition_type = condition_type
        if fields is not None:
            self.fields = fields

    @property
    def attribute_description(self):
        """Gets the attribute_description of this ConquestApiAttributeSet.  # noqa: E501


        :return: The attribute_description of this ConquestApiAttributeSet.  # noqa: E501
        :rtype: str
        """
        return self._attribute_description

    @attribute_description.setter
    def attribute_description(self, attribute_description):
        """Sets the attribute_description of this ConquestApiAttributeSet.


        :param attribute_description: The attribute_description of this ConquestApiAttributeSet.  # noqa: E501
        :type: str
        """

        self._attribute_description = attribute_description

    @property
    def attribute_id(self):
        """Gets the attribute_id of this ConquestApiAttributeSet.  # noqa: E501


        :return: The attribute_id of this ConquestApiAttributeSet.  # noqa: E501
        :rtype: int
        """
        return self._attribute_id

    @attribute_id.setter
    def attribute_id(self, attribute_id):
        """Sets the attribute_id of this ConquestApiAttributeSet.


        :param attribute_id: The attribute_id of this ConquestApiAttributeSet.  # noqa: E501
        :type: int
        """

        self._attribute_id = attribute_id

    @property
    def attribute_notes(self):
        """Gets the attribute_notes of this ConquestApiAttributeSet.  # noqa: E501


        :return: The attribute_notes of this ConquestApiAttributeSet.  # noqa: E501
        :rtype: str
        """
        return self._attribute_notes

    @attribute_notes.setter
    def attribute_notes(self, attribute_notes):
        """Sets the attribute_notes of this ConquestApiAttributeSet.


        :param attribute_notes: The attribute_notes of this ConquestApiAttributeSet.  # noqa: E501
        :type: str
        """

        self._attribute_notes = attribute_notes

    @property
    def attribute_type(self):
        """Gets the attribute_type of this ConquestApiAttributeSet.  # noqa: E501


        :return: The attribute_type of this ConquestApiAttributeSet.  # noqa: E501
        :rtype: ConquestApiObjectType
        """
        return self._attribute_type

    @attribute_type.setter
    def attribute_type(self, attribute_type):
        """Sets the attribute_type of this ConquestApiAttributeSet.


        :param attribute_type: The attribute_type of this ConquestApiAttributeSet.  # noqa: E501
        :type: ConquestApiObjectType
        """

        self._attribute_type = attribute_type

    @property
    def condition_type(self):
        """Gets the condition_type of this ConquestApiAttributeSet.  # noqa: E501


        :return: The condition_type of this ConquestApiAttributeSet.  # noqa: E501
        :rtype: ConquestApiConditionType
        """
        return self._condition_type

    @condition_type.setter
    def condition_type(self, condition_type):
        """Sets the condition_type of this ConquestApiAttributeSet.


        :param condition_type: The condition_type of this ConquestApiAttributeSet.  # noqa: E501
        :type: ConquestApiConditionType
        """

        self._condition_type = condition_type

    @property
    def fields(self):
        """Gets the fields of this ConquestApiAttributeSet.  # noqa: E501


        :return: The fields of this ConquestApiAttributeSet.  # noqa: E501
        :rtype: list[ConquestApiAttributeSetField]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this ConquestApiAttributeSet.


        :param fields: The fields of this ConquestApiAttributeSet.  # noqa: E501
        :type: list[ConquestApiAttributeSetField]
        """

        self._fields = fields

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
        if issubclass(ConquestApiAttributeSet, dict):
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
        if not isinstance(other, ConquestApiAttributeSet):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiAttributeSet):
            return True

        return self.to_dict() != other.to_dict()
