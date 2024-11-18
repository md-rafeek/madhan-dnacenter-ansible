#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: network_device_chassis_details_info
short_description: Information module for Network Device Chassis Details Info
description:
- This module represents an alias of the module network_device_chassis_details_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  deviceId:
    description:
    - DeviceId path parameter. Device ID.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices GetChassisDetailsForDeviceV1
  description: Complete reference of the GetChassisDetailsForDeviceV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-chassis-details-for-device-v-1
notes:
  - SDK Method used are
    devices.Devices.get_chassis_details_for_device_v1,

  - Paths used are
    get /dna/intent/api/v1/network-device/{deviceId}/chassis,
  - It should be noted that this module is an alias of network_device_chassis_details_v1_info

"""

EXAMPLES = r"""
- name: Get all Network Device Chassis Details Info
  cisco.dnac.network_device_chassis_details_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    deviceId: string
  register: result

"""
RETURN = r"""
dnac_response:
  This alias returns the output of network_device_chassis_details_v1_info.
"""
