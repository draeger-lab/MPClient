# coding: utf-8

"""
    Model Polisher API

    API for the Model Polisher.  # noqa: E501

    OpenAPI spec version: 2.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ConfigSboTerms(object):
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
        'omit_generic_terms': 'bool'
    }

    attribute_map = {
        'omit_generic_terms': 'omitGenericTerms'
    }

    def __init__(self, omit_generic_terms=False):  # noqa: E501
        """ConfigSboTerms - a model defined in Swagger"""  # noqa: E501
        self._omit_generic_terms = None
        self.discriminator = None
        if omit_generic_terms is not None:
            self.omit_generic_terms = omit_generic_terms

    @property
    def omit_generic_terms(self):
        """Gets the omit_generic_terms of this ConfigSboTerms.  # noqa: E501


        :return: The omit_generic_terms of this ConfigSboTerms.  # noqa: E501
        :rtype: bool
        """
        return self._omit_generic_terms

    @omit_generic_terms.setter
    def omit_generic_terms(self, omit_generic_terms):
        """Sets the omit_generic_terms of this ConfigSboTerms.


        :param omit_generic_terms: The omit_generic_terms of this ConfigSboTerms.  # noqa: E501
        :type: bool
        """

        self._omit_generic_terms = omit_generic_terms

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
        if issubclass(ConfigSboTerms, dict):
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
        if not isinstance(other, ConfigSboTerms):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
