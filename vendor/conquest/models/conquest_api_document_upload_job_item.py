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


class ConquestApiDocumentUploadJobItem(object):
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
        'created': 'datetime',
        'doc_id': 'str',
        'doc_type': 'str',
        'fail_message': 'str',
        'id': 'str',
        'is_upload_success': 'bool',
        'original_address_in_record': 'str',
        'original_address_to_file_system': 'str',
        'upload_uri': 'str',
        'upload_uri_expires': 'datetime'
    }

    attribute_map = {
        'created': 'Created',
        'doc_id': 'DocID',
        'doc_type': 'DocType',
        'fail_message': 'FailMessage',
        'id': 'ID',
        'is_upload_success': 'IsUploadSuccess',
        'original_address_in_record': 'OriginalAddressInRecord',
        'original_address_to_file_system': 'OriginalAddressToFileSystem',
        'upload_uri': 'UploadUri',
        'upload_uri_expires': 'UploadUriExpires'
    }

    def __init__(self, created=None, doc_id=None, doc_type=None, fail_message=None, id=None, is_upload_success=None, original_address_in_record=None, original_address_to_file_system=None, upload_uri=None, upload_uri_expires=None, _configuration=None):  # noqa: E501
        """ConquestApiDocumentUploadJobItem - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._created = None
        self._doc_id = None
        self._doc_type = None
        self._fail_message = None
        self._id = None
        self._is_upload_success = None
        self._original_address_in_record = None
        self._original_address_to_file_system = None
        self._upload_uri = None
        self._upload_uri_expires = None
        self.discriminator = None

        if created is not None:
            self.created = created
        if doc_id is not None:
            self.doc_id = doc_id
        if doc_type is not None:
            self.doc_type = doc_type
        if fail_message is not None:
            self.fail_message = fail_message
        if id is not None:
            self.id = id
        if is_upload_success is not None:
            self.is_upload_success = is_upload_success
        if original_address_in_record is not None:
            self.original_address_in_record = original_address_in_record
        if original_address_to_file_system is not None:
            self.original_address_to_file_system = original_address_to_file_system
        if upload_uri is not None:
            self.upload_uri = upload_uri
        if upload_uri_expires is not None:
            self.upload_uri_expires = upload_uri_expires

    @property
    def created(self):
        """Gets the created of this ConquestApiDocumentUploadJobItem.  # noqa: E501


        :return: The created of this ConquestApiDocumentUploadJobItem.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ConquestApiDocumentUploadJobItem.


        :param created: The created of this ConquestApiDocumentUploadJobItem.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def doc_id(self):
        """Gets the doc_id of this ConquestApiDocumentUploadJobItem.  # noqa: E501


        :return: The doc_id of this ConquestApiDocumentUploadJobItem.  # noqa: E501
        :rtype: str
        """
        return self._doc_id

    @doc_id.setter
    def doc_id(self, doc_id):
        """Sets the doc_id of this ConquestApiDocumentUploadJobItem.


        :param doc_id: The doc_id of this ConquestApiDocumentUploadJobItem.  # noqa: E501
        :type: str
        """

        self._doc_id = doc_id

    @property
    def doc_type(self):
        """Gets the doc_type of this ConquestApiDocumentUploadJobItem.  # noqa: E501


        :return: The doc_type of this ConquestApiDocumentUploadJobItem.  # noqa: E501
        :rtype: str
        """
        return self._doc_type

    @doc_type.setter
    def doc_type(self, doc_type):
        """Sets the doc_type of this ConquestApiDocumentUploadJobItem.


        :param doc_type: The doc_type of this ConquestApiDocumentUploadJobItem.  # noqa: E501
        :type: str
        """

        self._doc_type = doc_type

    @property
    def fail_message(self):
        """Gets the fail_message of this ConquestApiDocumentUploadJobItem.  # noqa: E501


        :return: The fail_message of this ConquestApiDocumentUploadJobItem.  # noqa: E501
        :rtype: str
        """
        return self._fail_message

    @fail_message.setter
    def fail_message(self, fail_message):
        """Sets the fail_message of this ConquestApiDocumentUploadJobItem.


        :param fail_message: The fail_message of this ConquestApiDocumentUploadJobItem.  # noqa: E501
        :type: str
        """

        self._fail_message = fail_message

    @property
    def id(self):
        """Gets the id of this ConquestApiDocumentUploadJobItem.  # noqa: E501


        :return: The id of this ConquestApiDocumentUploadJobItem.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConquestApiDocumentUploadJobItem.


        :param id: The id of this ConquestApiDocumentUploadJobItem.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def is_upload_success(self):
        """Gets the is_upload_success of this ConquestApiDocumentUploadJobItem.  # noqa: E501


        :return: The is_upload_success of this ConquestApiDocumentUploadJobItem.  # noqa: E501
        :rtype: bool
        """
        return self._is_upload_success

    @is_upload_success.setter
    def is_upload_success(self, is_upload_success):
        """Sets the is_upload_success of this ConquestApiDocumentUploadJobItem.


        :param is_upload_success: The is_upload_success of this ConquestApiDocumentUploadJobItem.  # noqa: E501
        :type: bool
        """

        self._is_upload_success = is_upload_success

    @property
    def original_address_in_record(self):
        """Gets the original_address_in_record of this ConquestApiDocumentUploadJobItem.  # noqa: E501


        :return: The original_address_in_record of this ConquestApiDocumentUploadJobItem.  # noqa: E501
        :rtype: str
        """
        return self._original_address_in_record

    @original_address_in_record.setter
    def original_address_in_record(self, original_address_in_record):
        """Sets the original_address_in_record of this ConquestApiDocumentUploadJobItem.


        :param original_address_in_record: The original_address_in_record of this ConquestApiDocumentUploadJobItem.  # noqa: E501
        :type: str
        """

        self._original_address_in_record = original_address_in_record

    @property
    def original_address_to_file_system(self):
        """Gets the original_address_to_file_system of this ConquestApiDocumentUploadJobItem.  # noqa: E501


        :return: The original_address_to_file_system of this ConquestApiDocumentUploadJobItem.  # noqa: E501
        :rtype: str
        """
        return self._original_address_to_file_system

    @original_address_to_file_system.setter
    def original_address_to_file_system(self, original_address_to_file_system):
        """Sets the original_address_to_file_system of this ConquestApiDocumentUploadJobItem.


        :param original_address_to_file_system: The original_address_to_file_system of this ConquestApiDocumentUploadJobItem.  # noqa: E501
        :type: str
        """

        self._original_address_to_file_system = original_address_to_file_system

    @property
    def upload_uri(self):
        """Gets the upload_uri of this ConquestApiDocumentUploadJobItem.  # noqa: E501


        :return: The upload_uri of this ConquestApiDocumentUploadJobItem.  # noqa: E501
        :rtype: str
        """
        return self._upload_uri

    @upload_uri.setter
    def upload_uri(self, upload_uri):
        """Sets the upload_uri of this ConquestApiDocumentUploadJobItem.


        :param upload_uri: The upload_uri of this ConquestApiDocumentUploadJobItem.  # noqa: E501
        :type: str
        """

        self._upload_uri = upload_uri

    @property
    def upload_uri_expires(self):
        """Gets the upload_uri_expires of this ConquestApiDocumentUploadJobItem.  # noqa: E501


        :return: The upload_uri_expires of this ConquestApiDocumentUploadJobItem.  # noqa: E501
        :rtype: datetime
        """
        return self._upload_uri_expires

    @upload_uri_expires.setter
    def upload_uri_expires(self, upload_uri_expires):
        """Sets the upload_uri_expires of this ConquestApiDocumentUploadJobItem.


        :param upload_uri_expires: The upload_uri_expires of this ConquestApiDocumentUploadJobItem.  # noqa: E501
        :type: datetime
        """

        self._upload_uri_expires = upload_uri_expires

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
        if issubclass(ConquestApiDocumentUploadJobItem, dict):
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
        if not isinstance(other, ConquestApiDocumentUploadJobItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiDocumentUploadJobItem):
            return True

        return self.to_dict() != other.to_dict()
