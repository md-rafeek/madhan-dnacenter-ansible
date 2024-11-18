#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2021, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)


DOCUMENTATION = r"""
---
module: telemetry_settings_apply
short_description: Resource module for Telemetry Settings Apply
description:
- This module represents an alias of the module telemetry_settings_apply_v1
version_added: '6.15.0'
extends_documentation_fragment:
  - cisco.dnac.module
author: Rafael Campos (@racampos)
options:
  deviceIds:
    description: The list of device Ids to perform the provisioning against.
    elements: str
    type: list
requirements:
- dnacentersdk >= 2.4.9
- python >= 3.5
seealso:
- name: Cisco DNA Center documentation for Network Settings UpdateADevicesTelemetrySettingsToConformToTheTelemetrySettingsForItsSiteV1
  description: Complete reference of the UpdateADevicesTelemetrySettingsToConformToTheTelemetrySettingsForItsSiteV1 API.
  link: https://developer.cisco.com/docs/dna-center/#!update-a-devices-telemetry-settings-to-conform-to-the-telemetry-settings-for-its-site-v-1
notes:
  - SDK Method used are
    network_settings.NetworkSettings.update_a_devices_telemetry_settings_to_conform_to_the_telemetry_settings_for_its_site_v1,

  - Paths used are
    post /dna/intent/api/v1/telemetrySettings/apply,
  - It should be noted that this module is an alias of telemetry_settings_apply_v1

"""

EXAMPLES = r"""
"""
RETURN = r"""
dnac_response:
  This alias returns the output of telemetry_settings_apply_v1.
"""
