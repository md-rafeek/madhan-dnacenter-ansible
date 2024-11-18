#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: compliance_device_v1_info
short_description: Information module for Compliance Device V1
description:
- Get all Compliance Device V1.
- Get Compliance Device V1 by id.
- Return compliance status of a device.
- Return compliance status of devices.
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
      ComplianceStatus query parameter. Specify "Compliance status(es)" separated by commas. The Compliance status
      can be 'COMPLIANT', 'NON_COMPLIANT', 'IN_PROGRESS', 'NOT_AVAILABLE', 'NOT_APPLICABLE', 'ERROR'.
    type: str
  deviceUuid:
    description:
    - DeviceUuid query parameter. Comma separated 'Device Ids'.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Compliance DeviceComplianceStatusV1
  description: Complete reference of the DeviceComplianceStatusV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!device-compliance-status-v-1
- name: Cisco DNA Center documentation for Compliance GetComplianceStatusV1
  description: Complete reference of the GetComplianceStatusV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-compliance-status-v-1
notes:
  - SDK Method used are
    compliance.Compliance.device_compliance_status_v1,
    compliance.Compliance.get_compliance_status_v1,

  - Paths used are
    get /dna/intent/api/v1/compliance,
    get /dna/intent/api/v1/compliance/{deviceUuid},

"""

EXAMPLES = r"""
- name: Get all Compliance Device V1
  cisco.dnac.compliance_device_v1_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    complianceStatus: string
    deviceUuid: string
  register: result

- name: Get Compliance Device V1 by id
  cisco.dnac.compliance_device_v1_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
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
      "response": {
        "deviceUuid": "string",
        "complianceStatus": "string",
        "lastUpdateTime": 0,
        "scheduleTime": "string"
      },
      "version": "string"
    }
"""
