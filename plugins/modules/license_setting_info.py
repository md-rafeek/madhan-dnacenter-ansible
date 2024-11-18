#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: license_setting_info
short_description: Information module for License Setting Info
description:
- This module represents an alias of the module license_setting_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Licenses RetrieveLicenseSettingV1
  description: Complete reference of the RetrieveLicenseSettingV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieve-license-setting-v-1
notes:
  - SDK Method used are
    licenses.Licenses.retrieve_license_setting_v1,

  - Paths used are
    get /dna/intent/api/v1/licenseSetting,
  - It should be noted that this module is an alias of license_setting_v1_info

"""

EXAMPLES = r"""
- name: Get all License Setting Info
  cisco.dnac.license_setting_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
  register: result

"""
RETURN = r"""
dnac_response:
  description:
    - This alias returns the output of license_setting_v1_info.
"""
