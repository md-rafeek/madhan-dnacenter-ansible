#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: security_threats_summary
short_description: Resource module for Security Threats Summary
description:
- This module represents an alias of the module security_threats_summary_v1
version_added: '6.16.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  endTime:
    description: End Time.
    type: int
  siteId:
    description: Site Id.
    elements: str
    type: list
  startTime:
    description: Start Time.
    type: int
  threatLevel:
    description: Threat Level.
    elements: str
    type: list
  threatType:
    description: Threat Type.
    elements: str
    type: list
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
notes:
  - SDK Method used are
    devices.Devices.threat_summary_v1,

  - Paths used are
    post /dna/intent/api/v1/security/threats/summary,
  - It should be noted that this module is an alias of security_threats_summary_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.security_threats_summary:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    endTime: 0
    siteId:
    - string
    startTime: 0
    threatLevel:
    - string
    threatType:
    - string

"""
RETURN = r"""
dnac_response:
  This alias returns the output of security_threats_summary_v1.
"""
