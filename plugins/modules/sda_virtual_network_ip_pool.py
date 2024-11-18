#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sda_virtual_network_ip_pool
short_description: Resource module for Sda Virtual Network Ip Pool
description:
- This module represents an alias of the module sda_virtual_network_ip_pool_v1
version_added: '3.1.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  autoGenerateVlanName:
    description: It will auto generate vlanName, if vlanName is empty(applicable for
      L3 and INFRA_VN).
    type: bool
  ipPoolName:
    description: IpPoolName query parameter.
    type: str
    version_added: 4.0.0
  isBridgeModeVm:
    description: Bridge Mode Vm enablement flag (applicable for L3 and L2 and default
      value is False ).
    type: bool
  isCommonPool:
    description: Common Pool enablement flag(applicable for L3 and L2 and default value
      is False ).
    type: bool
  isIpDirectedBroadcast:
    description: Ip Directed Broadcast enablement flag(applicable for L3 and default
      value is False ).
    type: bool
  isL2FloodingEnabled:
    description: Layer2 flooding enablement flag(applicable for L3 , L2 and always true
      for L2 and default value is False ).
    type: bool
    version_added: 4.0.0
  isLayer2Only:
    description: Layer2 Only enablement flag and default value is False.
    type: bool
  isThisCriticalPool:
    description: Critical pool enablement flag(applicable for L3 and default value is
      False ).
    type: bool
    version_added: 4.0.0
  isWirelessPool:
    description: Wireless Pool enablement flag(applicable for L3 and L2 and default
      value is False ).
    type: bool
    version_added: 4.0.0
  poolType:
    description: Pool Type (applicable for INFRA_VN).
    type: str
    version_added: 4.0.0
  scalableGroupName:
    description: Scalable Group Name(applicable for L3).
    type: str
    version_added: 4.0.0
  siteNameHierarchy:
    description: SiteNameHierarchy query parameter.
    type: str
    version_added: 4.0.0
  trafficType:
    description: Traffic type(applicable for L3 and L2).
    type: str
    version_added: 4.0.0
  virtualNetworkName:
    description: VirtualNetworkName query parameter.
    type: str
  vlanId:
    description: Vlan Id(applicable for L3 , L2 and INFRA_VN).
    type: str
  vlanName:
    description: Vlan name represent the segment name, if empty, vlanName would be auto
      generated by API.
    type: str
    version_added: 4.0.0
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA AddIPPoolInSDAVirtualNetworkV1
  description: Complete reference of the AddIPPoolInSDAVirtualNetworkV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!add-ip-pool-in-sda-virtual-network-v-1
- name: Cisco DNA Center documentation for SDA DeleteIPPoolFromSDAVirtualNetworkV1
  description: Complete reference of the DeleteIPPoolFromSDAVirtualNetworkV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!delete-ip-pool-from-sda-virtual-network-v-1
notes:
  - SDK Method used are
    sda.Sda.add_ip_pool_in_sda_virtual_network_v1,
    sda.Sda.delete_ip_pool_from_sda_virtual_network_v1,

  - Paths used are
    post /dna/intent/api/v1/business/sda/virtualnetwork/ippool,
    delete /dna/intent/api/v1/business/sda/virtualnetwork/ippool,
  - It should be noted that this module is an alias of sda_virtual_network_ip_pool_v1

"""

EXAMPLES = r"""
- name: Delete all
  cisco.dnac.sda_virtual_network_ip_pool:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    ipPoolName: string
    siteNameHierarchy: string
    virtualNetworkName: string

- name: Create
  cisco.dnac.sda_virtual_network_ip_pool:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    autoGenerateVlanName: true
    ipPoolName: string
    isBridgeModeVm: true
    isCommonPool: true
    isIpDirectedBroadcast: true
    isL2FloodingEnabled: true
    isLayer2Only: true
    isThisCriticalPool: true
    isWirelessPool: true
    poolType: string
    scalableGroupName: string
    siteNameHierarchy: string
    trafficType: string
    virtualNetworkName: string
    vlanId: string
    vlanName: string

"""
RETURN = r"""
dnac_response:
  This alias returns the output of sda_virtual_network_ip_pool_v1.
"""
