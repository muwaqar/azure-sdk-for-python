# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class NetworkStatusContract(Model):
    """Network Status details.

    All required parameters must be populated in order to send to Azure.

    :param dns_servers: Required. Gets the list of DNS servers IPV4 addresses.
    :type dns_servers: list[str]
    :param connectivity_status: Required. Gets the list of Connectivity Status
     to the Resources on which the service depends upon.
    :type connectivity_status:
     list[~azure.mgmt.apimanagement.models.ConnectivityStatusContract]
    """

    _validation = {
        'dns_servers': {'required': True},
        'connectivity_status': {'required': True},
    }

    _attribute_map = {
        'dns_servers': {'key': 'dnsServers', 'type': '[str]'},
        'connectivity_status': {'key': 'connectivityStatus', 'type': '[ConnectivityStatusContract]'},
    }

    def __init__(self, **kwargs):
        super(NetworkStatusContract, self).__init__(**kwargs)
        self.dns_servers = kwargs.get('dns_servers', None)
        self.connectivity_status = kwargs.get('connectivity_status', None)
