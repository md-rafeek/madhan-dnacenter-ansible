#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: sda_provision_device
short_description: Resource module for Sda Provision Device
description:
- Manage operations create, update and delete of the resource Sda Provision Device.
- Delete provisioned Wired Device.
- Re-Provision Wired Device.
- Provision Wired Device.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  deviceManagementIpAddress:
    description: DeviceManagementIpAddress query parameter. Valid IP address of the
      device currently provisioned in a fabric site.
    type: str
  siteNameHierarchy:
    description: Site Name Hierarchy for device location(only building / floor level).
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference to SDK documentation of current version
- name: SDK function re_provision_wired_device used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.sda.Sda.re_provision_wired_device

- name: SDK function provision_wired_device used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.sda.Sda.provision_wired_device

- name: Paths used on the module Sda Provision Device
  description: |-
    delete /dna/intent/api/v1/business/sda/provision-device,
    put /dna/intent/api/v1/business/sda/provision-device,
    post /dna/intent/api/v1/business/sda/provision-device
"""

EXAMPLES = r"""
- name: Delete all
  cisco.dnac.sda_provision_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    deviceManagementIpAddress: string

- name: Update all
  cisco.dnac.sda_provision_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    deviceManagementIpAddress: string
    siteNameHierarchy: string

- name: Create
  cisco.dnac.sda_provision_device:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    deviceManagementIpAddress: string
    siteNameHierarchy: string

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "status": "string",
      "description": "string",
      "taskId": "string",
      "taskStatusUrl": "string",
      "executionStatusUrl": "string",
      "executionId": "string"
    }
"""