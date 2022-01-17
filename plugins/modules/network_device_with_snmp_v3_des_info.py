#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: network_device_with_snmp_v3_des_info
short_description: Information module for Network Device With Snmp V3 Des
description:
- Get all Network Device With Snmp V3 Des.
- Returns devices added to DNAC with snmp v3 DES, where siteId is mandatory & accepts offset, limit, sortby, order which are optional.
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  siteId:
    description:
    - SiteId path parameter.
    type: str
  offset:
    description:
    - Offset query parameter. Row Number. Default value is 1.
    type: str
  limit:
    description:
    - Limit query parameter. Default value is 500.
    type: str
  sortBy:
    description:
    - SortBy query parameter. Sort By.
    type: str
  order:
    description:
    - Order query parameter.
    type: str
requirements:
- dnacentersdk >= 2.4.0
- python >= 3.5
seealso:
# Reference to SDK documentation of current version
- name: SDK function get_devices_with_snmpv3_des used
  link: https://dnacentersdk.rtfd.io/en/latest/api/api.html#dnacentersdk.api.v2_2_3_3.devices.Devices.get_devices_with_snmpv3_des

- name: Paths used on the module Network Device With Snmp V3 Des
  description: |-
    get /dna/intent/api/v1/network-device/insight/{siteId}/insecure-connection
"""

EXAMPLES = r"""
- name: Get all Network Device With Snmp V3 Des
  cisco.dnac.network_device_with_snmp_v3_des_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers:
      custom: value
    offset: string
    limit: string
    sortBy: string
    order: string
    siteId: string
  register: result

"""

RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": [
        {
          "id": "string",
          "managementIpAddress": "string",
          "hostname": "string",
          "type": "string",
          "family": "string",
          "lastUpdated": "string",
          "upTime": "string",
          "reachabilityStatus": "string"
        }
      ],
      "version": "string"
    }
"""