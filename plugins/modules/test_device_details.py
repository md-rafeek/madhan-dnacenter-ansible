# -*- coding: utf-8 -*-
# Copyright (c) 2024, Cisco Systems
# GNU General Public License v3.0+ (see LICENSE or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
import time
import re
import json
__metaclass__ = type
__author__ = ("A Mohamed Rafeek, Megha Kandari, Sonali Deepthi Kesali, Natarajan, Madhan Sankaranarayanan, Abhishek Maheshwari")


from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase
)
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.cisco.dnac.plugins.module_utils.verionbased import FindVersionNumber

class Accesspoint(DnacBase):
    """Class containing member attributes for DNAC Access Point Automation module"""

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged"]
        self.payload = module.params
        self.keymap = {}
        self.version = self.dnac.api.version

    def get_accesspoint_details(self, input_config):
        """
        Retrieves the current details of an device in Cisco Catalyst Center.

        Parameters:
        - self (object): An instance of the class containing the method.
        - input_config (dict): A dictionary containing the input configuration details.

        Returns:
        A tuple containing a boolean indicating if the device exists and a
        dictionary of the current inventory details based on the input given from
        playbook either mac_address or management_ip_address or hostname
        (
            True,
            {
                "ap_name": "NFW-AP1-9130AXE",
                "eth_mac": "34:5d:a8:0e:20:b4",
                "led_brightnessLevel": 3,
                "led_status": "Enabled",
                "location": "LTTS",
                "mac_address": "90:e9:5e:03:f3:40"
            }
        )

        Description:
        Retrieve device details from Cisco Catalyst Center using provided MAC address, management IP, or hostname.
        If found, return current device details; otherwise, log errors and fail the function.
        """
        accesspoint_exists = False
        current_configuration = {}
        ap_response = None
        input_param = {}
        input_config = input_config[0]
        self.keymap["mac_address"] = "macAddress"
        self.keymap["management_ip_address"] = "managementIpAddress"
        self.keymap["hostname"] = "hostname"
        for key in ['mac_address', 'management_ip_address', 'hostname']:
            if input_config.get(key):
                input_param[self.keymap[key]]= input_config[key]
                break

        if not input_param:
            msg = """Required param of mac_address, management_ip_address or hostname
                      is not in playbook config"""
            self.log(msg, "WARNING")
            self.module.fail_json(msg=msg, response=msg)

        try:
            ap_response = self.dnac._exec(
                family="devices",
                function='get_device_list',
                op_modifies=True,
                params=input_param,
            )

            self.log(str(ap_response), "WARNING")
            if ap_response and ap_response.get("response"):
                accesspoint_exists = True
                current_configuration = ap_response.get("response")[0]

        except Exception as e:
            self.msg = "The provided device '{0}' is either invalid or not present in the \
                     Cisco Catalyst Center.".format(str(input_param))
            self.log(msg + str(e), "WARNING")

        if not accesspoint_exists:
            self.msg = "The provided device '{0}' is either invalid or not present in the \
                     Cisco Catalyst Center.".format(str(input_param))
            self.module.fail_json(msg="MAC Address not exist:", response=str(self.msg))
        else:
            if current_configuration["family"] != "Unified AP":
                self.msg = "Provided device is not Access Point."
                self.module.fail_json(msg="MAC Address is not Access point")

        responses = {}
        if accesspoint_exists:
            responses["DEVICE_DETAILS"] = current_configuration
            self.result["response"] = responses
            self.result["version"] = self.version
            self.result['Message'] = "Fnd the data below"
            self.result['changed'] = True
        else:
            self.result['changed'] = False
            self.status = "failed"
            self.msg = "Unable to get success response, hence AP config not updated"
            self.result['Message'] = self.msg
        return self

    def pprint(self, jsondata):
        """
        Pretty prints JSON/dictionary data in a readable format.

        Parameters:
            jsondata (dict): Dictionary data to be printed.

        Returns:
            str: Formatted JSON string.
        """
        return json.dumps(jsondata, indent=4, separators=(',', ': '))


def main():
    """ main entry point for module execution
    """
    accepoint_spec = {
        'dnac_host': {'required': True, 'type': 'str'},
        'dnac_port': {'type': 'str', 'default': '443'},
        'dnac_username': {'type': 'str', 'default': 'admin'},
        'dnac_password': {'type': 'str', 'no_log': True},
        'dnac_verify': {'type': 'bool', 'default': 'True'},
        'dnac_version': {'type': 'str', 'default': '2.2.3.3'},
        'dnac_debug': {'type': 'bool', 'default': False},
        'dnac_log': {'type': 'bool', 'default': False},
        'dnac_log_level': {'type': 'str', 'default': 'WARNING'},
        "dnac_log_file_path": {"type": 'str', "default": 'dnac.log'},
        'config_verify': {'type': 'bool', "default": False},
        "dnac_log_append": {"type": 'bool', "default": True},
        'dnac_api_task_timeout': {'type': 'int', "default": 300},
        'dnac_task_poll_interval': {'type': 'int', "default": 2},
        'config': {'required': True, 'type': 'list', 'elements': 'dict'},
        'validate_response_schema': {'type': 'bool', 'default': True},
        'state': {'default': 'merged', 'choices': ['merged', 'deleted']},
        'force_sync': {'type': 'bool'}
    }
    module = AnsibleModule(
        argument_spec=accepoint_spec,
        supports_check_mode=True
    )

    ccc_network = Accesspoint(module)
    state = ccc_network.params.get("state")

    if state not in ccc_network.supported_states:
        ccc_network.status = "invalid"
        ccc_network.msg = "State {0} is invalid".format(state)
        ccc_network.check_return_status()

    ccc_network.get_accesspoint_details(ccc_network.params.get("config"))

    # ccc_network.validate_input_yml().check_return_status()
    # config_verify = ccc_network.params.get("config_verify")

    # for config in ccc_network.validated_config:
    #     ccc_network.reset_values()
    #     ccc_network.get_want(config).check_return_status()
    #     ccc_network.get_have(config).check_return_status()
    #     ccc_network.get_diff_state_apply[state](config).check_return_status()

    #     if config_verify:
    #         time.sleep(20)
    #         ccc_network.verify_diff_state_apply[state](config).check_return_status()

    module.exit_json(**ccc_network.result)


if __name__ == '__main__':
    main()
