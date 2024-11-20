#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or
# https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = r"""
---
module: interfaces_v1_info
short_description: Information module for Interfaces V1
description:
- Get all Interfaces V1.
- Get Interfaces V1 by id.
- >
   Retrieves the list of the interfaces from all network devices based on the provided query parameters. The latest
   interfaces data in the specified start and end time range will be returned. When there is no start and end time
   specified returns the latest available data.
- >
   Returns the interface data for the given interface instance Uuid along with the statistics data. The latest
   interface data in the specified start and end time range will be returned. When there is no start and end time
   specified returns the latest available data for the given interface Id. For detailed information about the usage
   of the API, please refer to the Open API specification document - https //github.com/cisco-en-
   programmability/catalyst-center-api-specs/blob/main/Assurance/CE_Cat_Center_Org-interfaces-1.0.2-resolved.yaml.
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module_info
author: Rafael Campos (@racampos)
options:
  headers:
    description: Additional headers.
    type: dict
  startTime:
    description:
    - >
      StartTime query parameter. Start time from which API queries the data set related to the resource. It must
      be specified in UNIX epochtime in milliseconds. Value is inclusive. If `startTime` is not provided, API will
      default to current time.
    type: float
  endTime:
    description:
    - >
      EndTime query parameter. End time to which API queries the data set related to the resource. It must be
      specified in UNIX epochtime in milliseconds. Value is inclusive.
    type: float
  limit:
    description:
    - Limit query parameter. Maximum number of records to return.
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
  siteHierarchy:
    description:
    - >
      SiteHierarchy query parameter. The full hierarchical breakdown of the site tree starting from Global site
      name and ending with the specific site name. The Root site is named "Global" (Ex.
      `Global/AreaName/BuildingName/FloorName`) This field supports wildcard asterisk (`*`) character search
      support. E.g. `*/San*, */San, /San*` Examples `?siteHierarchy=Global/AreaName/BuildingName/FloorName`
      (single siteHierarchy requested) `?siteHierarchy=Global/AreaName/BuildingName/FloorName&siteHierarchy=Global
      /AreaName2/BuildingName2/FloorName2` (multiple siteHierarchies requested).
    type: str
  siteHierarchyId:
    description:
    - >
      SiteHierarchyId query parameter. The full hierarchy breakdown of the site tree in id form starting from
      Global site UUID and ending with the specific site UUID. (Ex. `globalUuid/areaUuid/buildingUuid/floorUuid`)
      This field supports wildcard asterisk (`*`) character search support. E.g. `*uuid*, *uuid, uuid*` Examples
      `?siteHierarchyId=globalUuid/areaUuid/buildingUuid/floorUuid `(single siteHierarchyId requested) `?siteHiera
      rchyId=globalUuid/areaUuid/buildingUuid/floorUuid&siteHierarchyId=globalUuid/areaUuid2/buildingUuid2/floorUu
      id2` (multiple siteHierarchyIds requested).
    type: str
  siteId:
    description:
    - >
      SiteId query parameter. The UUID of the site. (Ex. `flooruuid`) Examples `?siteId=id1` (single id requested)
      `?siteId=id1&siteId=id2&siteId=id3` (multiple ids requested).
    type: str
  view:
    description:
    - >
      View query parameter. The specific summary view being requested. This is an optional parameter which can be
      passed to get one or more of the specific view associated fields. The default view is ``configuration``. ###
      Response data proviced by each view 1. **configuration** id,adminStatus,description,duplexConfig,duplexOper,
      interfaceIfIndex,interfaceType,ipv4Address,ipv6AddressList,isL3Interface,isWan,macAddress,mediaType,name,ope
      rStatus, portChannelId,portMode, portType,speed,timestamp,vlanId,networkDeviceId,networkDeviceIpAddress,netw
      orkDeviceMacAddress,siteName,siteHierarchy,siteHierarchyId 2. **statistics** id,name,rxDiscards,rxError,rxRa
      te,rxUtilization,txDiscards,txError,txRate,txUtilization,networkDeviceId,networkDeviceIpAddress,networkDevic
      eMacAddress,siteName,siteHierarchy,siteHierarchyId 3. **stackPort** id,name,peerStackMember,peerStackPort,st
      ackPortType,networkDeviceId,networkDeviceIpAddress,networkDeviceMacAddress,siteName,siteHierarchy,siteHierar
      chyId The default view is configuration, If need to access an additional view, simply include the view name
      in the query parameter. Examples view=configuration (single view requested)
      view=configuration&view=statistic&stackPort (multiple views requested).
    type: str
  attribute:
    description:
    - >
      Attribute query parameter. The following list of attributes can be provided in the attribute field
      id,adminStatus, description,duplexConfig,duplexOper,interfaceIfIndex,interfaceType,ipv4Address,ipv6AddressLi
      st,isL3Interface,isWan,macAddress,mediaType,name,operStatus,peerStackMember,peerStackPort,
      portChannelId,portMode, portType,rxDiscards,rxError,rxRate,rxUtilization,speed,stackPortType,timestamp,txDis
      cards,txError,txRate,txUtilization,vlanId,networkDeviceId,networkDeviceIpAddress,networkDeviceMacAddress,sit
      eName,siteHierarchy,siteHierarchyId If length of attribute list is too long, please use 'views' param
      instead. Examples attributes=name (single attribute requested) attributes=name,description,duplexOper
      (multiple attributes with comma separator).
    type: str
  networkDeviceId:
    description:
    - >
      NetworkDeviceId query parameter. The list of Network Device Uuids. (Ex.
      `6bef213c-19ca-4170-8375-b694e251101c`) Examples `networkDeviceId=6bef213c-19ca-4170-8375-b694e251101c`
      (single networkDeviceId requested) `networkDeviceId=6bef213c-19ca-4170-8375-
      b694e251101c&networkDeviceId=32219612-819e-4b5e-a96b-cf22aca13dd9&networkDeviceId=2541e9a7-b80d-4955-8aa2-
      79b233318ba0` (multiple networkDeviceIds with & separator).
    type: str
  networkDeviceIpAddress:
    description:
    - >
      NetworkDeviceIpAddress query parameter. The list of Network Device management IP Address. (Ex. `121.1.1.10`)
      This field supports wildcard (`*`) character-based search. Ex `*1.1*` or `1.1*` or `*1.1` Examples
      `networkDeviceIpAddress=121.1.1.10`
      `networkDeviceIpAddress=121.1.1.10&networkDeviceIpAddress=172.20.1.10&networkDeviceIpAddress=10.10.20.10`
      (multiple networkDevice IP Address with & separator).
    type: str
  networkDeviceMacAddress:
    description:
    - >
      NetworkDeviceMacAddress query parameter. The list of Network Device MAC Address. (Ex. `64 f6 9d 07 9a 00`)
      This field supports wildcard (`*`) character-based search. Ex `*AB AB AB*` or `AB AB AB*` or `*AB AB AB`
      Examples `networkDeviceMacAddress=64 f6 9d 07 9a 00` `networkDeviceMacAddress=64 f6 9d 07 9a
      00&networkDeviceMacAddress=70 56 9d 07 ac 77` (multiple networkDevice MAC addresses with & separator).
    type: str
  interfaceId:
    description:
    - >
      InterfaceId query parameter. The list of Interface Uuids. (Ex. `6bef213c-19ca-4170-8375-b694e251101c`)
      Examples `interfaceId=6bef213c-19ca-4170-8375-b694e251101c` (single interface uuid ) `interfaceId=6bef213c-
      19ca-4170-8375-b694e251101c&32219612-819e-4b5e-a96b-cf22aca13dd9&2541e9a7-b80d-4955-8aa2-79b233318ba0`
      (multiple Interface uuid with & separator).
    type: str
  interfaceName:
    description:
    - >
      InterfaceName query parameter. The list of Interface name (Ex. `GigabitEthernet1/0/1`) This field supports
      wildcard (`*`) character-based search. Ex `*1/0/1*` or `1/0/1*` or `*1/0/1` Examples
      `interfaceNames=GigabitEthernet1/0/1` (single interface name)
      `interfaceNames=GigabitEthernet1/0/1&GigabitEthernet2/0/1&GigabitEthernet3/0/1` (multiple interface names
      with & separator).
    type: str
  id:
    description:
    - Id path parameter. The interface Uuid.
    type: str
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Devices GetTheInterfaceDataForTheGivenInterfaceIdinstanceUuidAlongWithTheStatisticsDataV1
  description: Complete reference of the GetTheInterfaceDataForTheGivenInterfaceIdinstanceUuidAlongWithTheStatisticsDataV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!get-the-interface-data-for-the-given-interface-idinstance-uuid-along-with-the-statistics-data
- name: Cisco DNA Center documentation for Devices GetsInterfacesAlongWithStatisticsDataFromAllNetworkDevicesV1
  description: Complete reference of the GetsInterfacesAlongWithStatisticsDataFromAllNetworkDevicesV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!gets-interfaces-along-with-statistics-data-from-all-network-devices
notes:
  - SDK Method used are
    devices.Devices.get_the_interface_data_for_the_given_interface_idinstance_uuid_along_with_the_statistics_data_v1,
    devices.Devices.gets_interfaces_along_with_statistics_data_from_all_network_devices_v1,

  - Paths used are
    get /dna/data/api/v1/interfaces,
    get /dna/data/api/v1/interfaces/{id},

"""

EXAMPLES = r"""
- name: Get all Interfaces V1
  cisco.dnac.interfaces_v1_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    startTime: 0
    endTime: 0
    limit: 0
    offset: 0
    sortBy: string
    order: string
    siteHierarchy: string
    siteHierarchyId: string
    siteId: string
    view: string
    attribute: string
    networkDeviceId: string
    networkDeviceIpAddress: string
    networkDeviceMacAddress: string
    interfaceId: string
    interfaceName: string
  register: result

- name: Get Interfaces V1 by id
  cisco.dnac.interfaces_v1_info:
    dnac_host: "{{dnac_host}}"
    dnac_username: "{{dnac_username}}"
    dnac_password: "{{dnac_password}}"
    dnac_verify: "{{dnac_verify}}"
    dnac_port: "{{dnac_port}}"
    dnac_version: "{{dnac_version}}"
    dnac_debug: "{{dnac_debug}}"
    headers: "{{my_headers | from_json}}"
    startTime: 0
    endTime: 0
    view: string
    attribute: string
    id: string
  register: result

"""
RETURN = r"""
dnac_response:
  description: A dictionary or list with the response returned by the Cisco DNAC Python SDK
  returned: always
  type: dict
  sample: >
    {
      "response": {
        "id": "string",
        "adminStatus": "string",
        "description": "string",
        "duplexConfig": "string",
        "duplexOper": "string",
        "interfaceIfIndex": 0,
        "interfaceType": "string",
        "ipv4Address": "string",
        "ipv6AddressList": [
          "string"
        ],
        "isL3Interface": true,
        "isWan": true,
        "macAddr": "string",
        "mediaType": "string",
        "name": "string",
        "operStatus": "string",
        "peerStackMember": 0,
        "peerStackPort": "string",
        "portChannelId": "string",
        "portMode": "string",
        "portType": "string",
        "rxDiscards": 0,
        "rxError": 0,
        "rxRate": 0,
        "rxUtilization": 0,
        "speed": "string",
        "stackPortType": "string",
        "timestamp": 0,
        "txDiscards": 0,
        "txError": 0,
        "txRate": 0,
        "txUtilization": 0,
        "vlanId": "string",
        "networkDeviceId": "string",
        "networkDeviceIpAddress": "string",
        "networkDeviceMacAddress": "string",
        "siteName": "string",
        "siteHierarchy": "string",
        "siteHierarchyId": "string"
      },
      "version": "string"
    }
"""