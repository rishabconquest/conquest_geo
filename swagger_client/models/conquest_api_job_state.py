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

class ConquestApiJobState(object):
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
        'creation_details': 'ConquestApiJobCreationDetails',
        'job_key': 'ConquestApiJobKey',
        'progress': 'ConquestApiJobProgressInfo',
        'result': 'ConquestApiJobResult'
    }

    attribute_map = {
        'creation_details': 'creation_details',
        'job_key': 'job_key',
        'progress': 'progress',
        'result': 'result'
    }

    def __init__(self, creation_details=None, job_key=None, progress=None, result=None):  # noqa: E501
        """ConquestApiJobState - a model defined in Swagger"""  # noqa: E501
        self._creation_details = None
        self._job_key = None
        self._progress = None
        self._result = None
        self.discriminator = None
        if creation_details is not None:
            self.creation_details = creation_details
        if job_key is not None:
            self.job_key = job_key
        if progress is not None:
            self.progress = progress
        if result is not None:
            self.result = result

    @property
    def creation_details(self):
        """Gets the creation_details of this ConquestApiJobState.  # noqa: E501


        :return: The creation_details of this ConquestApiJobState.  # noqa: E501
        :rtype: ConquestApiJobCreationDetails
        """
        return self._creation_details

    @creation_details.setter
    def creation_details(self, creation_details):
        """Sets the creation_details of this ConquestApiJobState.


        :param creation_details: The creation_details of this ConquestApiJobState.  # noqa: E501
        :type: ConquestApiJobCreationDetails
        """

        self._creation_details = creation_details

    @property
    def job_key(self):
        """Gets the job_key of this ConquestApiJobState.  # noqa: E501


        :return: The job_key of this ConquestApiJobState.  # noqa: E501
        :rtype: ConquestApiJobKey
        """
        return self._job_key

    @job_key.setter
    def job_key(self, job_key):
        """Sets the job_key of this ConquestApiJobState.


        :param job_key: The job_key of this ConquestApiJobState.  # noqa: E501
        :type: ConquestApiJobKey
        """

        self._job_key = job_key

    @property
    def progress(self):
        """Gets the progress of this ConquestApiJobState.  # noqa: E501


        :return: The progress of this ConquestApiJobState.  # noqa: E501
        :rtype: ConquestApiJobProgressInfo
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this ConquestApiJobState.


        :param progress: The progress of this ConquestApiJobState.  # noqa: E501
        :type: ConquestApiJobProgressInfo
        """

        self._progress = progress

    @property
    def result(self):
        """Gets the result of this ConquestApiJobState.  # noqa: E501


        :return: The result of this ConquestApiJobState.  # noqa: E501
        :rtype: ConquestApiJobResult
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ConquestApiJobState.


        :param result: The result of this ConquestApiJobState.  # noqa: E501
        :type: ConquestApiJobResult
        """

        self._result = result

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
        if issubclass(ConquestApiJobState, dict):
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
        if not isinstance(other, ConquestApiJobState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
