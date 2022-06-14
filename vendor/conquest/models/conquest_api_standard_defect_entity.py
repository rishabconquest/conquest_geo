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


class ConquestApiStandardDefectEntity(object):
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
        'record': 'ConquestApiStandardDefectRecord',
        'std_defect_id': 'int',
        'type_id': 'int'
    }

    attribute_map = {
        'attribute_id': 'AttributeID',
        'record': 'Record',
        'std_defect_id': 'StdDefectID',
        'type_id': 'TypeID'
    }

    def __init__(self, attribute_id=None, record=None, std_defect_id=None, type_id=None, _configuration=None):  # noqa: E501
        """ConquestApiStandardDefectEntity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._attribute_id = None
        self._record = None
        self._std_defect_id = None
        self._type_id = None
        self.discriminator = None

        if attribute_id is not None:
            self.attribute_id = attribute_id
        if record is not None:
            self.record = record
        if std_defect_id is not None:
            self.std_defect_id = std_defect_id
        if type_id is not None:
            self.type_id = type_id

    @property
    def attribute_id(self):
        """Gets the attribute_id of this ConquestApiStandardDefectEntity.  # noqa: E501


        :return: The attribute_id of this ConquestApiStandardDefectEntity.  # noqa: E501
        :rtype: int
        """
        return self._attribute_id

    @attribute_id.setter
    def attribute_id(self, attribute_id):
        """Sets the attribute_id of this ConquestApiStandardDefectEntity.


        :param attribute_id: The attribute_id of this ConquestApiStandardDefectEntity.  # noqa: E501
        :type: int
        """

        self._attribute_id = attribute_id

    @property
    def record(self):
        """Gets the record of this ConquestApiStandardDefectEntity.  # noqa: E501


        :return: The record of this ConquestApiStandardDefectEntity.  # noqa: E501
        :rtype: ConquestApiStandardDefectRecord
        """
        return self._record

    @record.setter
    def record(self, record):
        """Sets the record of this ConquestApiStandardDefectEntity.


        :param record: The record of this ConquestApiStandardDefectEntity.  # noqa: E501
        :type: ConquestApiStandardDefectRecord
        """

        self._record = record

    @property
    def std_defect_id(self):
        """Gets the std_defect_id of this ConquestApiStandardDefectEntity.  # noqa: E501


        :return: The std_defect_id of this ConquestApiStandardDefectEntity.  # noqa: E501
        :rtype: int
        """
        return self._std_defect_id

    @std_defect_id.setter
    def std_defect_id(self, std_defect_id):
        """Sets the std_defect_id of this ConquestApiStandardDefectEntity.


        :param std_defect_id: The std_defect_id of this ConquestApiStandardDefectEntity.  # noqa: E501
        :type: int
        """

        self._std_defect_id = std_defect_id

    @property
    def type_id(self):
        """Gets the type_id of this ConquestApiStandardDefectEntity.  # noqa: E501


        :return: The type_id of this ConquestApiStandardDefectEntity.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this ConquestApiStandardDefectEntity.


        :param type_id: The type_id of this ConquestApiStandardDefectEntity.  # noqa: E501
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
        if issubclass(ConquestApiStandardDefectEntity, dict):
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
        if not isinstance(other, ConquestApiStandardDefectEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiStandardDefectEntity):
            return True

        return self.to_dict() != other.to_dict()
