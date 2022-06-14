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


class ConquestApiRecordColumn(object):
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
        'alias': 'str',
        'caption': 'str',
        'group': 'int',
        'identity': 'bool',
        'index': 'int',
        'relation': 'ConquestApiRelation',
        'value_type': 'ConquestApiValueType'
    }

    attribute_map = {
        'alias': 'alias',
        'caption': 'caption',
        'group': 'group',
        'identity': 'identity',
        'index': 'index',
        'relation': 'relation',
        'value_type': 'valueType'
    }

    def __init__(self, alias=None, caption=None, group=None, identity=None, index=None, relation=None, value_type=None, _configuration=None):  # noqa: E501
        """ConquestApiRecordColumn - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._alias = None
        self._caption = None
        self._group = None
        self._identity = None
        self._index = None
        self._relation = None
        self._value_type = None
        self.discriminator = None

        if alias is not None:
            self.alias = alias
        if caption is not None:
            self.caption = caption
        if group is not None:
            self.group = group
        if identity is not None:
            self.identity = identity
        if index is not None:
            self.index = index
        if relation is not None:
            self.relation = relation
        if value_type is not None:
            self.value_type = value_type

    @property
    def alias(self):
        """Gets the alias of this ConquestApiRecordColumn.  # noqa: E501

        alias is the column name or SQL alias in a query or user view.  - An alias with a prefix of 2 underscores '__' are reserved for Conquest. These fields are subject to change, they're a temporary solution   For example, __Title, __Subtitle  WARNING alias is not finalized, don't write code that depends on it.  view.column for non-calculated values defined in a Context (a selection of fields in the Field Dictionary)  # noqa: E501

        :return: The alias of this ConquestApiRecordColumn.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this ConquestApiRecordColumn.

        alias is the column name or SQL alias in a query or user view.  - An alias with a prefix of 2 underscores '__' are reserved for Conquest. These fields are subject to change, they're a temporary solution   For example, __Title, __Subtitle  WARNING alias is not finalized, don't write code that depends on it.  view.column for non-calculated values defined in a Context (a selection of fields in the Field Dictionary)  # noqa: E501

        :param alias: The alias of this ConquestApiRecordColumn.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def caption(self):
        """Gets the caption of this ConquestApiRecordColumn.  # noqa: E501


        :return: The caption of this ConquestApiRecordColumn.  # noqa: E501
        :rtype: str
        """
        return self._caption

    @caption.setter
    def caption(self, caption):
        """Sets the caption of this ConquestApiRecordColumn.


        :param caption: The caption of this ConquestApiRecordColumn.  # noqa: E501
        :type: str
        """

        self._caption = caption

    @property
    def group(self):
        """Gets the group of this ConquestApiRecordColumn.  # noqa: E501


        :return: The group of this ConquestApiRecordColumn.  # noqa: E501
        :rtype: int
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ConquestApiRecordColumn.


        :param group: The group of this ConquestApiRecordColumn.  # noqa: E501
        :type: int
        """

        self._group = group

    @property
    def identity(self):
        """Gets the identity of this ConquestApiRecordColumn.  # noqa: E501


        :return: The identity of this ConquestApiRecordColumn.  # noqa: E501
        :rtype: bool
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this ConquestApiRecordColumn.


        :param identity: The identity of this ConquestApiRecordColumn.  # noqa: E501
        :type: bool
        """

        self._identity = identity

    @property
    def index(self):
        """Gets the index of this ConquestApiRecordColumn.  # noqa: E501


        :return: The index of this ConquestApiRecordColumn.  # noqa: E501
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this ConquestApiRecordColumn.


        :param index: The index of this ConquestApiRecordColumn.  # noqa: E501
        :type: int
        """

        self._index = index

    @property
    def relation(self):
        """Gets the relation of this ConquestApiRecordColumn.  # noqa: E501


        :return: The relation of this ConquestApiRecordColumn.  # noqa: E501
        :rtype: ConquestApiRelation
        """
        return self._relation

    @relation.setter
    def relation(self, relation):
        """Sets the relation of this ConquestApiRecordColumn.


        :param relation: The relation of this ConquestApiRecordColumn.  # noqa: E501
        :type: ConquestApiRelation
        """

        self._relation = relation

    @property
    def value_type(self):
        """Gets the value_type of this ConquestApiRecordColumn.  # noqa: E501


        :return: The value_type of this ConquestApiRecordColumn.  # noqa: E501
        :rtype: ConquestApiValueType
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this ConquestApiRecordColumn.


        :param value_type: The value_type of this ConquestApiRecordColumn.  # noqa: E501
        :type: ConquestApiValueType
        """

        self._value_type = value_type

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
        if issubclass(ConquestApiRecordColumn, dict):
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
        if not isinstance(other, ConquestApiRecordColumn):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiRecordColumn):
            return True

        return self.to_dict() != other.to_dict()
