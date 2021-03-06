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


class ConquestApiReportDefinition(object):
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
        'external_report': 'bool',
        'filters': 'str',
        '_from': 'str',
        'group_by': 'str',
        'has_filter': 'bool',
        'having': 'str',
        'rep_cat_id': 'int',
        'report_definition': 'str',
        'report_name': 'str',
        'report_type': 'str',
        'report_xml': 'str',
        'select': 'str',
        'user_data': 'bool',
        'where': 'str'
    }

    attribute_map = {
        'attribute_id': 'AttributeID',
        'external_report': 'ExternalReport',
        'filters': 'Filters',
        '_from': 'From',
        'group_by': 'GroupBy',
        'has_filter': 'HasFilter',
        'having': 'Having',
        'rep_cat_id': 'RepCatID',
        'report_definition': 'ReportDefinition',
        'report_name': 'ReportName',
        'report_type': 'ReportType',
        'report_xml': 'ReportXML',
        'select': 'Select',
        'user_data': 'UserData',
        'where': 'Where'
    }

    def __init__(self, attribute_id=None, external_report=None, filters=None, _from=None, group_by=None, has_filter=None, having=None, rep_cat_id=None, report_definition=None, report_name=None, report_type=None, report_xml=None, select=None, user_data=None, where=None, _configuration=None):  # noqa: E501
        """ConquestApiReportDefinition - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._attribute_id = None
        self._external_report = None
        self._filters = None
        self.__from = None
        self._group_by = None
        self._has_filter = None
        self._having = None
        self._rep_cat_id = None
        self._report_definition = None
        self._report_name = None
        self._report_type = None
        self._report_xml = None
        self._select = None
        self._user_data = None
        self._where = None
        self.discriminator = None

        if attribute_id is not None:
            self.attribute_id = attribute_id
        if external_report is not None:
            self.external_report = external_report
        if filters is not None:
            self.filters = filters
        if _from is not None:
            self._from = _from
        if group_by is not None:
            self.group_by = group_by
        if has_filter is not None:
            self.has_filter = has_filter
        if having is not None:
            self.having = having
        if rep_cat_id is not None:
            self.rep_cat_id = rep_cat_id
        if report_definition is not None:
            self.report_definition = report_definition
        if report_name is not None:
            self.report_name = report_name
        if report_type is not None:
            self.report_type = report_type
        if report_xml is not None:
            self.report_xml = report_xml
        if select is not None:
            self.select = select
        if user_data is not None:
            self.user_data = user_data
        if where is not None:
            self.where = where

    @property
    def attribute_id(self):
        """Gets the attribute_id of this ConquestApiReportDefinition.  # noqa: E501


        :return: The attribute_id of this ConquestApiReportDefinition.  # noqa: E501
        :rtype: int
        """
        return self._attribute_id

    @attribute_id.setter
    def attribute_id(self, attribute_id):
        """Sets the attribute_id of this ConquestApiReportDefinition.


        :param attribute_id: The attribute_id of this ConquestApiReportDefinition.  # noqa: E501
        :type: int
        """

        self._attribute_id = attribute_id

    @property
    def external_report(self):
        """Gets the external_report of this ConquestApiReportDefinition.  # noqa: E501


        :return: The external_report of this ConquestApiReportDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._external_report

    @external_report.setter
    def external_report(self, external_report):
        """Sets the external_report of this ConquestApiReportDefinition.


        :param external_report: The external_report of this ConquestApiReportDefinition.  # noqa: E501
        :type: bool
        """

        self._external_report = external_report

    @property
    def filters(self):
        """Gets the filters of this ConquestApiReportDefinition.  # noqa: E501


        :return: The filters of this ConquestApiReportDefinition.  # noqa: E501
        :rtype: str
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this ConquestApiReportDefinition.


        :param filters: The filters of this ConquestApiReportDefinition.  # noqa: E501
        :type: str
        """

        self._filters = filters

    @property
    def _from(self):
        """Gets the _from of this ConquestApiReportDefinition.  # noqa: E501


        :return: The _from of this ConquestApiReportDefinition.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ConquestApiReportDefinition.


        :param _from: The _from of this ConquestApiReportDefinition.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def group_by(self):
        """Gets the group_by of this ConquestApiReportDefinition.  # noqa: E501


        :return: The group_by of this ConquestApiReportDefinition.  # noqa: E501
        :rtype: str
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this ConquestApiReportDefinition.


        :param group_by: The group_by of this ConquestApiReportDefinition.  # noqa: E501
        :type: str
        """

        self._group_by = group_by

    @property
    def has_filter(self):
        """Gets the has_filter of this ConquestApiReportDefinition.  # noqa: E501


        :return: The has_filter of this ConquestApiReportDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._has_filter

    @has_filter.setter
    def has_filter(self, has_filter):
        """Sets the has_filter of this ConquestApiReportDefinition.


        :param has_filter: The has_filter of this ConquestApiReportDefinition.  # noqa: E501
        :type: bool
        """

        self._has_filter = has_filter

    @property
    def having(self):
        """Gets the having of this ConquestApiReportDefinition.  # noqa: E501


        :return: The having of this ConquestApiReportDefinition.  # noqa: E501
        :rtype: str
        """
        return self._having

    @having.setter
    def having(self, having):
        """Sets the having of this ConquestApiReportDefinition.


        :param having: The having of this ConquestApiReportDefinition.  # noqa: E501
        :type: str
        """

        self._having = having

    @property
    def rep_cat_id(self):
        """Gets the rep_cat_id of this ConquestApiReportDefinition.  # noqa: E501


        :return: The rep_cat_id of this ConquestApiReportDefinition.  # noqa: E501
        :rtype: int
        """
        return self._rep_cat_id

    @rep_cat_id.setter
    def rep_cat_id(self, rep_cat_id):
        """Sets the rep_cat_id of this ConquestApiReportDefinition.


        :param rep_cat_id: The rep_cat_id of this ConquestApiReportDefinition.  # noqa: E501
        :type: int
        """

        self._rep_cat_id = rep_cat_id

    @property
    def report_definition(self):
        """Gets the report_definition of this ConquestApiReportDefinition.  # noqa: E501


        :return: The report_definition of this ConquestApiReportDefinition.  # noqa: E501
        :rtype: str
        """
        return self._report_definition

    @report_definition.setter
    def report_definition(self, report_definition):
        """Sets the report_definition of this ConquestApiReportDefinition.


        :param report_definition: The report_definition of this ConquestApiReportDefinition.  # noqa: E501
        :type: str
        """

        self._report_definition = report_definition

    @property
    def report_name(self):
        """Gets the report_name of this ConquestApiReportDefinition.  # noqa: E501


        :return: The report_name of this ConquestApiReportDefinition.  # noqa: E501
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        """Sets the report_name of this ConquestApiReportDefinition.


        :param report_name: The report_name of this ConquestApiReportDefinition.  # noqa: E501
        :type: str
        """

        self._report_name = report_name

    @property
    def report_type(self):
        """Gets the report_type of this ConquestApiReportDefinition.  # noqa: E501


        :return: The report_type of this ConquestApiReportDefinition.  # noqa: E501
        :rtype: str
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """Sets the report_type of this ConquestApiReportDefinition.


        :param report_type: The report_type of this ConquestApiReportDefinition.  # noqa: E501
        :type: str
        """

        self._report_type = report_type

    @property
    def report_xml(self):
        """Gets the report_xml of this ConquestApiReportDefinition.  # noqa: E501


        :return: The report_xml of this ConquestApiReportDefinition.  # noqa: E501
        :rtype: str
        """
        return self._report_xml

    @report_xml.setter
    def report_xml(self, report_xml):
        """Sets the report_xml of this ConquestApiReportDefinition.


        :param report_xml: The report_xml of this ConquestApiReportDefinition.  # noqa: E501
        :type: str
        """

        self._report_xml = report_xml

    @property
    def select(self):
        """Gets the select of this ConquestApiReportDefinition.  # noqa: E501


        :return: The select of this ConquestApiReportDefinition.  # noqa: E501
        :rtype: str
        """
        return self._select

    @select.setter
    def select(self, select):
        """Sets the select of this ConquestApiReportDefinition.


        :param select: The select of this ConquestApiReportDefinition.  # noqa: E501
        :type: str
        """

        self._select = select

    @property
    def user_data(self):
        """Gets the user_data of this ConquestApiReportDefinition.  # noqa: E501


        :return: The user_data of this ConquestApiReportDefinition.  # noqa: E501
        :rtype: bool
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        """Sets the user_data of this ConquestApiReportDefinition.


        :param user_data: The user_data of this ConquestApiReportDefinition.  # noqa: E501
        :type: bool
        """

        self._user_data = user_data

    @property
    def where(self):
        """Gets the where of this ConquestApiReportDefinition.  # noqa: E501


        :return: The where of this ConquestApiReportDefinition.  # noqa: E501
        :rtype: str
        """
        return self._where

    @where.setter
    def where(self, where):
        """Sets the where of this ConquestApiReportDefinition.


        :param where: The where of this ConquestApiReportDefinition.  # noqa: E501
        :type: str
        """

        self._where = where

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
        if issubclass(ConquestApiReportDefinition, dict):
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
        if not isinstance(other, ConquestApiReportDefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiReportDefinition):
            return True

        return self.to_dict() != other.to_dict()
