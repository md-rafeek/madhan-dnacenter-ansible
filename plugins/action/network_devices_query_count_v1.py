#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
from ansible.plugins.action import ActionBase
try:
    from ansible_collections.ansible.utils.plugins.module_utils.common.argspec_validate import (
        AnsibleArgSpecValidator,
    )
except ImportError:
    ANSIBLE_UTILS_IS_INSTALLED = False
else:
    ANSIBLE_UTILS_IS_INSTALLED = True
from ansible.errors import AnsibleActionFail
from ansible_collections.cisco.dnac.plugins.plugin_utils.dnac import (
    DNACSDK,
    dnac_argument_spec,
)

# Get common arguements specification
argument_spec = dnac_argument_spec()
# Add arguments specific for this module
argument_spec.update(dict(
    startTime=dict(type="int"),
    endTime=dict(type="int"),
    views=dict(type="list"),
    attributes=dict(type="list"),
    filters=dict(type="list"),
    aggregateAttributes=dict(type="list"),
    page=dict(type="dict"),
))

required_if = []
required_one_of = []
mutually_exclusive = []
required_together = []


class ActionModule(ActionBase):
    def __init__(self, *args, **kwargs):
        if not ANSIBLE_UTILS_IS_INSTALLED:
            raise AnsibleActionFail("ansible.utils is not installed. Execute 'ansible-galaxy collection install ansible.utils'")
        super(ActionModule, self).__init__(*args, **kwargs)
        self._supports_async = False
        self._supports_check_mode = False
        self._result = None

    # Checks the supplied parameters against the argument spec for this module
    def _check_argspec(self):
        aav = AnsibleArgSpecValidator(
            data=self._task.args,
            schema=dict(argument_spec=argument_spec),
            schema_format="argspec",
            schema_conditionals=dict(
                required_if=required_if,
                required_one_of=required_one_of,
                mutually_exclusive=mutually_exclusive,
                required_together=required_together,
            ),
            name=self._task.action,
        )
        valid, errors, self._task.args = aav.validate()
        if not valid:
            raise AnsibleActionFail(errors)

    def get_object(self, params):
        new_object = dict(
            startTime=params.get("startTime"),
            endTime=params.get("endTime"),
            views=params.get("views"),
            attributes=params.get("attributes"),
            filters=params.get("filters"),
            aggregateAttributes=params.get("aggregateAttributes"),
            page=params.get("page"),
        )
        return new_object

    def run(self, tmp=None, task_vars=None):
        self._task.diff = False
        self._result = super(ActionModule, self).run(tmp, task_vars)
        self._result["changed"] = False
        self._check_argspec()

        dnac = DNACSDK(params=self._task.args)

        response = dnac.exec(
            family="devices",
            # No function
            # Metadata: {'type': 'c', 'look_by': '', 'urls': ['/data/api/v1/networkDevices/query/count'], 'tag': 'Devices', 'version_added': '6.15.0', 'get_all': 'gets_the_total_number_network_devices_based_on_the_provided_complex_filters_and_aggregation_functions_v1', 'operation_id_list': ['get:GetsTheTotalNumberNetworkDevicesBasedOnTheProvidedComplexFiltersAndAggregationFunctionsV1'], 'description': 'get:Gets the total number Network Devices based on the provided complex filters and aggregation functions. For detailed information about the usage of the API, please refer to the Open API specification document - https://github.com/cisco-en-programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-AssuranceNetworkDevices-1.0.2-resolved.yaml.\n', 'method_url': 'get:post /data/api/v1/networkDevices/query/count,\n'}
            params=self.get_object(self._task.args),
        )
        self._result.update(dict(dnac_response=response))
        self._result.update(dnac.exit_json())
        return self._result
