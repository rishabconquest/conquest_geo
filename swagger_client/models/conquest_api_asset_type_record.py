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

class ConquestApiAssetTypeRecord(object):
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
        'hyperlinks': 'ConquestApiCustomHyperlinkList',
        'map_style': 'ConquestApiStyle',
        'type_description': 'str',
        'type_notes': 'str',
        'type_user_text1': 'str',
        'type_user_text2': 'str',
        'val_item': 'bool'
    }

    attribute_map = {
        'hyperlinks': 'Hyperlinks',
        'map_style': 'MapStyle',
        'type_description': 'TypeDescription',
        'type_notes': 'TypeNotes',
        'type_user_text1': 'TypeUserText1',
        'type_user_text2': 'TypeUserText2',
        'val_item': 'ValItem'
    }

    def __init__(self, hyperlinks=None, map_style=None, type_description=None, type_notes=None, type_user_text1=None, type_user_text2=None, val_item=None):  # noqa: E501
        """ConquestApiAssetTypeRecord - a model defined in Swagger"""  # noqa: E501
        self._hyperlinks = None
        self._map_style = None
        self._type_description = None
        self._type_notes = None
        self._type_user_text1 = None
        self._type_user_text2 = None
        self._val_item = None
        self.discriminator = None
        if hyperlinks is not None:
            self.hyperlinks = hyperlinks
        if map_style is not None:
            self.map_style = map_style
        if type_description is not None:
            self.type_description = type_description
        if type_notes is not None:
            self.type_notes = type_notes
        if type_user_text1 is not None:
            self.type_user_text1 = type_user_text1
        if type_user_text2 is not None:
            self.type_user_text2 = type_user_text2
        if val_item is not None:
            self.val_item = val_item

    @property
    def hyperlinks(self):
        """Gets the hyperlinks of this ConquestApiAssetTypeRecord.  # noqa: E501


        :return: The hyperlinks of this ConquestApiAssetTypeRecord.  # noqa: E501
        :rtype: ConquestApiCustomHyperlinkList
        """
        return self._hyperlinks

    @hyperlinks.setter
    def hyperlinks(self, hyperlinks):
        """Sets the hyperlinks of this ConquestApiAssetTypeRecord.


        :param hyperlinks: The hyperlinks of this ConquestApiAssetTypeRecord.  # noqa: E501
        :type: ConquestApiCustomHyperlinkList
        """

        self._hyperlinks = hyperlinks

    @property
    def map_style(self):
        """Gets the map_style of this ConquestApiAssetTypeRecord.  # noqa: E501


        :return: The map_style of this ConquestApiAssetTypeRecord.  # noqa: E501
        :rtype: ConquestApiStyle
        """
        return self._map_style

    @map_style.setter
    def map_style(self, map_style):
        """Sets the map_style of this ConquestApiAssetTypeRecord.


        :param map_style: The map_style of this ConquestApiAssetTypeRecord.  # noqa: E501
        :type: ConquestApiStyle
        """

        self._map_style = map_style

    @property
    def type_description(self):
        """Gets the type_description of this ConquestApiAssetTypeRecord.  # noqa: E501


        :return: The type_description of this ConquestApiAssetTypeRecord.  # noqa: E501
        :rtype: str
        """
        return self._type_description

    @type_description.setter
    def type_description(self, type_description):
        """Sets the type_description of this ConquestApiAssetTypeRecord.


        :param type_description: The type_description of this ConquestApiAssetTypeRecord.  # noqa: E501
        :type: str
        """

        self._type_description = type_description

    @property
    def type_notes(self):
        """Gets the type_notes of this ConquestApiAssetTypeRecord.  # noqa: E501


        :return: The type_notes of this ConquestApiAssetTypeRecord.  # noqa: E501
        :rtype: str
        """
        return self._type_notes

    @type_notes.setter
    def type_notes(self, type_notes):
        """Sets the type_notes of this ConquestApiAssetTypeRecord.


        :param type_notes: The type_notes of this ConquestApiAssetTypeRecord.  # noqa: E501
        :type: str
        """

        self._type_notes = type_notes

    @property
    def type_user_text1(self):
        """Gets the type_user_text1 of this ConquestApiAssetTypeRecord.  # noqa: E501


        :return: The type_user_text1 of this ConquestApiAssetTypeRecord.  # noqa: E501
        :rtype: str
        """
        return self._type_user_text1

    @type_user_text1.setter
    def type_user_text1(self, type_user_text1):
        """Sets the type_user_text1 of this ConquestApiAssetTypeRecord.


        :param type_user_text1: The type_user_text1 of this ConquestApiAssetTypeRecord.  # noqa: E501
        :type: str
        """

        self._type_user_text1 = type_user_text1

    @property
    def type_user_text2(self):
        """Gets the type_user_text2 of this ConquestApiAssetTypeRecord.  # noqa: E501


        :return: The type_user_text2 of this ConquestApiAssetTypeRecord.  # noqa: E501
        :rtype: str
        """
        return self._type_user_text2

    @type_user_text2.setter
    def type_user_text2(self, type_user_text2):
        """Sets the type_user_text2 of this ConquestApiAssetTypeRecord.


        :param type_user_text2: The type_user_text2 of this ConquestApiAssetTypeRecord.  # noqa: E501
        :type: str
        """

        self._type_user_text2 = type_user_text2

    @property
    def val_item(self):
        """Gets the val_item of this ConquestApiAssetTypeRecord.  # noqa: E501


        :return: The val_item of this ConquestApiAssetTypeRecord.  # noqa: E501
        :rtype: bool
        """
        return self._val_item

    @val_item.setter
    def val_item(self, val_item):
        """Sets the val_item of this ConquestApiAssetTypeRecord.


        :param val_item: The val_item of this ConquestApiAssetTypeRecord.  # noqa: E501
        :type: bool
        """

        self._val_item = val_item

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
        if issubclass(ConquestApiAssetTypeRecord, dict):
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
        if not isinstance(other, ConquestApiAssetTypeRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
