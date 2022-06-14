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


class ConquestApiCalculateDefectResponseDateResult(object):
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
        'parameters': 'ConquestApiCalculateDefectResponseDateParameters',
        'response_date': 'ConquestApiTimestampValue'
    }

    attribute_map = {
        'parameters': 'Parameters',
        'response_date': 'ResponseDate'
    }

    def __init__(self, parameters=None, response_date=None, _configuration=None):  # noqa: E501
        """ConquestApiCalculateDefectResponseDateResult - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._parameters = None
        self._response_date = None
        self.discriminator = None

        if parameters is not None:
            self.parameters = parameters
        if response_date is not None:
            self.response_date = response_date

    @property
    def parameters(self):
        """Gets the parameters of this ConquestApiCalculateDefectResponseDateResult.  # noqa: E501


        :return: The parameters of this ConquestApiCalculateDefectResponseDateResult.  # noqa: E501
        :rtype: ConquestApiCalculateDefectResponseDateParameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ConquestApiCalculateDefectResponseDateResult.


        :param parameters: The parameters of this ConquestApiCalculateDefectResponseDateResult.  # noqa: E501
        :type: ConquestApiCalculateDefectResponseDateParameters
        """

        self._parameters = parameters

    @property
    def response_date(self):
        """Gets the response_date of this ConquestApiCalculateDefectResponseDateResult.  # noqa: E501

        The Response Date calculated from the Current Inspection Date, Asset's Priority and Severity.  # noqa: E501

        :return: The response_date of this ConquestApiCalculateDefectResponseDateResult.  # noqa: E501
        :rtype: ConquestApiTimestampValue
        """
        return self._response_date

    @response_date.setter
    def response_date(self, response_date):
        """Sets the response_date of this ConquestApiCalculateDefectResponseDateResult.

        The Response Date calculated from the Current Inspection Date, Asset's Priority and Severity.  # noqa: E501

        :param response_date: The response_date of this ConquestApiCalculateDefectResponseDateResult.  # noqa: E501
        :type: ConquestApiTimestampValue
        """

        self._response_date = response_date

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
        if issubclass(ConquestApiCalculateDefectResponseDateResult, dict):
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
        if not isinstance(other, ConquestApiCalculateDefectResponseDateResult):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiCalculateDefectResponseDateResult):
            return True

        return self.to_dict() != other.to_dict()
