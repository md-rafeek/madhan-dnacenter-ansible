#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: wireless_settings_dot11be_profiles_info
short_description: Information module for Wireless Settings Dot11Be Profiles Info
description:
- This module represents an alias of the module wireless_settings_dot11be_profiles_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  limit:
    description:
    - Limit query parameter.
    type: float
  offset:
    description:
    - Offset query parameter.
    type: float
  id:
    description:
    - Id path parameter. 802.11be Profile ID.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Wireless Get80211beProfileByIDV1
  description: Complete reference of the Get80211beProfileByIDV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-80-21-1be-profile-by-id-v-1
- name: Cisco DNA Center documentation for Wireless GetAll80211beProfilesV1
  description: Complete reference of the GetAll80211beProfilesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-all-80-21-1be-profiles-v-1
notes:
  - SDK Method used are
    wireless.Wireless.get80211be_profile_by_id_v1,
    wireless.Wireless.get_all80211be_profiles_v1,

  - Paths used are
    get /dna/intent/api/v1/wirelessSettings/dot11beProfiles,
    get /dna/intent/api/v1/wirelessSettings/dot11beProfiles/{id},
  - It should be noted that this module is an alias of wireless_settings_dot11be_profiles_v1_info

"""

EXAMPLES = r"""
- name: Get all Wireless Settings Dot11Be Profiles Info
  cisco.dnac.wireless_settings_dot11be_profiles_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    limit: 0
    offset: 0
  register: result

- name: Get Wireless Settings Dot11Be Profiles Info by id
  cisco.dnac.wireless_settings_dot11be_profiles_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
  register: result

"""
RETURN = r"""
dnac_response:
  description:
    - This alias returns the output of wireless_settings_dot11be_profiles_v1_info.
"""
