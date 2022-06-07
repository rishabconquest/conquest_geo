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

class ConquestApiDocumentMigrationWorkLoad(object):
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
        'device_name': 'str',
        'notes': 'str',
        'overall_progress_message': 'str',
        'overall_progress_value': 'float',
        'progress_details': 'list[ConquestApiDocumentTypeMigrationProgress]',
        'user_name': 'str',
        'work_load_id': 'str',
        'work_started': 'datetime'
    }

    attribute_map = {
        'device_name': 'DeviceName',
        'notes': 'Notes',
        'overall_progress_message': 'OverallProgressMessage',
        'overall_progress_value': 'OverallProgressValue',
        'progress_details': 'ProgressDetails',
        'user_name': 'UserName',
        'work_load_id': 'WorkLoadID',
        'work_started': 'WorkStarted'
    }

    def __init__(self, device_name=None, notes=None, overall_progress_message=None, overall_progress_value=None, progress_details=None, user_name=None, work_load_id=None, work_started=None):  # noqa: E501
        """ConquestApiDocumentMigrationWorkLoad - a model defined in Swagger"""  # noqa: E501
        self._device_name = None
        self._notes = None
        self._overall_progress_message = None
        self._overall_progress_value = None
        self._progress_details = None
        self._user_name = None
        self._work_load_id = None
        self._work_started = None
        self.discriminator = None
        if device_name is not None:
            self.device_name = device_name
        if notes is not None:
            self.notes = notes
        if overall_progress_message is not None:
            self.overall_progress_message = overall_progress_message
        if overall_progress_value is not None:
            self.overall_progress_value = overall_progress_value
        if progress_details is not None:
            self.progress_details = progress_details
        if user_name is not None:
            self.user_name = user_name
        if work_load_id is not None:
            self.work_load_id = work_load_id
        if work_started is not None:
            self.work_started = work_started

    @property
    def device_name(self):
        """Gets the device_name of this ConquestApiDocumentMigrationWorkLoad.  # noqa: E501


        :return: The device_name of this ConquestApiDocumentMigrationWorkLoad.  # noqa: E501
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this ConquestApiDocumentMigrationWorkLoad.


        :param device_name: The device_name of this ConquestApiDocumentMigrationWorkLoad.  # noqa: E501
        :type: str
        """

        self._device_name = device_name

    @property
    def notes(self):
        """Gets the notes of this ConquestApiDocumentMigrationWorkLoad.  # noqa: E501


        :return: The notes of this ConquestApiDocumentMigrationWorkLoad.  # noqa: E501
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this ConquestApiDocumentMigrationWorkLoad.


        :param notes: The notes of this ConquestApiDocumentMigrationWorkLoad.  # noqa: E501
        :type: str
        """

        self._notes = notes

    @property
    def overall_progress_message(self):
        """Gets the overall_progress_message of this ConquestApiDocumentMigrationWorkLoad.  # noqa: E501


        :return: The overall_progress_message of this ConquestApiDocumentMigrationWorkLoad.  # noqa: E501
        :rtype: str
        """
        return self._overall_progress_message

    @overall_progress_message.setter
    def overall_progress_message(self, overall_progress_message):
        """Sets the overall_progress_message of this ConquestApiDocumentMigrationWorkLoad.


        :param overall_progress_message: The overall_progress_message of this ConquestApiDocumentMigrationWorkLoad.  # noqa: E501
        :type: str
        """

        self._overall_progress_message = overall_progress_message

    @property
    def overall_progress_value(self):
        """Gets the overall_progress_value of this ConquestApiDocumentMigrationWorkLoad.  # noqa: E501


        :return: The overall_progress_value of this ConquestApiDocumentMigrationWorkLoad.  # noqa: E501
        :rtype: float
        """
        return self._overall_progress_value

    @overall_progress_value.setter
    def overall_progress_value(self, overall_progress_value):
        """Sets the overall_progress_value of this ConquestApiDocumentMigrationWorkLoad.


        :param overall_progress_value: The overall_progress_value of this ConquestApiDocumentMigrationWorkLoad.  # noqa: E501
        :type: float
        """

        self._overall_progress_value = overall_progress_value

    @property
    def progress_details(self):
        """Gets the progress_details of this ConquestApiDocumentMigrationWorkLoad.  # noqa: E501


        :return: The progress_details of this ConquestApiDocumentMigrationWorkLoad.  # noqa: E501
        :rtype: list[ConquestApiDocumentTypeMigrationProgress]
        """
        return self._progress_details

    @progress_details.setter
    def progress_details(self, progress_details):
        """Sets the progress_details of this ConquestApiDocumentMigrationWorkLoad.


        :param progress_details: The progress_details of this ConquestApiDocumentMigrationWorkLoad.  # noqa: E501
        :type: list[ConquestApiDocumentTypeMigrationProgress]
        """

        self._progress_details = progress_details

    @property
    def user_name(self):
        """Gets the user_name of this ConquestApiDocumentMigrationWorkLoad.  # noqa: E501


        :return: The user_name of this ConquestApiDocumentMigrationWorkLoad.  # noqa: E501
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ConquestApiDocumentMigrationWorkLoad.


        :param user_name: The user_name of this ConquestApiDocumentMigrationWorkLoad.  # noqa: E501
        :type: str
        """

        self._user_name = user_name

    @property
    def work_load_id(self):
        """Gets the work_load_id of this ConquestApiDocumentMigrationWorkLoad.  # noqa: E501


        :return: The work_load_id of this ConquestApiDocumentMigrationWorkLoad.  # noqa: E501
        :rtype: str
        """
        return self._work_load_id

    @work_load_id.setter
    def work_load_id(self, work_load_id):
        """Sets the work_load_id of this ConquestApiDocumentMigrationWorkLoad.


        :param work_load_id: The work_load_id of this ConquestApiDocumentMigrationWorkLoad.  # noqa: E501
        :type: str
        """

        self._work_load_id = work_load_id

    @property
    def work_started(self):
        """Gets the work_started of this ConquestApiDocumentMigrationWorkLoad.  # noqa: E501


        :return: The work_started of this ConquestApiDocumentMigrationWorkLoad.  # noqa: E501
        :rtype: datetime
        """
        return self._work_started

    @work_started.setter
    def work_started(self, work_started):
        """Sets the work_started of this ConquestApiDocumentMigrationWorkLoad.


        :param work_started: The work_started of this ConquestApiDocumentMigrationWorkLoad.  # noqa: E501
        :type: datetime
        """

        self._work_started = work_started

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
        if issubclass(ConquestApiDocumentMigrationWorkLoad, dict):
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
        if not isinstance(other, ConquestApiDocumentMigrationWorkLoad):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
