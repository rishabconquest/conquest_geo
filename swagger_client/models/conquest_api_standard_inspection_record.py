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

class ConquestApiStandardInspectionRecord(object):
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
        'std_inspection_description': 'str'
    }

    attribute_map = {
        'std_inspection_description': 'StdInspectionDescription'
    }

    def __init__(self, std_inspection_description=None):  # noqa: E501
        """ConquestApiStandardInspectionRecord - a model defined in Swagger"""  # noqa: E501
        self._std_inspection_description = None
        self.discriminator = None
        if std_inspection_description is not None:
            self.std_inspection_description = std_inspection_description

    @property
    def std_inspection_description(self):
        """Gets the std_inspection_description of this ConquestApiStandardInspectionRecord.  # noqa: E501


        :return: The std_inspection_description of this ConquestApiStandardInspectionRecord.  # noqa: E501
        :rtype: str
        """
        return self._std_inspection_description

    @std_inspection_description.setter
    def std_inspection_description(self, std_inspection_description):
        """Sets the std_inspection_description of this ConquestApiStandardInspectionRecord.


        :param std_inspection_description: The std_inspection_description of this ConquestApiStandardInspectionRecord.  # noqa: E501
        :type: str
        """

        self._std_inspection_description = std_inspection_description

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
        if issubclass(ConquestApiStandardInspectionRecord, dict):
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
        if not isinstance(other, ConquestApiStandardInspectionRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other