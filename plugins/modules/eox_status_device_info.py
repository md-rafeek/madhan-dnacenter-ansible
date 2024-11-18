#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: eox_status_device_info
short_description: Information module for Eox Status Device Info
description:
- This module represents an alias of the module eox_status_device_v1_info
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
    - DeviceId path parameter. Device instance UUID.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for EoX GetEoXDetailsPerDeviceV1
  description: Complete reference of the GetEoXDetailsPerDeviceV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-eo-x-details-per-device-v-1
- name: Cisco DNA Center documentation for EoX GetEoXStatusForAllDevicesV1
  description: Complete reference of the GetEoXStatusForAllDevicesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-eo-x-status-for-all-devices-v-1
notes:
  - SDK Method used are
    eox.Eox.get_eox_details_per_device_v1,
    eox.Eox.get_eox_status_for_all_devices_v1,

  - Paths used are
    get /dna/intent/api/v1/eox-status/device,
    get /dna/intent/api/v1/eox-status/device/{deviceId},
  - It should be noted that this module is an alias of eox_status_device_v1_info

"""

EXAMPLES = r"""
- name: Get all Eox Status Device Info
  cisco.dnac.eox_status_device_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result

- name: Get Eox Status Device Info by id
  cisco.dnac.eox_status_device_info:
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
  This alias returns the output of eox_status_device_v1_info.
"""
