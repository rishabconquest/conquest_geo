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

class ConquestApiJobProgressInfo(object):
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
        'last_updated': 'datetime',
        'status': 'ConquestApiJobStatus',
        'status_description': 'str',
        'title': 'str',
        'total_work': 'float',
        'work_done': 'float'
    }

    attribute_map = {
        'last_updated': 'last_updated',
        'status': 'status',
        'status_description': 'status_description',
        'title': 'title',
        'total_work': 'total_work',
        'work_done': 'work_done'
    }

    def __init__(self, last_updated=None, status=None, status_description=None, title=None, total_work=None, work_done=None):  # noqa: E501
        """ConquestApiJobProgressInfo - a model defined in Swagger"""  # noqa: E501
        self._last_updated = None
        self._status = None
        self._status_description = None
        self._title = None
        self._total_work = None
        self._work_done = None
        self.discriminator = None
        if last_updated is not None:
            self.last_updated = last_updated
        if status is not None:
            self.status = status
        if status_description is not None:
            self.status_description = status_description
        if title is not None:
            self.title = title
        if total_work is not None:
            self.total_work = total_work
        if work_done is not None:
            self.work_done = work_done

    @property
    def last_updated(self):
        """Gets the last_updated of this ConquestApiJobProgressInfo.  # noqa: E501


        :return: The last_updated of this ConquestApiJobProgressInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this ConquestApiJobProgressInfo.


        :param last_updated: The last_updated of this ConquestApiJobProgressInfo.  # noqa: E501
        :type: datetime
        """

        self._last_updated = last_updated

    @property
    def status(self):
        """Gets the status of this ConquestApiJobProgressInfo.  # noqa: E501


        :return: The status of this ConquestApiJobProgressInfo.  # noqa: E501
        :rtype: ConquestApiJobStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ConquestApiJobProgressInfo.


        :param status: The status of this ConquestApiJobProgressInfo.  # noqa: E501
        :type: ConquestApiJobStatus
        """

        self._status = status

    @property
    def status_description(self):
        """Gets the status_description of this ConquestApiJobProgressInfo.  # noqa: E501


        :return: The status_description of this ConquestApiJobProgressInfo.  # noqa: E501
        :rtype: str
        """
        return self._status_description

    @status_description.setter
    def status_description(self, status_description):
        """Sets the status_description of this ConquestApiJobProgressInfo.


        :param status_description: The status_description of this ConquestApiJobProgressInfo.  # noqa: E501
        :type: str
        """

        self._status_description = status_description

    @property
    def title(self):
        """Gets the title of this ConquestApiJobProgressInfo.  # noqa: E501


        :return: The title of this ConquestApiJobProgressInfo.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ConquestApiJobProgressInfo.


        :param title: The title of this ConquestApiJobProgressInfo.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def total_work(self):
        """Gets the total_work of this ConquestApiJobProgressInfo.  # noqa: E501

        Total Units of work. Default is 1.  # noqa: E501

        :return: The total_work of this ConquestApiJobProgressInfo.  # noqa: E501
        :rtype: float
        """
        return self._total_work

    @total_work.setter
    def total_work(self, total_work):
        """Sets the total_work of this ConquestApiJobProgressInfo.

        Total Units of work. Default is 1.  # noqa: E501

        :param total_work: The total_work of this ConquestApiJobProgressInfo.  # noqa: E501
        :type: float
        """

        self._total_work = total_work

    @property
    def work_done(self):
        """Gets the work_done of this ConquestApiJobProgressInfo.  # noqa: E501

        Units of work currently completed, progress of process is calculated using = WorkDone / TotalWork. Default is 0.  # noqa: E501

        :return: The work_done of this ConquestApiJobProgressInfo.  # noqa: E501
        :rtype: float
        """
        return self._work_done

    @work_done.setter
    def work_done(self, work_done):
        """Sets the work_done of this ConquestApiJobProgressInfo.

        Units of work currently completed, progress of process is calculated using = WorkDone / TotalWork. Default is 0.  # noqa: E501

        :param work_done: The work_done of this ConquestApiJobProgressInfo.  # noqa: E501
        :type: float
        """

        self._work_done = work_done

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
        if issubclass(ConquestApiJobProgressInfo, dict):
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
        if not isinstance(other, ConquestApiJobProgressInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other