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

from .proxy_only_resource import ProxyOnlyResource


class SiteConfigResource(ProxyOnlyResource):
    """Web app configuration ARM resource.

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar id: Resource Id.
    :vartype id: str
    :ivar name: Resource Name.
    :vartype name: str
    :param kind: Kind of resource.
    :type kind: str
    :ivar type: Resource type.
    :vartype type: str
    :param number_of_workers: Number of workers.
    :type number_of_workers: int
    :param default_documents: Default documents.
    :type default_documents: list[str]
    :param net_framework_version: .NET Framework version. Default value:
     "v4.6" .
    :type net_framework_version: str
    :param php_version: Version of PHP.
    :type php_version: str
    :param python_version: Version of Python.
    :type python_version: str
    :param node_version: Version of Node.js.
    :type node_version: str
    :param linux_fx_version: Linux App Framework and version
    :type linux_fx_version: str
    :param request_tracing_enabled: <code>true</code> if request tracing is
     enabled; otherwise, <code>false</code>.
    :type request_tracing_enabled: bool
    :param request_tracing_expiration_time: Request tracing expiration time.
    :type request_tracing_expiration_time: datetime
    :param remote_debugging_enabled: <code>true</code> if remote debugging is
     enabled; otherwise, <code>false</code>.
    :type remote_debugging_enabled: bool
    :param remote_debugging_version: Remote debugging version.
    :type remote_debugging_version: str
    :param http_logging_enabled: <code>true</code> if HTTP logging is enabled;
     otherwise, <code>false</code>.
    :type http_logging_enabled: bool
    :param logs_directory_size_limit: HTTP logs directory size limit.
    :type logs_directory_size_limit: int
    :param detailed_error_logging_enabled: <code>true</code> if detailed error
     logging is enabled; otherwise, <code>false</code>.
    :type detailed_error_logging_enabled: bool
    :param publishing_username: Publishing user name.
    :type publishing_username: str
    :param app_settings: Application settings.
    :type app_settings: list[~azure.mgmt.web.models.NameValuePair]
    :param connection_strings: Connection strings.
    :type connection_strings: list[~azure.mgmt.web.models.ConnStringInfo]
    :ivar machine_key: Site MachineKey.
    :vartype machine_key: ~azure.mgmt.web.models.SiteMachineKey
    :param handler_mappings: Handler mappings.
    :type handler_mappings: list[~azure.mgmt.web.models.HandlerMapping]
    :param document_root: Document root.
    :type document_root: str
    :param scm_type: SCM type. Possible values include: 'None', 'Dropbox',
     'Tfs', 'LocalGit', 'GitHub', 'CodePlexGit', 'CodePlexHg', 'BitbucketGit',
     'BitbucketHg', 'ExternalGit', 'ExternalHg', 'OneDrive', 'VSO'
    :type scm_type: str or ~azure.mgmt.web.models.ScmType
    :param use32_bit_worker_process: <code>true</code> to use 32-bit worker
     process; otherwise, <code>false</code>.
    :type use32_bit_worker_process: bool
    :param web_sockets_enabled: <code>true</code> if WebSocket is enabled;
     otherwise, <code>false</code>.
    :type web_sockets_enabled: bool
    :param always_on: <code>true</code> if Always On is enabled; otherwise,
     <code>false</code>.
    :type always_on: bool
    :param java_version: Java version.
    :type java_version: str
    :param java_container: Java container.
    :type java_container: str
    :param java_container_version: Java container version.
    :type java_container_version: str
    :param app_command_line: App command line to launch.
    :type app_command_line: str
    :param managed_pipeline_mode: Managed pipeline mode. Possible values
     include: 'Integrated', 'Classic'
    :type managed_pipeline_mode: str or
     ~azure.mgmt.web.models.ManagedPipelineMode
    :param virtual_applications: Virtual applications.
    :type virtual_applications:
     list[~azure.mgmt.web.models.VirtualApplication]
    :param load_balancing: Site load balancing. Possible values include:
     'WeightedRoundRobin', 'LeastRequests', 'LeastResponseTime',
     'WeightedTotalTraffic', 'RequestHash'
    :type load_balancing: str or ~azure.mgmt.web.models.SiteLoadBalancing
    :param experiments: This is work around for polymophic types.
    :type experiments: ~azure.mgmt.web.models.Experiments
    :param limits: Site limits.
    :type limits: ~azure.mgmt.web.models.SiteLimits
    :param auto_heal_enabled: <code>true</code> if Auto Heal is enabled;
     otherwise, <code>false</code>.
    :type auto_heal_enabled: bool
    :param auto_heal_rules: Auto Heal rules.
    :type auto_heal_rules: ~azure.mgmt.web.models.AutoHealRules
    :param tracing_options: Tracing options.
    :type tracing_options: str
    :param vnet_name: Virtual Network name.
    :type vnet_name: str
    :param cors: Cross-Origin Resource Sharing (CORS) settings.
    :type cors: ~azure.mgmt.web.models.CorsSettings
    :param push: Push endpoint settings.
    :type push: ~azure.mgmt.web.models.PushSettings
    :param api_definition: Information about the formal API definition for the
     app.
    :type api_definition: ~azure.mgmt.web.models.ApiDefinitionInfo
    :param auto_swap_slot_name: Auto-swap slot name.
    :type auto_swap_slot_name: str
    :param local_my_sql_enabled: <code>true</code> to enable local MySQL;
     otherwise, <code>false</code>. Default value: False .
    :type local_my_sql_enabled: bool
    :param ip_security_restrictions: IP security restrictions.
    :type ip_security_restrictions:
     list[~azure.mgmt.web.models.IpSecurityRestriction]
    :param http20_enabled: Http20Enabled: configures a web site to allow
     clients to connect over http2.0. Default value: True .
    :type http20_enabled: bool
    :param min_tls_version: MinTlsVersion: configures the minimum version of
     TLS required for SSL requests. Possible values include: '1.0', '1.1',
     '1.2'
    :type min_tls_version: str or ~azure.mgmt.web.models.SupportedTlsVersions
    """

    _validation = {
        'id': {'readonly': True},
        'name': {'readonly': True},
        'type': {'readonly': True},
        'machine_key': {'readonly': True},
    }

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'number_of_workers': {'key': 'properties.numberOfWorkers', 'type': 'int'},
        'default_documents': {'key': 'properties.defaultDocuments', 'type': '[str]'},
        'net_framework_version': {'key': 'properties.netFrameworkVersion', 'type': 'str'},
        'php_version': {'key': 'properties.phpVersion', 'type': 'str'},
        'python_version': {'key': 'properties.pythonVersion', 'type': 'str'},
        'node_version': {'key': 'properties.nodeVersion', 'type': 'str'},
        'linux_fx_version': {'key': 'properties.linuxFxVersion', 'type': 'str'},
        'request_tracing_enabled': {'key': 'properties.requestTracingEnabled', 'type': 'bool'},
        'request_tracing_expiration_time': {'key': 'properties.requestTracingExpirationTime', 'type': 'iso-8601'},
        'remote_debugging_enabled': {'key': 'properties.remoteDebuggingEnabled', 'type': 'bool'},
        'remote_debugging_version': {'key': 'properties.remoteDebuggingVersion', 'type': 'str'},
        'http_logging_enabled': {'key': 'properties.httpLoggingEnabled', 'type': 'bool'},
        'logs_directory_size_limit': {'key': 'properties.logsDirectorySizeLimit', 'type': 'int'},
        'detailed_error_logging_enabled': {'key': 'properties.detailedErrorLoggingEnabled', 'type': 'bool'},
        'publishing_username': {'key': 'properties.publishingUsername', 'type': 'str'},
        'app_settings': {'key': 'properties.appSettings', 'type': '[NameValuePair]'},
        'connection_strings': {'key': 'properties.connectionStrings', 'type': '[ConnStringInfo]'},
        'machine_key': {'key': 'properties.machineKey', 'type': 'SiteMachineKey'},
        'handler_mappings': {'key': 'properties.handlerMappings', 'type': '[HandlerMapping]'},
        'document_root': {'key': 'properties.documentRoot', 'type': 'str'},
        'scm_type': {'key': 'properties.scmType', 'type': 'str'},
        'use32_bit_worker_process': {'key': 'properties.use32BitWorkerProcess', 'type': 'bool'},
        'web_sockets_enabled': {'key': 'properties.webSocketsEnabled', 'type': 'bool'},
        'always_on': {'key': 'properties.alwaysOn', 'type': 'bool'},
        'java_version': {'key': 'properties.javaVersion', 'type': 'str'},
        'java_container': {'key': 'properties.javaContainer', 'type': 'str'},
        'java_container_version': {'key': 'properties.javaContainerVersion', 'type': 'str'},
        'app_command_line': {'key': 'properties.appCommandLine', 'type': 'str'},
        'managed_pipeline_mode': {'key': 'properties.managedPipelineMode', 'type': 'ManagedPipelineMode'},
        'virtual_applications': {'key': 'properties.virtualApplications', 'type': '[VirtualApplication]'},
        'load_balancing': {'key': 'properties.loadBalancing', 'type': 'SiteLoadBalancing'},
        'experiments': {'key': 'properties.experiments', 'type': 'Experiments'},
        'limits': {'key': 'properties.limits', 'type': 'SiteLimits'},
        'auto_heal_enabled': {'key': 'properties.autoHealEnabled', 'type': 'bool'},
        'auto_heal_rules': {'key': 'properties.autoHealRules', 'type': 'AutoHealRules'},
        'tracing_options': {'key': 'properties.tracingOptions', 'type': 'str'},
        'vnet_name': {'key': 'properties.vnetName', 'type': 'str'},
        'cors': {'key': 'properties.cors', 'type': 'CorsSettings'},
        'push': {'key': 'properties.push', 'type': 'PushSettings'},
        'api_definition': {'key': 'properties.apiDefinition', 'type': 'ApiDefinitionInfo'},
        'auto_swap_slot_name': {'key': 'properties.autoSwapSlotName', 'type': 'str'},
        'local_my_sql_enabled': {'key': 'properties.localMySqlEnabled', 'type': 'bool'},
        'ip_security_restrictions': {'key': 'properties.ipSecurityRestrictions', 'type': '[IpSecurityRestriction]'},
        'http20_enabled': {'key': 'properties.http20Enabled', 'type': 'bool'},
        'min_tls_version': {'key': 'properties.minTlsVersion', 'type': 'str'},
    }

    def __init__(self, kind=None, number_of_workers=None, default_documents=None, net_framework_version="v4.6", php_version=None, python_version=None, node_version=None, linux_fx_version=None, request_tracing_enabled=None, request_tracing_expiration_time=None, remote_debugging_enabled=None, remote_debugging_version=None, http_logging_enabled=None, logs_directory_size_limit=None, detailed_error_logging_enabled=None, publishing_username=None, app_settings=None, connection_strings=None, handler_mappings=None, document_root=None, scm_type=None, use32_bit_worker_process=None, web_sockets_enabled=None, always_on=None, java_version=None, java_container=None, java_container_version=None, app_command_line=None, managed_pipeline_mode=None, virtual_applications=None, load_balancing=None, experiments=None, limits=None, auto_heal_enabled=None, auto_heal_rules=None, tracing_options=None, vnet_name=None, cors=None, push=None, api_definition=None, auto_swap_slot_name=None, local_my_sql_enabled=False, ip_security_restrictions=None, http20_enabled=True, min_tls_version=None):
        super(SiteConfigResource, self).__init__(kind=kind)
        self.number_of_workers = number_of_workers
        self.default_documents = default_documents
        self.net_framework_version = net_framework_version
        self.php_version = php_version
        self.python_version = python_version
        self.node_version = node_version
        self.linux_fx_version = linux_fx_version
        self.request_tracing_enabled = request_tracing_enabled
        self.request_tracing_expiration_time = request_tracing_expiration_time
        self.remote_debugging_enabled = remote_debugging_enabled
        self.remote_debugging_version = remote_debugging_version
        self.http_logging_enabled = http_logging_enabled
        self.logs_directory_size_limit = logs_directory_size_limit
        self.detailed_error_logging_enabled = detailed_error_logging_enabled
        self.publishing_username = publishing_username
        self.app_settings = app_settings
        self.connection_strings = connection_strings
        self.machine_key = None
        self.handler_mappings = handler_mappings
        self.document_root = document_root
        self.scm_type = scm_type
        self.use32_bit_worker_process = use32_bit_worker_process
        self.web_sockets_enabled = web_sockets_enabled
        self.always_on = always_on
        self.java_version = java_version
        self.java_container = java_container
        self.java_container_version = java_container_version
        self.app_command_line = app_command_line
        self.managed_pipeline_mode = managed_pipeline_mode
        self.virtual_applications = virtual_applications
        self.load_balancing = load_balancing
        self.experiments = experiments
        self.limits = limits
        self.auto_heal_enabled = auto_heal_enabled
        self.auto_heal_rules = auto_heal_rules
        self.tracing_options = tracing_options
        self.vnet_name = vnet_name
        self.cors = cors
        self.push = push
        self.api_definition = api_definition
        self.auto_swap_slot_name = auto_swap_slot_name
        self.local_my_sql_enabled = local_my_sql_enabled
        self.ip_security_restrictions = ip_security_restrictions
        self.http20_enabled = http20_enabled
        self.min_tls_version = min_tls_version
