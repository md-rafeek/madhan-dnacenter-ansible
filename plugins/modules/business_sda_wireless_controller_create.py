#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: business_sda_wireless_controller_create
short_description: Resource module for Business Sda Wireless Controller Create
description:
- Manage operation create of the resource Business Sda Wireless Controller Create.
- Add WLC to Fabric Domain.
version_added: '4.0.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  deviceIPAddress:
    description: DeviceIPAddress query parameter. Device Management IP Address.
    type: str
  deviceName:
    description: EWLC Device Name.
    type: str
  siteNameHierarchy:
    description: Site Name Hierarchy.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference to SDK documentation of current version
- name: SDK function add_w_l_c_to_fabric_domain used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.fabric_wireless.FabricWireless.add_w_l_c_to_fabric_domain

- name: Paths used on the module Business Sda Wireless Controller Create
  description: |-
    post /dna/intent/api/v1/business/sda/wireless-controller
"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.business_sda_wireless_controller_create:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deviceName: string
    siteNameHierarchy: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "executionId": "string",
      "executionStatusUrl": "string",
      "message": "string"
    }
"""