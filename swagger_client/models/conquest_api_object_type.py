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

class ConquestApiObjectType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    NONE = "ObjectType_None"
    ASSET = "ObjectType_Asset"
    ACTION = "ObjectType_Action"
    REQUEST = "ObjectType_Request"
    DEFECT = "ObjectType_Defect"
    LOGBOOK = "ObjectType_LogBook"
    LOGREADING = "ObjectType_LogReading"
    CYCLICACTION = "ObjectType_CyclicAction"
    INSPECTION = "ObjectType_Inspection"
    ORGANISATIONUNIT = "ObjectType_OrganisationUnit"
    CONTRACTOR = "ObjectType_Contractor"
    FILTER = "ObjectType_Filter"
    VIEW = "ObjectType_View"
    QUERY = "ObjectType_Query"
    REPORT = "ObjectType_Report"
    RISKEVENT = "ObjectType_RiskEvent"
    MAPVIEW = "ObjectType_MapView"
    INSPECTIONPROGRAM = "ObjectType_InspectionProgram"
    LOCATION = "ObjectType_Location"
    FUNCTION = "ObjectType_Function"
    RESOURCE = "ObjectType_Resource"
    RESOURCEASSIGNMENT = "ObjectType_ResourceAssignment"
    HIERARCHY = "ObjectType_Hierarchy"
    CODEFIELD = "ObjectType_CodeField"
    CODE = "ObjectType_Code"
    DOCUMENT = "ObjectType_Document"
    DIARYENTRY = "ObjectType_DiaryEntry"
    DETERIORATIONCURVE = "ObjectType_DeteriorationCurve"
    VALUATIONTRANSACTION = "ObjectType_ValuationTransaction"
    DOCUMENTCONTAINER = "ObjectType_DocumentContainer"
    CONDITIONHISTORY = "ObjectType_ConditionHistory"
    ASSETINSPECTION = "ObjectType_AssetInspection"
    DEFECTHISTORY = "ObjectType_DefectHistory"
    ASSETTYPE = "ObjectType_AssetType"
    STANDARDACTION = "ObjectType_StandardAction"
    STANDARDDEFECT = "ObjectType_StandardDefect"
    STANDARDINSPECTION = "ObjectType_StandardInspection"
    STANDARDRISKEVENT = "ObjectType_StandardRiskEvent"
    ACTIONCATEGORY = "ObjectType_ActionCategory"
    ATTRIBUTESET = "ObjectType_AttributeSet"
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self):  # noqa: E501
        """ConquestApiObjectType - a model defined in Swagger"""  # noqa: E501
        self.discriminator = None

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
        if issubclass(ConquestApiObjectType, dict):
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
        if not isinstance(other, ConquestApiObjectType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
