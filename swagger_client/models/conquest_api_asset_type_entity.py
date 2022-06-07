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

class ConquestApiAssetTypeEntity(object):
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
        'attribute_id': 'int',
        'document_location': 'str',
        'field_descriptions': 'ConquestApiFieldDescriptions',
        'parent_id': 'int',
        'record': 'ConquestApiAssetTypeRecord',
        'type_id': 'int'
    }

    attribute_map = {
        'attribute_id': 'AttributeID',
        'document_location': 'DocumentLocation',
        'field_descriptions': 'FieldDescriptions',
        'parent_id': 'ParentID',
        'record': 'Record',
        'type_id': 'TypeID'
    }

    def __init__(self, attribute_id=None, document_location=None, field_descriptions=None, parent_id=None, record=None, type_id=None):  # noqa: E501
        """ConquestApiAssetTypeEntity - a model defined in Swagger"""  # noqa: E501
        self._attribute_id = None
        self._document_location = None
        self._field_descriptions = None
        self._parent_id = None
        self._record = None
        self._type_id = None
        self.discriminator = None
        if attribute_id is not None:
            self.attribute_id = attribute_id
        if document_location is not None:
            self.document_location = document_location
        if field_descriptions is not None:
            self.field_descriptions = field_descriptions
        if parent_id is not None:
            self.parent_id = parent_id
        if record is not None:
            self.record = record
        if type_id is not None:
            self.type_id = type_id

    @property
    def attribute_id(self):
        """Gets the attribute_id of this ConquestApiAssetTypeEntity.  # noqa: E501


        :return: The attribute_id of this ConquestApiAssetTypeEntity.  # noqa: E501
        :rtype: int
        """
        return self._attribute_id

    @attribute_id.setter
    def attribute_id(self, attribute_id):
        """Sets the attribute_id of this ConquestApiAssetTypeEntity.


        :param attribute_id: The attribute_id of this ConquestApiAssetTypeEntity.  # noqa: E501
        :type: int
        """

        self._attribute_id = attribute_id

    @property
    def document_location(self):
        """Gets the document_location of this ConquestApiAssetTypeEntity.  # noqa: E501


        :return: The document_location of this ConquestApiAssetTypeEntity.  # noqa: E501
        :rtype: str
        """
        return self._document_location

    @document_location.setter
    def document_location(self, document_location):
        """Sets the document_location of this ConquestApiAssetTypeEntity.


        :param document_location: The document_location of this ConquestApiAssetTypeEntity.  # noqa: E501
        :type: str
        """

        self._document_location = document_location

    @property
    def field_descriptions(self):
        """Gets the field_descriptions of this ConquestApiAssetTypeEntity.  # noqa: E501


        :return: The field_descriptions of this ConquestApiAssetTypeEntity.  # noqa: E501
        :rtype: ConquestApiFieldDescriptions
        """
        return self._field_descriptions

    @field_descriptions.setter
    def field_descriptions(self, field_descriptions):
        """Sets the field_descriptions of this ConquestApiAssetTypeEntity.


        :param field_descriptions: The field_descriptions of this ConquestApiAssetTypeEntity.  # noqa: E501
        :type: ConquestApiFieldDescriptions
        """

        self._field_descriptions = field_descriptions

    @property
    def parent_id(self):
        """Gets the parent_id of this ConquestApiAssetTypeEntity.  # noqa: E501


        :return: The parent_id of this ConquestApiAssetTypeEntity.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this ConquestApiAssetTypeEntity.


        :param parent_id: The parent_id of this ConquestApiAssetTypeEntity.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def record(self):
        """Gets the record of this ConquestApiAssetTypeEntity.  # noqa: E501


        :return: The record of this ConquestApiAssetTypeEntity.  # noqa: E501
        :rtype: ConquestApiAssetTypeRecord
        """
        return self._record

    @record.setter
    def record(self, record):
        """Sets the record of this ConquestApiAssetTypeEntity.


        :param record: The record of this ConquestApiAssetTypeEntity.  # noqa: E501
        :type: ConquestApiAssetTypeRecord
        """

        self._record = record

    @property
    def type_id(self):
        """Gets the type_id of this ConquestApiAssetTypeEntity.  # noqa: E501


        :return: The type_id of this ConquestApiAssetTypeEntity.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this ConquestApiAssetTypeEntity.


        :param type_id: The type_id of this ConquestApiAssetTypeEntity.  # noqa: E501
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
        if issubclass(ConquestApiAssetTypeEntity, dict):
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
        if not isinstance(other, ConquestApiAssetTypeEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other