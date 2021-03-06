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

class ConquestApiGeoPackageTableDescription(object):
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
        'column_infos': 'list[ConquestApigpkgColumnInfo]',
        'contents': 'ConquestApigpkgContents',
        'data_columns': 'list[ConquestApigpkgDataColumns]',
        'geometry_column': 'ConquestApigpkgGeometryColumns',
        'geometry_columns': 'list[ConquestApigpkgGeometryColumns]',
        'key_column_option': 'ConquestApiGeoPackageKeyColumnDescriptionOption',
        'object_id_column': 'ConquestApigpkgColumnInfo',
        'object_type': 'ConquestApiObjectType',
        'srs_supported': 'bool',
        'table_name': 'str'
    }

    attribute_map = {
        'column_infos': 'ColumnInfos',
        'contents': 'Contents',
        'data_columns': 'DataColumns',
        'geometry_column': 'GeometryColumn',
        'geometry_columns': 'GeometryColumns',
        'key_column_option': 'KeyColumnOption',
        'object_id_column': 'ObjectIDColumn',
        'object_type': 'ObjectType',
        'srs_supported': 'SrsSupported',
        'table_name': 'TableName'
    }

    def __init__(self, column_infos=None, contents=None, data_columns=None, geometry_column=None, geometry_columns=None, key_column_option=None, object_id_column=None, object_type=None, srs_supported=None, table_name=None):  # noqa: E501
        """ConquestApiGeoPackageTableDescription - a model defined in Swagger"""  # noqa: E501
        self._column_infos = None
        self._contents = None
        self._data_columns = None
        self._geometry_column = None
        self._geometry_columns = None
        self._key_column_option = None
        self._object_id_column = None
        self._object_type = None
        self._srs_supported = None
        self._table_name = None
        self.discriminator = None
        if column_infos is not None:
            self.column_infos = column_infos
        if contents is not None:
            self.contents = contents
        if data_columns is not None:
            self.data_columns = data_columns
        if geometry_column is not None:
            self.geometry_column = geometry_column
        if geometry_columns is not None:
            self.geometry_columns = geometry_columns
        if key_column_option is not None:
            self.key_column_option = key_column_option
        if object_id_column is not None:
            self.object_id_column = object_id_column
        if object_type is not None:
            self.object_type = object_type
        if srs_supported is not None:
            self.srs_supported = srs_supported
        if table_name is not None:
            self.table_name = table_name

    @property
    def column_infos(self):
        """Gets the column_infos of this ConquestApiGeoPackageTableDescription.  # noqa: E501


        :return: The column_infos of this ConquestApiGeoPackageTableDescription.  # noqa: E501
        :rtype: list[ConquestApigpkgColumnInfo]
        """
        return self._column_infos

    @column_infos.setter
    def column_infos(self, column_infos):
        """Sets the column_infos of this ConquestApiGeoPackageTableDescription.


        :param column_infos: The column_infos of this ConquestApiGeoPackageTableDescription.  # noqa: E501
        :type: list[ConquestApigpkgColumnInfo]
        """

        self._column_infos = column_infos

    @property
    def contents(self):
        """Gets the contents of this ConquestApiGeoPackageTableDescription.  # noqa: E501


        :return: The contents of this ConquestApiGeoPackageTableDescription.  # noqa: E501
        :rtype: ConquestApigpkgContents
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        """Sets the contents of this ConquestApiGeoPackageTableDescription.


        :param contents: The contents of this ConquestApiGeoPackageTableDescription.  # noqa: E501
        :type: ConquestApigpkgContents
        """

        self._contents = contents

    @property
    def data_columns(self):
        """Gets the data_columns of this ConquestApiGeoPackageTableDescription.  # noqa: E501

        DataColumns are what could be identified in a geo package for a table.  # noqa: E501

        :return: The data_columns of this ConquestApiGeoPackageTableDescription.  # noqa: E501
        :rtype: list[ConquestApigpkgDataColumns]
        """
        return self._data_columns

    @data_columns.setter
    def data_columns(self, data_columns):
        """Sets the data_columns of this ConquestApiGeoPackageTableDescription.

        DataColumns are what could be identified in a geo package for a table.  # noqa: E501

        :param data_columns: The data_columns of this ConquestApiGeoPackageTableDescription.  # noqa: E501
        :type: list[ConquestApigpkgDataColumns]
        """

        self._data_columns = data_columns

    @property
    def geometry_column(self):
        """Gets the geometry_column of this ConquestApiGeoPackageTableDescription.  # noqa: E501


        :return: The geometry_column of this ConquestApiGeoPackageTableDescription.  # noqa: E501
        :rtype: ConquestApigpkgGeometryColumns
        """
        return self._geometry_column

    @geometry_column.setter
    def geometry_column(self, geometry_column):
        """Sets the geometry_column of this ConquestApiGeoPackageTableDescription.


        :param geometry_column: The geometry_column of this ConquestApiGeoPackageTableDescription.  # noqa: E501
        :type: ConquestApigpkgGeometryColumns
        """

        self._geometry_column = geometry_column

    @property
    def geometry_columns(self):
        """Gets the geometry_columns of this ConquestApiGeoPackageTableDescription.  # noqa: E501

        GeometryColumns are what could be identified in a geo package for a table. There can only be one of these per table.  # noqa: E501

        :return: The geometry_columns of this ConquestApiGeoPackageTableDescription.  # noqa: E501
        :rtype: list[ConquestApigpkgGeometryColumns]
        """
        return self._geometry_columns

    @geometry_columns.setter
    def geometry_columns(self, geometry_columns):
        """Sets the geometry_columns of this ConquestApiGeoPackageTableDescription.

        GeometryColumns are what could be identified in a geo package for a table. There can only be one of these per table.  # noqa: E501

        :param geometry_columns: The geometry_columns of this ConquestApiGeoPackageTableDescription.  # noqa: E501
        :type: list[ConquestApigpkgGeometryColumns]
        """

        self._geometry_columns = geometry_columns

    @property
    def key_column_option(self):
        """Gets the key_column_option of this ConquestApiGeoPackageTableDescription.  # noqa: E501


        :return: The key_column_option of this ConquestApiGeoPackageTableDescription.  # noqa: E501
        :rtype: ConquestApiGeoPackageKeyColumnDescriptionOption
        """
        return self._key_column_option

    @key_column_option.setter
    def key_column_option(self, key_column_option):
        """Sets the key_column_option of this ConquestApiGeoPackageTableDescription.


        :param key_column_option: The key_column_option of this ConquestApiGeoPackageTableDescription.  # noqa: E501
        :type: ConquestApiGeoPackageKeyColumnDescriptionOption
        """

        self._key_column_option = key_column_option

    @property
    def object_id_column(self):
        """Gets the object_id_column of this ConquestApiGeoPackageTableDescription.  # noqa: E501


        :return: The object_id_column of this ConquestApiGeoPackageTableDescription.  # noqa: E501
        :rtype: ConquestApigpkgColumnInfo
        """
        return self._object_id_column

    @object_id_column.setter
    def object_id_column(self, object_id_column):
        """Sets the object_id_column of this ConquestApiGeoPackageTableDescription.


        :param object_id_column: The object_id_column of this ConquestApiGeoPackageTableDescription.  # noqa: E501
        :type: ConquestApigpkgColumnInfo
        """

        self._object_id_column = object_id_column

    @property
    def object_type(self):
        """Gets the object_type of this ConquestApiGeoPackageTableDescription.  # noqa: E501


        :return: The object_type of this ConquestApiGeoPackageTableDescription.  # noqa: E501
        :rtype: ConquestApiObjectType
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        """Sets the object_type of this ConquestApiGeoPackageTableDescription.


        :param object_type: The object_type of this ConquestApiGeoPackageTableDescription.  # noqa: E501
        :type: ConquestApiObjectType
        """

        self._object_type = object_type

    @property
    def srs_supported(self):
        """Gets the srs_supported of this ConquestApiGeoPackageTableDescription.  # noqa: E501


        :return: The srs_supported of this ConquestApiGeoPackageTableDescription.  # noqa: E501
        :rtype: bool
        """
        return self._srs_supported

    @srs_supported.setter
    def srs_supported(self, srs_supported):
        """Sets the srs_supported of this ConquestApiGeoPackageTableDescription.


        :param srs_supported: The srs_supported of this ConquestApiGeoPackageTableDescription.  # noqa: E501
        :type: bool
        """

        self._srs_supported = srs_supported

    @property
    def table_name(self):
        """Gets the table_name of this ConquestApiGeoPackageTableDescription.  # noqa: E501


        :return: The table_name of this ConquestApiGeoPackageTableDescription.  # noqa: E501
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this ConquestApiGeoPackageTableDescription.


        :param table_name: The table_name of this ConquestApiGeoPackageTableDescription.  # noqa: E501
        :type: str
        """

        self._table_name = table_name

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
        if issubclass(ConquestApiGeoPackageTableDescription, dict):
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
        if not isinstance(other, ConquestApiGeoPackageTableDescription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
