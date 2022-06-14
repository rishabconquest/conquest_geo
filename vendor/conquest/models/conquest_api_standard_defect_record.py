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


class ConquestApiStandardDefectRecord(object):
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
        'completed_icon_file': 'ConquestApiStyle',
        'default_severity_id': 'int',
        'icon_file': 'ConquestApiStyle',
        'layout': 'str',
        'ordr': 'int',
        'std_defect_description': 'str'
    }

    attribute_map = {
        'completed_icon_file': 'CompletedIconFile',
        'default_severity_id': 'DefaultSeverityID',
        'icon_file': 'IconFile',
        'layout': 'Layout',
        'ordr': 'Ordr',
        'std_defect_description': 'StdDefectDescription'
    }

    def __init__(self, completed_icon_file=None, default_severity_id=None, icon_file=None, layout=None, ordr=None, std_defect_description=None, _configuration=None):  # noqa: E501
        """ConquestApiStandardDefectRecord - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._completed_icon_file = None
        self._default_severity_id = None
        self._icon_file = None
        self._layout = None
        self._ordr = None
        self._std_defect_description = None
        self.discriminator = None

        if completed_icon_file is not None:
            self.completed_icon_file = completed_icon_file
        if default_severity_id is not None:
            self.default_severity_id = default_severity_id
        if icon_file is not None:
            self.icon_file = icon_file
        if layout is not None:
            self.layout = layout
        if ordr is not None:
            self.ordr = ordr
        if std_defect_description is not None:
            self.std_defect_description = std_defect_description

    @property
    def completed_icon_file(self):
        """Gets the completed_icon_file of this ConquestApiStandardDefectRecord.  # noqa: E501


        :return: The completed_icon_file of this ConquestApiStandardDefectRecord.  # noqa: E501
        :rtype: ConquestApiStyle
        """
        return self._completed_icon_file

    @completed_icon_file.setter
    def completed_icon_file(self, completed_icon_file):
        """Sets the completed_icon_file of this ConquestApiStandardDefectRecord.


        :param completed_icon_file: The completed_icon_file of this ConquestApiStandardDefectRecord.  # noqa: E501
        :type: ConquestApiStyle
        """

        self._completed_icon_file = completed_icon_file

    @property
    def default_severity_id(self):
        """Gets the default_severity_id of this ConquestApiStandardDefectRecord.  # noqa: E501


        :return: The default_severity_id of this ConquestApiStandardDefectRecord.  # noqa: E501
        :rtype: int
        """
        return self._default_severity_id

    @default_severity_id.setter
    def default_severity_id(self, default_severity_id):
        """Sets the default_severity_id of this ConquestApiStandardDefectRecord.


        :param default_severity_id: The default_severity_id of this ConquestApiStandardDefectRecord.  # noqa: E501
        :type: int
        """

        self._default_severity_id = default_severity_id

    @property
    def icon_file(self):
        """Gets the icon_file of this ConquestApiStandardDefectRecord.  # noqa: E501


        :return: The icon_file of this ConquestApiStandardDefectRecord.  # noqa: E501
        :rtype: ConquestApiStyle
        """
        return self._icon_file

    @icon_file.setter
    def icon_file(self, icon_file):
        """Sets the icon_file of this ConquestApiStandardDefectRecord.


        :param icon_file: The icon_file of this ConquestApiStandardDefectRecord.  # noqa: E501
        :type: ConquestApiStyle
        """

        self._icon_file = icon_file

    @property
    def layout(self):
        """Gets the layout of this ConquestApiStandardDefectRecord.  # noqa: E501


        :return: The layout of this ConquestApiStandardDefectRecord.  # noqa: E501
        :rtype: str
        """
        return self._layout

    @layout.setter
    def layout(self, layout):
        """Sets the layout of this ConquestApiStandardDefectRecord.


        :param layout: The layout of this ConquestApiStandardDefectRecord.  # noqa: E501
        :type: str
        """

        self._layout = layout

    @property
    def ordr(self):
        """Gets the ordr of this ConquestApiStandardDefectRecord.  # noqa: E501


        :return: The ordr of this ConquestApiStandardDefectRecord.  # noqa: E501
        :rtype: int
        """
        return self._ordr

    @ordr.setter
    def ordr(self, ordr):
        """Sets the ordr of this ConquestApiStandardDefectRecord.


        :param ordr: The ordr of this ConquestApiStandardDefectRecord.  # noqa: E501
        :type: int
        """

        self._ordr = ordr

    @property
    def std_defect_description(self):
        """Gets the std_defect_description of this ConquestApiStandardDefectRecord.  # noqa: E501


        :return: The std_defect_description of this ConquestApiStandardDefectRecord.  # noqa: E501
        :rtype: str
        """
        return self._std_defect_description

    @std_defect_description.setter
    def std_defect_description(self, std_defect_description):
        """Sets the std_defect_description of this ConquestApiStandardDefectRecord.


        :param std_defect_description: The std_defect_description of this ConquestApiStandardDefectRecord.  # noqa: E501
        :type: str
        """

        self._std_defect_description = std_defect_description

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
        if issubclass(ConquestApiStandardDefectRecord, dict):
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
        if not isinstance(other, ConquestApiStandardDefectRecord):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiStandardDefectRecord):
            return True

        return self.to_dict() != other.to_dict()
