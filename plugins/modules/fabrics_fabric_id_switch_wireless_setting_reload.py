#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)
DOCUMENTATION = r"""
---
module: fabrics_fabric_id_switch_wireless_setting_reload
short_description: Resource module for Fabrics Fabric Id Switch Wireless Setting Reload
description:
  - This module represents an alias of the module fabrics_fabric_id_switch_wireless_setting_reload_v1
version_added: '6.17.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  deviceId:
    description: Network Device ID.
    type: str
  fabricId:
    description: FabricId path parameter. The 'fabricId' represents the Fabric ID
      of a particular Fabric Site. The 'fabricId' can be obtained using the api /dna/intent/api/v1/sda/fabricSites.
      Example e290f1ee-6c54-4b01-90e6-d701748f0851.
    type: str
requirements:
  - dnacentersdk >= 2.4.9
  - python >= 3.5
seealso:
  - name: Cisco DNA Center documentation for Fabric Wireless ReloadSwitchForWirelessControllerCleanupV1
    description: Complete reference of the ReloadSwitchForWirelessControllerCleanupV1
      API.
    link:
      https://developer.cisco.com/docs/dna-center/#!reload-switch-for-wireless-controller-cleanup
notes:
  - SDK Method used are fabric_wireless.FabricWireless.reload_switch_for_wireless_controller_cleanup_v1,
  - Paths used are post /dna/intent/api/v1/sda/fabrics/{fabricId}/switchWirelessSetting/reload,
  - It should be noted that this module is an alias of fabrics_fabric_id_switch_wireless_setting_reload_v1
"""
EXAMPLES = r"""
- name: Create
  cisco.dnac.fabrics_fabric_id_switch_wireless_setting_reload:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    deviceId: string
    fabricId: string
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
