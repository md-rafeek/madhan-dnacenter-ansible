#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: snmp_properties
short_description: Resource module for Snmp Properties
description:
- Manage operation create of the resource Snmp Properties.
- Adds SNMP properties.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Snmp Properties's payload.
    suboptions:
      id:
        description: Snmp Properties's id.
        type: str
      instanceTenantId:
        description: Snmp Properties's instanceTenantId.
        type: str
      instanceUuid:
        description: Snmp Properties's instanceUuid.
        type: str
      intValue:
        description: Snmp Properties's intValue.
        type: int
      systemPropertyName:
        description: Snmp Properties's systemPropertyName.
        type: str
    type: list
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference to SDK documentation of current version
- name: SDK function create_update_snmp_properties used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.discovery.Discovery.create_update_snmp_properties

- name: Paths used on the module Snmp Properties
  description: |-
    post /dna/intent/api/v1/snmp-property
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.snmp_properties:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "taskId": "string",
        "url": "string"
      },
      "version": "string"
    }
"""