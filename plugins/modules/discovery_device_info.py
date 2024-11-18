#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: discovery_device_info
short_description: Information module for Discovery Device Info
description:
- This module represents an alias of the module discovery_device_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
    - Id path parameter. Discovery ID.
    type: str
  taskId:
    description:
    - TaskId query parameter.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Discovery GetDiscoveredNetworkDevicesByDiscoveryIdV1
  description: Complete reference of the GetDiscoveredNetworkDevicesByDiscoveryIdV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-discovered-network-devices-by-discovery-id-v-1
notes:
  - SDK Method used are
    discovery.Discovery.get_discovered_network_devices_by_discovery_id_v1,

  - Paths used are
    get /dna/intent/api/v1/discovery/{id}/network-device,
  - It should be noted that this module is an alias of discovery_device_v1_info

"""

EXAMPLES = r"""
- name: Get all Discovery Device Info
  cisco.dnac.discovery_device_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    taskId: string
    id: string
  register: result

"""
RETURN = r"""
dnac_response:
  This alias returns the output of discovery_device_v1_info.
"""
