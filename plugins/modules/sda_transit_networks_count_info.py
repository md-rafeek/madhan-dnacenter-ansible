#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: sda_transit_networks_count_info
short_description: Information module for Sda Transit Networks Count Info
description:
- This module represents an alias of the module sda_transit_networks_count_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  type:
    description:
    - >
      Type query parameter. Type of the transit network. Allowed values are IP_BASED_TRANSIT,
      SDA_LISP_PUB_SUB_TRANSIT, SDA_LISP_BGP_TRANSIT.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for SDA GetTransitNetworksCountV1
  description: Complete reference of the GetTransitNetworksCountV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-transit-networks-count-v-1
notes:
  - SDK Method used are
    sda.Sda.get_transit_networks_count_v1,

  - Paths used are
    get /dna/intent/api/v1/sda/transitNetworks/count,
  - It should be noted that this module is an alias of sda_transit_networks_count_v1_info

"""

EXAMPLES = r"""
- name: Get all Sda Transit Networks Count Info
  cisco.dnac.sda_transit_networks_count_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    type: string
  register: result

"""
RETURN = r"""
dnac_response:
  This alias returns the output of sda_transit_networks_count_v1_info.
"""
