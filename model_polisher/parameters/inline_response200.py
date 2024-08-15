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

class InlineResponse200(object):
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
        'run_id': 'RunId',
        'diff': 'Diff',
        'model_file': 'Base64ModelFile'
    }

    attribute_map = {
        'run_id': 'runId',
        'diff': 'diff',
        'model_file': 'modelFile'
    }

    def __init__(self, run_id=None, diff=None, model_file=None):  # noqa: E501
        """InlineResponse200 - a model defined in Swagger"""  # noqa: E501
        self._run_id = None
        self._diff = None
        self._model_file = None
        self.discriminator = None
        if run_id is not None:
            self.run_id = run_id
        if diff is not None:
            self.diff = diff
        if model_file is not None:
            self.model_file = model_file

    @property
    def run_id(self):
        """Gets the run_id of this InlineResponse200.  # noqa: E501


        :return: The run_id of this InlineResponse200.  # noqa: E501
        :rtype: RunId
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this InlineResponse200.


        :param run_id: The run_id of this InlineResponse200.  # noqa: E501
        :type: RunId
        """

        self._run_id = run_id

    @property
    def diff(self):
        """Gets the diff of this InlineResponse200.  # noqa: E501


        :return: The diff of this InlineResponse200.  # noqa: E501
        :rtype: Diff
        """
        return self._diff

    @diff.setter
    def diff(self, diff):
        """Sets the diff of this InlineResponse200.


        :param diff: The diff of this InlineResponse200.  # noqa: E501
        :type: Diff
        """

        self._diff = diff

    @property
    def model_file(self):
        """Gets the model_file of this InlineResponse200.  # noqa: E501


        :return: The model_file of this InlineResponse200.  # noqa: E501
        :rtype: Base64ModelFile
        """
        return self._model_file

    @model_file.setter
    def model_file(self, model_file):
        """Sets the model_file of this InlineResponse200.


        :param model_file: The model_file of this InlineResponse200.  # noqa: E501
        :type: Base64ModelFile
        """

        self._model_file = model_file

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
        if issubclass(InlineResponse200, dict):
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
        if not isinstance(other, InlineResponse200):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other