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


class ConquestApiRequestEntity(object):
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
        'arq_id': 'int',
        'completed': 'bool',
        'completed_by': 'str',
        'edit_date': 'datetime',
        'editor': 'str',
        'map_style': 'ConquestApiStyle',
        'record': 'ConquestApiRequestRecord',
        'reference_id': 'str',
        'lock': 'ConquestApiLock'
    }

    attribute_map = {
        'arq_id': 'ArqID',
        'completed': 'Completed',
        'completed_by': 'CompletedBy',
        'edit_date': 'EditDate',
        'editor': 'Editor',
        'map_style': 'MapStyle',
        'record': 'Record',
        'reference_id': 'ReferenceID',
        'lock': 'lock'
    }

    def __init__(self, arq_id=None, completed=None, completed_by=None, edit_date=None, editor=None, map_style=None, record=None, reference_id=None, lock=None, _configuration=None):  # noqa: E501
        """ConquestApiRequestEntity - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._arq_id = None
        self._completed = None
        self._completed_by = None
        self._edit_date = None
        self._editor = None
        self._map_style = None
        self._record = None
        self._reference_id = None
        self._lock = None
        self.discriminator = None

        if arq_id is not None:
            self.arq_id = arq_id
        if completed is not None:
            self.completed = completed
        if completed_by is not None:
            self.completed_by = completed_by
        if edit_date is not None:
            self.edit_date = edit_date
        if editor is not None:
            self.editor = editor
        if map_style is not None:
            self.map_style = map_style
        if record is not None:
            self.record = record
        if reference_id is not None:
            self.reference_id = reference_id
        if lock is not None:
            self.lock = lock

    @property
    def arq_id(self):
        """Gets the arq_id of this ConquestApiRequestEntity.  # noqa: E501


        :return: The arq_id of this ConquestApiRequestEntity.  # noqa: E501
        :rtype: int
        """
        return self._arq_id

    @arq_id.setter
    def arq_id(self, arq_id):
        """Sets the arq_id of this ConquestApiRequestEntity.


        :param arq_id: The arq_id of this ConquestApiRequestEntity.  # noqa: E501
        :type: int
        """

        self._arq_id = arq_id

    @property
    def completed(self):
        """Gets the completed of this ConquestApiRequestEntity.  # noqa: E501


        :return: The completed of this ConquestApiRequestEntity.  # noqa: E501
        :rtype: bool
        """
        return self._completed

    @completed.setter
    def completed(self, completed):
        """Sets the completed of this ConquestApiRequestEntity.


        :param completed: The completed of this ConquestApiRequestEntity.  # noqa: E501
        :type: bool
        """

        self._completed = completed

    @property
    def completed_by(self):
        """Gets the completed_by of this ConquestApiRequestEntity.  # noqa: E501


        :return: The completed_by of this ConquestApiRequestEntity.  # noqa: E501
        :rtype: str
        """
        return self._completed_by

    @completed_by.setter
    def completed_by(self, completed_by):
        """Sets the completed_by of this ConquestApiRequestEntity.


        :param completed_by: The completed_by of this ConquestApiRequestEntity.  # noqa: E501
        :type: str
        """

        self._completed_by = completed_by

    @property
    def edit_date(self):
        """Gets the edit_date of this ConquestApiRequestEntity.  # noqa: E501


        :return: The edit_date of this ConquestApiRequestEntity.  # noqa: E501
        :rtype: datetime
        """
        return self._edit_date

    @edit_date.setter
    def edit_date(self, edit_date):
        """Sets the edit_date of this ConquestApiRequestEntity.


        :param edit_date: The edit_date of this ConquestApiRequestEntity.  # noqa: E501
        :type: datetime
        """

        self._edit_date = edit_date

    @property
    def editor(self):
        """Gets the editor of this ConquestApiRequestEntity.  # noqa: E501


        :return: The editor of this ConquestApiRequestEntity.  # noqa: E501
        :rtype: str
        """
        return self._editor

    @editor.setter
    def editor(self, editor):
        """Sets the editor of this ConquestApiRequestEntity.


        :param editor: The editor of this ConquestApiRequestEntity.  # noqa: E501
        :type: str
        """

        self._editor = editor

    @property
    def map_style(self):
        """Gets the map_style of this ConquestApiRequestEntity.  # noqa: E501


        :return: The map_style of this ConquestApiRequestEntity.  # noqa: E501
        :rtype: ConquestApiStyle
        """
        return self._map_style

    @map_style.setter
    def map_style(self, map_style):
        """Sets the map_style of this ConquestApiRequestEntity.


        :param map_style: The map_style of this ConquestApiRequestEntity.  # noqa: E501
        :type: ConquestApiStyle
        """

        self._map_style = map_style

    @property
    def record(self):
        """Gets the record of this ConquestApiRequestEntity.  # noqa: E501


        :return: The record of this ConquestApiRequestEntity.  # noqa: E501
        :rtype: ConquestApiRequestRecord
        """
        return self._record

    @record.setter
    def record(self, record):
        """Sets the record of this ConquestApiRequestEntity.


        :param record: The record of this ConquestApiRequestEntity.  # noqa: E501
        :type: ConquestApiRequestRecord
        """

        self._record = record

    @property
    def reference_id(self):
        """Gets the reference_id of this ConquestApiRequestEntity.  # noqa: E501


        :return: The reference_id of this ConquestApiRequestEntity.  # noqa: E501
        :rtype: str
        """
        return self._reference_id

    @reference_id.setter
    def reference_id(self, reference_id):
        """Sets the reference_id of this ConquestApiRequestEntity.


        :param reference_id: The reference_id of this ConquestApiRequestEntity.  # noqa: E501
        :type: str
        """

        self._reference_id = reference_id

    @property
    def lock(self):
        """Gets the lock of this ConquestApiRequestEntity.  # noqa: E501


        :return: The lock of this ConquestApiRequestEntity.  # noqa: E501
        :rtype: ConquestApiLock
        """
        return self._lock

    @lock.setter
    def lock(self, lock):
        """Sets the lock of this ConquestApiRequestEntity.


        :param lock: The lock of this ConquestApiRequestEntity.  # noqa: E501
        :type: ConquestApiLock
        """

        self._lock = lock

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
        if issubclass(ConquestApiRequestEntity, dict):
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
        if not isinstance(other, ConquestApiRequestEntity):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiRequestEntity):
            return True

        return self.to_dict() != other.to_dict()
