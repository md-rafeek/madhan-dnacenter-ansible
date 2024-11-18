#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: floors_settings
short_description: Resource module for Floors Settings
description:
- This module represents an alias of the module floors_settings_v2
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  unitsOfMeasure:
    description: Floor units of measure.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Site Design UpdatesFloorSettingsV2
  description: Complete reference of the UpdatesFloorSettingsV2 API.
  link: https://developer.cisco.com/docs/dna-center/#!updates-floor-settings-v-2
notes:
  - SDK Method used are
    site_design.SiteDesign.updates_floor_settings_v2,

  - Paths used are
    put /dna/intent/api/v2/floors/settings,
  - It should be noted that this module is an alias of floors_settings_v2

"""

EXAMPLES = r"""
- name: Update all
  cisco.dnac.floors_settings:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    state: present
    unitsOfMeasure: string

"""
RETURN = r"""
dnac_response:
  description:
    - This alias returns the output of floors_settings_v2.
"""
