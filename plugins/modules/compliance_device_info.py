#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_device_info
short_description: Information module for Compliance Device
description:
- Get all Compliance Device.
- Get Compliance Device by id.
- Return compliance status of device(s).
- Return compliance status of a device.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  complianceStatus:
    description:
    - >
      ComplianceStatus query parameter. Compliance status can be have value among
      'COMPLIANT','NON_COMPLIANT','IN_PROGRESS', 'ERROR'.
    type: str
  deviceUuid:
    description:
    - DeviceUuid query parameter. Comma separated deviceUuids.
    type: str
  offset:
    description:
    - Offset query parameter. Offset/starting row.
    type: int
  limit:
    description:
    - Limit query parameter. Number of records to be retrieved.
    type: int
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference to SDK documentation of current version
- name: SDK function get_compliance_status used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.compliance.Compliance.get_compliance_status

- name: SDK function device_compliance_status used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.compliance.Compliance.device_compliance_status

- name: Paths used on the module Compliance Device
  description: |-
    get /dna/intent/api/v1/compliance,
    get /dna/intent/api/v1/compliance/{deviceUuid}
"""

EXAMPLES = r"""
- name: Get all Compliance Device
  cisco.dnac.compliance_device_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    complianceStatus: string
    deviceUuid: string
    offset: 0
    limit: 0
  register: result

- name: Get Compliance Device by id
  cisco.dnac.compliance_device_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    deviceUuid: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "version": "string",
      "response": {
        "deviceUuid": "string",
        "complianceStatus": "string",
        "message": "string",
        "scheduleTime": 0,
        "lastUpdateTime": 0
      }
    }
"""