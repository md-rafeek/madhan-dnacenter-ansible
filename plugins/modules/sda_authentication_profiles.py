#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sda_authentication_profiles
short_description: Resource module for Sda Authentication Profiles
description:
- This module represents an alias of the module sda_authentication_profiles_v1
version_added: '6.14.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  payload:
    description: Sda Authentication Profiles's payload.
    elements: dict
    suboptions:
      authenticationOrder:
        description: First authentication method.
        type: str
      authenticationProfileName:
        description: The default host authentication template (updating this field is
          not allowed).
        type: str
      dot1xToMabFallbackTimeout:
        description: 802.1x Timeout.
        type: int
      fabricId:
        description: ID of the fabric this authentication profile is assigned to (updating
          this field is not allowed).
        type: str
      id:
        description: ID of the authentication profile (updating this field is not allowed).
        type: str
      isBpduGuardEnabled:
        description: Enable/disable BPDU Guard. Only applicable when authenticationProfileName
          is set to "Closed Authentication" (defaults to true).
        type: bool
      numberOfHosts:
        description: Number of Hosts.
        type: str
      wakeOnLan:
        description: Wake on LAN.
        type: bool
    type: list
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA UpdateAuthenticationProfileV1
  description: Complete reference of the UpdateAuthenticationProfileV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-authentication-profile-v-1
notes:
  - SDK Method used are
    sda.Sda.update_authentication_profile_v1,

  - Paths used are
    put /dna/intent/api/v1/sda/authenticationProfiles,
  - It should be noted that this module is an alias of sda_authentication_profiles_v1

"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.sda_authentication_profiles:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    payload:
    - authenticationOrder: string
      authenticationProfileName: string
      dot1xToMabFallbackTimeout: 0
      fabricId: string
      id: string
      isBpduGuardEnabled: true
      numberOfHosts: string
      wakeOnLan: true

"""
RETURN = r"""
dnac_response:
  This alias returns the output of sda_authentication_profiles_v1.
"""
