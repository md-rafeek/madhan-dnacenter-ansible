#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_device_role_v1_info
short_description: Information module for Sda Device Role V1
description:
- Get all Sda Device Role V1.
- Get device role in SDA Fabric.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceManagementIpAddress:
    description:
    - DeviceManagementIpAddress query parameter. Device Management IP Address.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA GetDeviceRoleInSDAFabricV1
  description: Complete reference of the GetDeviceRoleInSDAFabricV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-device-role-in-sda-fabric-v-1
notes:
  - SDK Method used are
    sda.Sda.get_device_role_in_sda_fabric_v1,

  - Paths used are
    get /dna/intent/api/v1/business/sda/device/role,

"""

EXAMPLES = r"""
- name: Get all Sda Device Role V1
  cisco.dnac.sda_device_role_v1_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    deviceManagementIpAddress: string
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "roles": [
        "string"
      ],
      "status": "string",
      "description": "string"
    }
"""
