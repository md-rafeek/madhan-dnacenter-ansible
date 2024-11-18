#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: device_credential_info
short_description: Information module for Device Credential Info
description:
- This module represents an alias of the module device_credential_v1_info
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
    - SiteId query parameter. Site id to retrieve the credential details associated with the site.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Network Settings GetDeviceCredentialDetailsV1
  description: Complete reference of the GetDeviceCredentialDetailsV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-device-credential-details-v-1
notes:
  - SDK Method used are
    network_settings.NetworkSettings.get_device_credential_details_v1,

  - Paths used are
    get /dna/intent/api/v1/device-credential,
  - It should be noted that this module is an alias of device_credential_v1_info

"""

EXAMPLES = r"""
- name: Get all Device Credential Info
  cisco.dnac.device_credential_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    siteId: string
  register: result

"""
RETURN = r"""
dnac_response:
  This alias returns the output of device_credential_v1_info.
"""
