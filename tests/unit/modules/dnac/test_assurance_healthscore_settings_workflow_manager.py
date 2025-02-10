# Copyright (c) 2025 Cisco and/or its affiliates.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Make coding more python3-ish
from __future__ import absolute_import, division, print_function

__metaclass__ = type
from unittest.mock import patch
from ansible_collections.cisco.dnac.plugins.modules import assurance_healthscore_settings_workflow_manager
from .dnac_module import TestDnacModule, set_module_args, loadPlaybookData


class TestDnacHealthscoreWorkflow(TestDnacModule):
    module = assurance_healthscore_settings_workflow_manager
    test_data = loadPlaybookData("assurance_healthscore_settings_workflow_manager")
    playbook_config_updation = test_data.get("playbook_config_updation")

    def setUp(self):
        super(TestDnacHealthscoreWorkflow, self).setUp()

        self.mock_dnac_init = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK.__init__")
        self.run_dnac_init = self.mock_dnac_init.start()
        self.run_dnac_init.side_effect = [None]
        self.mock_dnac_exec = patch(
            "ansible_collections.cisco.dnac.plugins.module_utils.dnac.DNACSDK._exec"
        )
        self.run_dnac_exec = self.mock_dnac_exec.start()

        self.load_fixtures()

    def tearDown(self):
        super(TestDnacHealthscoreWorkflow, self).tearDown()
        self.mock_dnac_exec.stop()
        self.mock_dnac_init.stop()

    def load_fixtures(self, response=None, device=""):
        """
        Load fixtures for user.
        """
        if "no_updataion" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("get_kpi_details"),
            ]

        if "updation" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("require_update_kpi_detail_1"),
                self.test_data.get("require_update_kpi_detail_2"),
                self.test_data.get("healthscore_settings_updation"),
                self.test_data.get("updated_kpi_detail"),
                self.test_data.get("after_update_kpi_detail_1"),
                self.test_data.get("after_update_kpi_detail_2"),
            ]

        if "update_not_required" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("kpi_detail"),
                self.test_data.get("require_update_kpi_detail_2"),
                self.test_data.get("healthscore_settings_updation"),
                self.test_data.get("updated_kpi_detail"),
                self.test_data.get("kpi_detail"),
                self.test_data.get("after_update_kpi_detail_2"),
            ]

        if "exception_updation" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                Exception(),
            ]

        if "verification_failure" in self._testMethodName:
            self.run_dnac_exec.side_effect = [
                self.test_data.get("require_update_kpi_detail"),
                self.test_data.get("healthscore_settings_updation"),
                self.test_data.get("require_update_kpi_detail")
            ]

    def test_healthscore_settings_workflow_manager_exception_updation(self):
        """
        Test case for healthscore settings workflow manager exception handling during update.

        Verifies that the healthscore settings workflow manager correctly handles exceptions when attempting
        to update healthscore settings, ensuring the system behaves as expected under error conditions.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_updation
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result['response'][0]['device_healthscore_settings']['msg'])
        self.assertEqual(
            result['response'][0]['device_healthscore_settings']['msg'],
            {}
        )

    def test_healthscore_settings_workflow_manager_update_not_required(self):
        """
        Test case for healthscore settings workflow manager when update is not required.

        Verifies that the healthscore settings workflow manager correctly handles situations where no
        update is needed, ensuring the system behaves as expected when no changes are required.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config=self.playbook_config_updation
            )
        )
        result = self.execute_module(changed=False, failed=False)
        print(result['response'][0]['device_healthscore_settings']['msg'])
        self.assertEqual(
            result['response'][0]['device_healthscore_settings']['msg'],
            {'linkDiscardThreshold': "Healthscore settings doesn't require an update"}
        )

    def test_healthscore_settings_workflow_manager_error_while_update(self):
        """
        Test case for healthscore settings workflow manager when an error occurs during update.

        Verifies that the workflow manager properly handles errors and exceptions during the
        healthscore settings update process, ensuring the system remains stable.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_updation
            )
        )
        result = self.execute_module(changed=False, failed=True)
        print(result['response'][0]['device_healthscore_settings']['msg'])
        self.assertEqual(
            result['response'][0]['device_healthscore_settings']['msg'],
            {}
        )

    def test_healthscore_settings_workflow_manager_updation(self):
        """
        Test case for healthscore settings workflow manager update process.

        Verifies that the healthscore settings workflow manager successfully handles the update process,
        ensuring proper behavior and data integrity during the update.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_version="2.3.7.9",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_updation
            )
        )
        result = self.execute_module(changed=True, failed=False)
        print(result['response']['msg'])
        self.assertEqual(
            result['response']['msg'],
            {'linkDiscardThreshold': 'Healthscore settings Updated Successfully'}
        )

    def test_healthscore_settings_workflow_manager_verification_failure(self):
        """
        Test case for healthscore settings workflow manager verification failure.

        Verifies that the healthscore settings workflow manager handles verification failures correctly,
        ensuring the system responds appropriately when verification of settings fails.
        """

        set_module_args(
            dict(
                dnac_host="1.1.1.1",
                dnac_username="dummy",
                dnac_password="dummy",
                dnac_log=True,
                state="merged",
                config_verify=True,
                config=self.playbook_config_updation
            )
        )
        result = self.execute_module(changed=True, failed=True)
        print(result['response'][0]['device_healthscore_settings']['msg'])
        self.assertEqual(
            result['response'][0]['device_healthscore_settings']['msg'],
            {}
        )
