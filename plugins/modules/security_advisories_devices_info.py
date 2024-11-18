#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: security_advisories_devices_info
short_description: Information module for Security Advisories Devices Info
description:
- This module represents an alias of the module security_advisories_devices_v1_info
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  advisoryId:
    description:
    - AdvisoryId path parameter. Advisory ID.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Security Advisories GetDevicesPerAdvisoryV1
  description: Complete reference of the GetDevicesPerAdvisoryV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-devices-per-advisory-v-1
notes:
  - SDK Method used are
    security_advisories.SecurityAdvisories.get_devices_per_advisory_v1,

  - Paths used are
    get /dna/intent/api/v1/security-advisory/advisory/{advisoryId}/device,
  - It should be noted that this module is an alias of security_advisories_devices_v1_info

"""

EXAMPLES = r"""
- name: Get all Security Advisories Devices Info
  cisco.dnac.security_advisories_devices_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    advisoryId: string
  register: result

"""
RETURN = r"""
dnac_response:
  description:
    - This alias returns the output of security_advisories_devices_v1_info.
"""
