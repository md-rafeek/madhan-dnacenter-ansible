#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: custom_issue_definitions_info
short_description: Information module for Custom Issue Definitions Info
description:
- This module represents an alias of the module custom_issue_definitions_v1_info
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  id:
    description:
    - >
      Id query parameter. The custom issue definition identifier and unique identifier across the profile.Examples
      id=6bef213c-19ca-4170-8375-b694e251101c (single entity uuid requested)
      id=6bef213c-19ca-4170-8375-b694e251101c&id=19ca-4170-8375-b694e251101c-6bef213c (multiple Id request in the
      query param).
    type: str
  profileId:
    description:
    - >
      ProfileId query parameter. The profile identifier to fetch the profile associated custom issue definitions.
      The default is global. For the custom profile, it is profile UUID. Example
      3fa85f64-5717-4562-b3fc-2c963f66afa6.
    type: str
  name:
    description:
    - Name query parameter. The list of UDI issue names.
    type: str
  priority:
    description:
    - >
      Priority query parameter. The Issue priority value, possible values are P1, P2, P3, P4. P1 A critical issue
      that needs immediate attention and can have a wide impact on network operations. P2 A major issue that can
      potentially impact multiple devices or clients. P3 A minor issue that has a localized or minimal impact. P4
      A warning issue that may not be an immediate problem but addressing it can optimize the network performance.
    type: str
  isEnabled:
    description:
    - IsEnabled query parameter. The enable status of the custom issue definition, either true or false.
    type: bool
  severity:
    description:
    - >
      Severity query parameter. The syslog severity level. 0 Emergency 1 Alert, 2 Critical. 3 Error, 4 Warning, 5
      Notice, 6 Info. Examples severity=1&severity=2 (multi value support with & separator).
    type: float
  facility:
    description:
    - Facility query parameter. The syslog facility name.
    type: str
  mnemonic:
    description:
    - Mnemonic query parameter. The syslog mnemonic name.
    type: str
  limit:
    description:
    - Limit query parameter. The maximum number of records to return.
    type: float
  offset:
    description:
    - >
      Offset query parameter. Specifies the starting point within all records returned by the API. It's one based
      offset. The starting value is 1.
    type: float
  sortBy:
    description:
    - SortBy query parameter. A field within the response to sort by.
    type: str
  order:
    description:
    - Order query parameter. The sort order of the field ascending or descending.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Issues GetAllTheCustomIssueDefinitionsBasedOnTheGivenFiltersV1
  description: Complete reference of the GetAllTheCustomIssueDefinitionsBasedOnTheGivenFiltersV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-all-the-custom-issue-definitions-based-on-the-given-filters-v-1
notes:
  - SDK Method used are
    issues.Issues.get_all_the_custom_issue_definitions_based_on_the_given_filters_v1,

  - Paths used are
    get /dna/intent/api/v1/customIssueDefinitions,
  - It should be noted that this module is an alias of custom_issue_definitions_v1_info

"""

EXAMPLES = r"""
- name: Get all Custom Issue Definitions Info
  cisco.dnac.custom_issue_definitions_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    id: string
    profileId: string
    name: string
    priority: string
    isEnabled: True
    severity: 0
    facility: string
    mnemonic: string
    limit: 0
    offset: 0
    sortBy: string
    order: string
  register: result

"""
RETURN = r"""
dnac_response:
  description:
    - This alias returns the output of custom_issue_definitions_v1_info.
"""
