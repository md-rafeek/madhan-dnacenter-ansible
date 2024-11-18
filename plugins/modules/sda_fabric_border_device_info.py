#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sda_fabric_border_device_info
short_description: Information module for Sda Fabric Border Device Info
description:
- This module represents an alias of the module sda_fabric_border_device_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceManagementIpAddress:
    version_added: "4.0.0"
    description:
    - DeviceManagementIpAddress query parameter.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA GetBorderDeviceDetailFromSDAFabricV1
  description: Complete reference of the GetBorderDeviceDetailFromSDAFabricV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-border-device-detail-from-sda-fabric-v-1
notes:
  - SDK Method used are
    sda.Sda.gets_border_device_detail,

  - Paths used are
    get /dna/intent/api/v1/business/sda/border-device,
  - It should be noted that this module is an alias of sda_fabric_border_device_v1_info

"""

EXAMPLES = r"""
- name: Get all Sda Fabric Border Device Info
  cisco.dnac.sda_fabric_border_device_info:
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
  This alias returns the output of sda_fabric_border_device_v1_info.
"""
