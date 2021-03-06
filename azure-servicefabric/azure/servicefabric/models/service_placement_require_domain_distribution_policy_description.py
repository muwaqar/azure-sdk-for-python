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

from .service_placement_policy_description import ServicePlacementPolicyDescription


class ServicePlacementRequireDomainDistributionPolicyDescription(ServicePlacementPolicyDescription):
    """Describes the policy to be used for placement of a Service Fabric service
    where two replicas from the same partition should never be placed in the
    same fault or upgrade domain.
    While this is not common it can expose the service to an increased risk of
    concurrent failures due to unplanned outages or other cases of
    subsequent/concurrent failures. As an example, consider a case where
    replicas are deployed across different data center, with one replica per
    location. In the event that one of the datacenters goes offline, normally
    the replica that was placed in that datacenter will be packed into one of
    the remaining datacenters. If this is not desirable then this policy should
    be set.
    .

    :param type: Constant filled by server.
    :type type: str
    :param domain_name: The name of the domain that should used for placement
     as per this policy.
    :type domain_name: str
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'Type', 'type': 'str'},
        'domain_name': {'key': 'DomainName', 'type': 'str'},
    }

    def __init__(self, domain_name=None):
        super(ServicePlacementRequireDomainDistributionPolicyDescription, self).__init__()
        self.domain_name = domain_name
        self.type = 'RequireDomainDistribution'
