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


class JobCreateParameters(Model):
    """The parameters supplied to the create job operation.

    :param runbook: Gets or sets the runbook.
    :type runbook: ~azure.mgmt.automation.models.RunbookAssociationProperty
    :param parameters: Gets or sets the parameters of the job.
    :type parameters: dict[str, str]
    :param run_on: Gets or sets the runOn which specifies the group name where
     the job is to be executed.
    :type run_on: str
    """

    _validation = {
        'runbook': {'required': True},
    }

    _attribute_map = {
        'runbook': {'key': 'properties.runbook', 'type': 'RunbookAssociationProperty'},
        'parameters': {'key': 'properties.parameters', 'type': '{str}'},
        'run_on': {'key': 'properties.runOn', 'type': 'str'},
    }

    def __init__(self, runbook, parameters=None, run_on=None):
        super(JobCreateParameters, self).__init__()
        self.runbook = runbook
        self.parameters = parameters
        self.run_on = run_on
