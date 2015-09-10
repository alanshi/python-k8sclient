# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from pprint import pformat
from six import iteritems


class V1ServiceSpec(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        Swagger model

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'ports': 'list[V1ServicePort]',
            'selector': 'str',
            'cluster_ip': 'str',
            'type': 'str',
            'deprecated_public_i_ps': 'list[str]',
            'session_affinity': 'str'
        }

        self.attribute_map = {
            'ports': 'ports',
            'selector': 'selector',
            'cluster_ip': 'clusterIP',
            'type': 'type',
            'deprecated_public_i_ps': 'deprecatedPublicIPs',
            'session_affinity': 'sessionAffinity'
        }

        self._ports = None
        self._selector = None
        self._cluster_ip = None
        self._type = None
        self._deprecated_public_i_ps = None
        self._session_affinity = None

    @property
    def ports(self):
        """
        Gets the ports of this V1ServiceSpec.
        ports exposed by the service; see http://releases.k8s.io/v1.0.4/docs/services.md#virtual-ips-and-service-proxies

        :return: The ports of this V1ServiceSpec.
        :rtype: list[V1ServicePort]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """
        Sets the ports of this V1ServiceSpec.
        ports exposed by the service; see http://releases.k8s.io/v1.0.4/docs/services.md#virtual-ips-and-service-proxies

        :param ports: The ports of this V1ServiceSpec.
        :type: list[V1ServicePort]
        """
        self._ports = ports

    @property
    def selector(self):
        """
        Gets the selector of this V1ServiceSpec.
        label keys and values that must match in order to receive traffic for this service; if empty, all pods are selected, if not specified, endpoints must be manually specified; see http://releases.k8s.io/v1.0.4/docs/services.md#overview

        :return: The selector of this V1ServiceSpec.
        :rtype: str
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """
        Sets the selector of this V1ServiceSpec.
        label keys and values that must match in order to receive traffic for this service; if empty, all pods are selected, if not specified, endpoints must be manually specified; see http://releases.k8s.io/v1.0.4/docs/services.md#overview

        :param selector: The selector of this V1ServiceSpec.
        :type: str
        """
        self._selector = selector

    @property
    def cluster_ip(self):
        """
        Gets the cluster_ip of this V1ServiceSpec.
        IP address of the service; usually assigned by the system; if specified, it will be allocated to the service if unused or else creation of the service will fail; cannot be updated; 'None' can be specified for a headless service when proxying is not required; see http://releases.k8s.io/v1.0.4/docs/services.md#virtual-ips-and-service-proxies

        :return: The cluster_ip of this V1ServiceSpec.
        :rtype: str
        """
        return self._cluster_ip

    @cluster_ip.setter
    def cluster_ip(self, cluster_ip):
        """
        Sets the cluster_ip of this V1ServiceSpec.
        IP address of the service; usually assigned by the system; if specified, it will be allocated to the service if unused or else creation of the service will fail; cannot be updated; 'None' can be specified for a headless service when proxying is not required; see http://releases.k8s.io/v1.0.4/docs/services.md#virtual-ips-and-service-proxies

        :param cluster_ip: The cluster_ip of this V1ServiceSpec.
        :type: str
        """
        self._cluster_ip = cluster_ip

    @property
    def type(self):
        """
        Gets the type of this V1ServiceSpec.
        type of this service; must be ClusterIP, NodePort, or LoadBalancer; defaults to ClusterIP; see http://releases.k8s.io/v1.0.4/docs/services.md#external-services

        :return: The type of this V1ServiceSpec.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this V1ServiceSpec.
        type of this service; must be ClusterIP, NodePort, or LoadBalancer; defaults to ClusterIP; see http://releases.k8s.io/v1.0.4/docs/services.md#external-services

        :param type: The type of this V1ServiceSpec.
        :type: str
        """
        self._type = type

    @property
    def deprecated_public_i_ps(self):
        """
        Gets the deprecated_public_i_ps of this V1ServiceSpec.
        deprecated. externally visible IPs (e.g. load balancers) that should be proxied to this service

        :return: The deprecated_public_i_ps of this V1ServiceSpec.
        :rtype: list[str]
        """
        return self._deprecated_public_i_ps

    @deprecated_public_i_ps.setter
    def deprecated_public_i_ps(self, deprecated_public_i_ps):
        """
        Sets the deprecated_public_i_ps of this V1ServiceSpec.
        deprecated. externally visible IPs (e.g. load balancers) that should be proxied to this service

        :param deprecated_public_i_ps: The deprecated_public_i_ps of this V1ServiceSpec.
        :type: list[str]
        """
        self._deprecated_public_i_ps = deprecated_public_i_ps

    @property
    def session_affinity(self):
        """
        Gets the session_affinity of this V1ServiceSpec.
        enable client IP based session affinity; must be ClientIP or None; defaults to None; see http://releases.k8s.io/v1.0.4/docs/services.md#virtual-ips-and-service-proxies

        :return: The session_affinity of this V1ServiceSpec.
        :rtype: str
        """
        return self._session_affinity

    @session_affinity.setter
    def session_affinity(self, session_affinity):
        """
        Sets the session_affinity of this V1ServiceSpec.
        enable client IP based session affinity; must be ClientIP or None; defaults to None; see http://releases.k8s.io/v1.0.4/docs/services.md#virtual-ips-and-service-proxies

        :param session_affinity: The session_affinity of this V1ServiceSpec.
        :type: str
        """
        self._session_affinity = session_affinity

    def to_dict(self):
        """
        Return model properties dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Return model properties str
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()
