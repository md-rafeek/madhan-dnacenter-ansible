#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: security_advisories_ids_per_device_info
short_description: Information module for Security Advisories Ids Per Device Info
description:
- This module represents an alias of the module security_advisories_ids_per_device_v1_info
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
- name: Cisco DNA Center documentation for Security Advisories GetAdvisoryDeviceDetailV1
  description: Complete reference of the GetAdvisoryDeviceDetailV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-advisory-device-detail-v-1
notes:
  - SDK Method used are
    security_advisories.SecurityAdvisories.get_advisory_device_detail_v1,

  - Paths used are
    get /dna/intent/api/v1/security-advisory/device/{deviceId},
  - It should be noted that this module is an alias of security_advisories_ids_per_device_v1_info

"""

EXAMPLES = r"""
- name: Get Security Advisories Ids Per Device Info by id
  cisco.dnac.security_advisories_ids_per_device_info:
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
  This alias returns the output of security_advisories_ids_per_device_v1_info.
"""
