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


class TaskInformation(Model):
    """Information about a task running on a compute node.

    :param task_url: The URL of the task.
    :type task_url: str
    :param job_id: The ID of the job to which the task belongs.
    :type job_id: str
    :param task_id: The ID of the task.
    :type task_id: str
    :param subtask_id: The ID of the subtask if the task is a multi-instance
     task.
    :type subtask_id: int
    :param task_state: The current state of the task. Possible values include:
     'active', 'preparing', 'running', 'completed'
    :type task_state: str or ~azure.batch.models.TaskState
    :param execution_info: Information about the execution of the task.
    :type execution_info: ~azure.batch.models.TaskExecutionInformation
    """

    _validation = {
        'task_state': {'required': True},
    }

    _attribute_map = {
        'task_url': {'key': 'taskUrl', 'type': 'str'},
        'job_id': {'key': 'jobId', 'type': 'str'},
        'task_id': {'key': 'taskId', 'type': 'str'},
        'subtask_id': {'key': 'subtaskId', 'type': 'int'},
        'task_state': {'key': 'taskState', 'type': 'TaskState'},
        'execution_info': {'key': 'executionInfo', 'type': 'TaskExecutionInformation'},
    }

    def __init__(self, task_state, task_url=None, job_id=None, task_id=None, subtask_id=None, execution_info=None):
        self.task_url = task_url
        self.job_id = job_id
        self.task_id = task_id
        self.subtask_id = subtask_id
        self.task_state = task_state
        self.execution_info = execution_info
