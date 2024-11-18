#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: clients_trend_analytics_id
short_description: Resource module for Clients Trend Analytics Id
description:
- This module represents an alias of the module clients_trend_analytics_id_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  aggregateAttributes:
    description: Clients Trend Analytics Id's aggregateAttributes.
    elements: dict
    suboptions:
      function:
        description: Function.
        type: str
      name:
        description: Name.
        type: str
    type: list
  attributes:
    description: Attributes.
    elements: str
    type: list
  endTime:
    description: End Time.
    type: int
  filters:
    description: Clients Trend Analytics Id's filters.
    elements: dict
    suboptions:
      key:
        description: Key.
        type: str
      operator:
        description: Operator.
        type: str
      value:
        description: Value.
        type: int
    type: list
  groupBy:
    description: Group By.
    elements: str
    type: list
  headers:
    description: Additional headers.
    type: dict
  id:
    description: Id path parameter. Id is the client mac address. It can be specified
      in one of the notational conventions 01 23 45 67 89 AB or 01-23-45-67-89-AB or
      0123.4567.89AB and is case insensitive.
    type: str
  page:
    description: Clients Trend Analytics Id's page.
    suboptions:
      cursor:
        description: Cursor.
        type: str
      limit:
        description: Limit.
        type: int
      timeSortOrder:
        description: Time Sort Order.
        type: str
    type: dict
  startTime:
    description: Start Time.
    type: int
  trendInterval:
    description: Trend Interval.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Clients RetrievesSpecificClientInformationOverASpecifiedPeriodOfTimeV1
  description: Complete reference of the RetrievesSpecificClientInformationOverASpecifiedPeriodOfTimeV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!retrieves-specific-client-information-over-a-specified-period-of-time-v-1
notes:
  - SDK Method used are
    clients.Clients.retrieves_specific_client_information_over_a_specified_period_of_time_v1,

  - Paths used are
    post /dna/data/api/v1/clients/{id}/trendAnalytics,
  - It should be noted that this module is an alias of clients_trend_analytics_id_v1

"""

EXAMPLES = r"""
- name: Create
  cisco.dnac.clients_trend_analytics_id:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    aggregateAttributes:
    - function: string
      name: string
    attributes:
    - string
    endTime: 0
    filters:
    - key: string
      operator: string
      value: 0
    groupBy:
    - string
    headers: '{{my_headers | from_json}}'
    id: string
    page:
      cursor: string
      limit: 0
      timeSortOrder: string
    startTime: 0
    trendInterval: string

"""
RETURN = r"""
dnac_response:
  This alias returns the output of clients_trend_analytics_id_v1.
"""
