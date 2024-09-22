# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: release-1.31
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from kubernetes.client.configuration import Configuration


class V1beta1VolumeAttributesClass(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'api_version': 'str',
        'driver_name': 'str',
        'kind': 'str',
        'metadata': 'V1ObjectMeta',
        'parameters': 'dict(str, str)'
    }

    attribute_map = {
        'api_version': 'apiVersion',
        'driver_name': 'driverName',
        'kind': 'kind',
        'metadata': 'metadata',
        'parameters': 'parameters'
    }

    def __init__(self, api_version=None, driver_name=None, kind=None, metadata=None, parameters=None, local_vars_configuration=None):  # noqa: E501
        """V1beta1VolumeAttributesClass - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._api_version = None
        self._driver_name = None
        self._kind = None
        self._metadata = None
        self._parameters = None
        self.discriminator = None

        if api_version is not None:
            self.api_version = api_version
        self.driver_name = driver_name
        if kind is not None:
            self.kind = kind
        if metadata is not None:
            self.metadata = metadata
        if parameters is not None:
            self.parameters = parameters

    @property
    def api_version(self):
        """Gets the api_version of this V1beta1VolumeAttributesClass.  # noqa: E501

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :return: The api_version of this V1beta1VolumeAttributesClass.  # noqa: E501
        :rtype: str
        """
        return self._api_version

    @api_version.setter
    def api_version(self, api_version):
        """Sets the api_version of this V1beta1VolumeAttributesClass.

        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources  # noqa: E501

        :param api_version: The api_version of this V1beta1VolumeAttributesClass.  # noqa: E501
        :type: str
        """

        self._api_version = api_version

    @property
    def driver_name(self):
        """Gets the driver_name of this V1beta1VolumeAttributesClass.  # noqa: E501

        Name of the CSI driver This field is immutable.  # noqa: E501

        :return: The driver_name of this V1beta1VolumeAttributesClass.  # noqa: E501
        :rtype: str
        """
        return self._driver_name

    @driver_name.setter
    def driver_name(self, driver_name):
        """Sets the driver_name of this V1beta1VolumeAttributesClass.

        Name of the CSI driver This field is immutable.  # noqa: E501

        :param driver_name: The driver_name of this V1beta1VolumeAttributesClass.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and driver_name is None:  # noqa: E501
            raise ValueError("Invalid value for `driver_name`, must not be `None`")  # noqa: E501

        self._driver_name = driver_name

    @property
    def kind(self):
        """Gets the kind of this V1beta1VolumeAttributesClass.  # noqa: E501

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :return: The kind of this V1beta1VolumeAttributesClass.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this V1beta1VolumeAttributesClass.

        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds  # noqa: E501

        :param kind: The kind of this V1beta1VolumeAttributesClass.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def metadata(self):
        """Gets the metadata of this V1beta1VolumeAttributesClass.  # noqa: E501


        :return: The metadata of this V1beta1VolumeAttributesClass.  # noqa: E501
        :rtype: V1ObjectMeta
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this V1beta1VolumeAttributesClass.


        :param metadata: The metadata of this V1beta1VolumeAttributesClass.  # noqa: E501
        :type: V1ObjectMeta
        """

        self._metadata = metadata

    @property
    def parameters(self):
        """Gets the parameters of this V1beta1VolumeAttributesClass.  # noqa: E501

        parameters hold volume attributes defined by the CSI driver. These values are opaque to the Kubernetes and are passed directly to the CSI driver. The underlying storage provider supports changing these attributes on an existing volume, however the parameters field itself is immutable. To invoke a volume update, a new VolumeAttributesClass should be created with new parameters, and the PersistentVolumeClaim should be updated to reference the new VolumeAttributesClass.  This field is required and must contain at least one key/value pair. The keys cannot be empty, and the maximum number of parameters is 512, with a cumulative max size of 256K. If the CSI driver rejects invalid parameters, the target PersistentVolumeClaim will be set to an \"Infeasible\" state in the modifyVolumeStatus field.  # noqa: E501

        :return: The parameters of this V1beta1VolumeAttributesClass.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this V1beta1VolumeAttributesClass.

        parameters hold volume attributes defined by the CSI driver. These values are opaque to the Kubernetes and are passed directly to the CSI driver. The underlying storage provider supports changing these attributes on an existing volume, however the parameters field itself is immutable. To invoke a volume update, a new VolumeAttributesClass should be created with new parameters, and the PersistentVolumeClaim should be updated to reference the new VolumeAttributesClass.  This field is required and must contain at least one key/value pair. The keys cannot be empty, and the maximum number of parameters is 512, with a cumulative max size of 256K. If the CSI driver rejects invalid parameters, the target PersistentVolumeClaim will be set to an \"Infeasible\" state in the modifyVolumeStatus field.  # noqa: E501

        :param parameters: The parameters of this V1beta1VolumeAttributesClass.  # noqa: E501
        :type: dict(str, str)
        """

        self._parameters = parameters

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, V1beta1VolumeAttributesClass):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, V1beta1VolumeAttributesClass):
            return True

        return self.to_dict() != other.to_dict()
