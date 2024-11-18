#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sda_fabric_devices_layer2_handoffs
short_description: Resource module for Sda Fabric Devices Layer2 Handoffs
description:
- This module represents an alias of the module sda_fabric_devices_layer2_handoffs_v1
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  fabricId:
    description: FabricId query parameter. ID of the fabric this device belongs to.
    type: str
  id:
    description: Id path parameter. ID of the layer 2 handoff of a fabric device.
    type: str
  networkDeviceId:
    description: NetworkDeviceId query parameter. Network device ID of the fabric device.
    type: str
  payload:
    description: Sda Fabric Devices Layer2 Handoffs's payload.
    elements: dict
    suboptions:
      externalVlanId:
        description: External VLAN number into which the fabric must be extended. Allowed
          VLAN range is 2-4094 except for reserved vlans (1, 1002-1005, 2046, 4094).
        type: int
      fabricId:
        description: ID of the fabric this device is assigned to.
        type: str
      interfaceName:
        description: Interface name of the layer 2 handoff. E.g., GigabitEthernet1/0/4.
        type: str
      internalVlanId:
        description: VLAN number associated with this fabric. Allowed VLAN range is
          2-4094 except for reserved vlans (1, 1002-1005, 2046, 4094).
        type: int
      networkDeviceId:
        description: Network device ID of the fabric device.
        type: str
    type: list
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA AddFabricDevicesLayer2HandoffsV1
  description: Complete reference of the AddFabricDevicesLayer2HandoffsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!add-fabric-devices-layer-2-handoffs-v-1
- name: Cisco DNA Center documentation for SDA DeleteFabricDeviceLayer2HandoffByIdV1
  description: Complete reference of the DeleteFabricDeviceLayer2HandoffByIdV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-fabric-device-layer-2-handoff-by-id-v-1
- name: Cisco DNA Center documentation for SDA DeleteFabricDeviceLayer2HandoffsV1
  description: Complete reference of the DeleteFabricDeviceLayer2HandoffsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-fabric-device-layer-2-handoffs-v-1
notes:
  - SDK Method used are
    sda.Sda.add_fabric_devices_layer2_handoffs_v1,
    sda.Sda.delete_fabric_device_layer2_handoff_by_id_v1,

  - Paths used are
    post /dna/intent/api/v1/sda/fabricDevices/layer2Handoffs,
    delete /dna/intent/api/v1/sda/fabricDevices/layer2Handoffs,
    delete /dna/intent/api/v1/sda/fabricDevices/layer2Handoffs/{id},
  - It should be noted that this module is an alias of sda_fabric_devices_layer2_handoffs_v1

"""

EXAMPLES = r"""
- name: Delete all
  cisco.dnac.sda_fabric_devices_layer2_handoffs:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    fabricId: string
    networkDeviceId: string

- name: Create
  cisco.dnac.sda_fabric_devices_layer2_handoffs:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    payload:
    - externalVlanId: 0
      fabricId: string
      interfaceName: string
      internalVlanId: 0
      networkDeviceId: string

- name: Delete by id
  cisco.dnac.sda_fabric_devices_layer2_handoffs:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: absent
    id: string

"""
RETURN = r"""
dnac_response:
  This alias returns the output of sda_fabric_devices_layer2_handoffs_v1.
"""
