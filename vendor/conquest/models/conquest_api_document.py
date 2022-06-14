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


class ConquestApiDocument(object):
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
        'content': 'str',
        'content_length': 'str',
        'content_type': 'str',
        'create_time': 'datetime',
        'created_by': 'str',
        'document_description': 'str',
        'document_id': 'int',
        'file_should_be_accessible': 'bool',
        'link': 'str',
        'object_key': 'ConquestApiObjectKey',
        'order': 'int',
        'upload_status': 'ConquestApiUploadStatus'
    }

    attribute_map = {
        'content': 'Content',
        'content_length': 'ContentLength',
        'content_type': 'ContentType',
        'create_time': 'CreateTime',
        'created_by': 'CreatedBy',
        'document_description': 'DocumentDescription',
        'document_id': 'DocumentID',
        'file_should_be_accessible': 'FileShouldBeAccessible',
        'link': 'Link',
        'object_key': 'ObjectKey',
        'order': 'Order',
        'upload_status': 'UploadStatus'
    }

    def __init__(self, content=None, content_length=None, content_type=None, create_time=None, created_by=None, document_description=None, document_id=None, file_should_be_accessible=None, link=None, object_key=None, order=None, upload_status=None, _configuration=None):  # noqa: E501
        """ConquestApiDocument - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._content = None
        self._content_length = None
        self._content_type = None
        self._create_time = None
        self._created_by = None
        self._document_description = None
        self._document_id = None
        self._file_should_be_accessible = None
        self._link = None
        self._object_key = None
        self._order = None
        self._upload_status = None
        self.discriminator = None

        if content is not None:
            self.content = content
        if content_length is not None:
            self.content_length = content_length
        if content_type is not None:
            self.content_type = content_type
        if create_time is not None:
            self.create_time = create_time
        if created_by is not None:
            self.created_by = created_by
        if document_description is not None:
            self.document_description = document_description
        if document_id is not None:
            self.document_id = document_id
        if file_should_be_accessible is not None:
            self.file_should_be_accessible = file_should_be_accessible
        if link is not None:
            self.link = link
        if object_key is not None:
            self.object_key = object_key
        if order is not None:
            self.order = order
        if upload_status is not None:
            self.upload_status = upload_status

    @property
    def content(self):
        """Gets the content of this ConquestApiDocument.  # noqa: E501


        :return: The content of this ConquestApiDocument.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ConquestApiDocument.


        :param content: The content of this ConquestApiDocument.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def content_length(self):
        """Gets the content_length of this ConquestApiDocument.  # noqa: E501


        :return: The content_length of this ConquestApiDocument.  # noqa: E501
        :rtype: str
        """
        return self._content_length

    @content_length.setter
    def content_length(self, content_length):
        """Sets the content_length of this ConquestApiDocument.


        :param content_length: The content_length of this ConquestApiDocument.  # noqa: E501
        :type: str
        """

        self._content_length = content_length

    @property
    def content_type(self):
        """Gets the content_type of this ConquestApiDocument.  # noqa: E501


        :return: The content_type of this ConquestApiDocument.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this ConquestApiDocument.


        :param content_type: The content_type of this ConquestApiDocument.  # noqa: E501
        :type: str
        """

        self._content_type = content_type

    @property
    def create_time(self):
        """Gets the create_time of this ConquestApiDocument.  # noqa: E501


        :return: The create_time of this ConquestApiDocument.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ConquestApiDocument.


        :param create_time: The create_time of this ConquestApiDocument.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def created_by(self):
        """Gets the created_by of this ConquestApiDocument.  # noqa: E501


        :return: The created_by of this ConquestApiDocument.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ConquestApiDocument.


        :param created_by: The created_by of this ConquestApiDocument.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def document_description(self):
        """Gets the document_description of this ConquestApiDocument.  # noqa: E501


        :return: The document_description of this ConquestApiDocument.  # noqa: E501
        :rtype: str
        """
        return self._document_description

    @document_description.setter
    def document_description(self, document_description):
        """Sets the document_description of this ConquestApiDocument.


        :param document_description: The document_description of this ConquestApiDocument.  # noqa: E501
        :type: str
        """

        self._document_description = document_description

    @property
    def document_id(self):
        """Gets the document_id of this ConquestApiDocument.  # noqa: E501


        :return: The document_id of this ConquestApiDocument.  # noqa: E501
        :rtype: int
        """
        return self._document_id

    @document_id.setter
    def document_id(self, document_id):
        """Sets the document_id of this ConquestApiDocument.


        :param document_id: The document_id of this ConquestApiDocument.  # noqa: E501
        :type: int
        """

        self._document_id = document_id

    @property
    def file_should_be_accessible(self):
        """Gets the file_should_be_accessible of this ConquestApiDocument.  # noqa: E501

        FileShouldBeAccessible reports whether the document file SHOULD be accessible.  This depends on two things: - Is the file from a correctly configured document location? - Has the file been uploaded successfully (UploadStatus_Completed)?  # noqa: E501

        :return: The file_should_be_accessible of this ConquestApiDocument.  # noqa: E501
        :rtype: bool
        """
        return self._file_should_be_accessible

    @file_should_be_accessible.setter
    def file_should_be_accessible(self, file_should_be_accessible):
        """Sets the file_should_be_accessible of this ConquestApiDocument.

        FileShouldBeAccessible reports whether the document file SHOULD be accessible.  This depends on two things: - Is the file from a correctly configured document location? - Has the file been uploaded successfully (UploadStatus_Completed)?  # noqa: E501

        :param file_should_be_accessible: The file_should_be_accessible of this ConquestApiDocument.  # noqa: E501
        :type: bool
        """

        self._file_should_be_accessible = file_should_be_accessible

    @property
    def link(self):
        """Gets the link of this ConquestApiDocument.  # noqa: E501

        Link is the location from which a document can be accessed. It is calculated from the document Address.  Link is empty when a location requires accessing a document with a security token.  All uploaded documents will have an empty Link field.  You can obtain an appropriate link which encodes a security token using the GenerateDocumentLinkCommand OR use the \"/download/document?object_type=...&object_id=...&document_id=...\" endpoint which will either serve    the file or redirect to a link, potentially generated by the GenerateDocumentLinkCommand  # noqa: E501

        :return: The link of this ConquestApiDocument.  # noqa: E501
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this ConquestApiDocument.

        Link is the location from which a document can be accessed. It is calculated from the document Address.  Link is empty when a location requires accessing a document with a security token.  All uploaded documents will have an empty Link field.  You can obtain an appropriate link which encodes a security token using the GenerateDocumentLinkCommand OR use the \"/download/document?object_type=...&object_id=...&document_id=...\" endpoint which will either serve    the file or redirect to a link, potentially generated by the GenerateDocumentLinkCommand  # noqa: E501

        :param link: The link of this ConquestApiDocument.  # noqa: E501
        :type: str
        """

        self._link = link

    @property
    def object_key(self):
        """Gets the object_key of this ConquestApiDocument.  # noqa: E501


        :return: The object_key of this ConquestApiDocument.  # noqa: E501
        :rtype: ConquestApiObjectKey
        """
        return self._object_key

    @object_key.setter
    def object_key(self, object_key):
        """Sets the object_key of this ConquestApiDocument.


        :param object_key: The object_key of this ConquestApiDocument.  # noqa: E501
        :type: ConquestApiObjectKey
        """

        self._object_key = object_key

    @property
    def order(self):
        """Gets the order of this ConquestApiDocument.  # noqa: E501


        :return: The order of this ConquestApiDocument.  # noqa: E501
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ConquestApiDocument.


        :param order: The order of this ConquestApiDocument.  # noqa: E501
        :type: int
        """

        self._order = order

    @property
    def upload_status(self):
        """Gets the upload_status of this ConquestApiDocument.  # noqa: E501


        :return: The upload_status of this ConquestApiDocument.  # noqa: E501
        :rtype: ConquestApiUploadStatus
        """
        return self._upload_status

    @upload_status.setter
    def upload_status(self, upload_status):
        """Sets the upload_status of this ConquestApiDocument.


        :param upload_status: The upload_status of this ConquestApiDocument.  # noqa: E501
        :type: ConquestApiUploadStatus
        """

        self._upload_status = upload_status

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
        if issubclass(ConquestApiDocument, dict):
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
        if not isinstance(other, ConquestApiDocument):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConquestApiDocument):
            return True

        return self.to_dict() != other.to_dict()
