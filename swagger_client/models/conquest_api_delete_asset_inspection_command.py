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

class ConquestApiDeleteAssetInspectionCommand(object):
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
        'asset_inspection_id': 'int'
    }

    attribute_map = {
        'asset_inspection_id': 'AssetInspectionID'
    }

    def __init__(self, asset_inspection_id=None):  # noqa: E501
        """ConquestApiDeleteAssetInspectionCommand - a model defined in Swagger"""  # noqa: E501
        self._asset_inspection_id = None
        self.discriminator = None
        if asset_inspection_id is not None:
            self.asset_inspection_id = asset_inspection_id

    @property
    def asset_inspection_id(self):
        """Gets the asset_inspection_id of this ConquestApiDeleteAssetInspectionCommand.  # noqa: E501


        :return: The asset_inspection_id of this ConquestApiDeleteAssetInspectionCommand.  # noqa: E501
        :rtype: int
        """
        return self._asset_inspection_id

    @asset_inspection_id.setter
    def asset_inspection_id(self, asset_inspection_id):
        """Sets the asset_inspection_id of this ConquestApiDeleteAssetInspectionCommand.


        :param asset_inspection_id: The asset_inspection_id of this ConquestApiDeleteAssetInspectionCommand.  # noqa: E501
        :type: int
        """

        self._asset_inspection_id = asset_inspection_id

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
        if issubclass(ConquestApiDeleteAssetInspectionCommand, dict):
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
        if not isinstance(other, ConquestApiDeleteAssetInspectionCommand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
