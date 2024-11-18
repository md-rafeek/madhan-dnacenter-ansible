#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: wireless_controllers_wireless_mobility_groups_info
short_description: Information module for Wireless Controllers Wireless Mobility Groups Info
description:
- This module represents an alias of the module wireless_controllers_wireless_mobility_groups_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  networkDeviceId:
    description:
    - >
      NetworkDeviceId query parameter. Employ this query parameter to obtain the details of the Mobility Group
      corresponding to the provided networkDeviceId. Obtain the network device ID value by using the API GET call
      /dna/intent/api/v1/network-device/ip-address/${ipAddress}.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless GetAllMobilityGroupsV1
  description: Complete reference of the GetAllMobilityGroupsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-all-mobility-groups-v-1
notes:
  - SDK Method used are
    wireless.Wireless.get_all_mobility_groups_v1,

  - Paths used are
    get /dna/intent/api/v1/wirelessControllers/wirelessMobilityGroups,
  - It should be noted that this module is an alias of wireless_controllers_wireless_mobility_groups_v1_info

"""

EXAMPLES = r"""
- name: Get all Wireless Controllers Wireless Mobility Groups Info
  cisco.dnac.wireless_controllers_wireless_mobility_groups_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    networkDeviceId: string
  register: result

"""
RETURN = r"""
dnac_response:
  This alias returns the output of wireless_controllers_wireless_mobility_groups_v1_info.
"""
