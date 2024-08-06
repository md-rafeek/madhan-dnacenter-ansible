#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type
import json
import importlib  
import inspect    
import pkgutil    
import difflib 
from ansible_collections.cisco.dnac.plugins.module_utils.dnac import (
    DnacBase,
    validate_list_of_dicts,
    validate_str,
    get_dict_result,
)

class FindVersionNumber(DnacBase):
    """Class containing member attributes for DNAC Version details"""

    def __init__(self, module):
        super().__init__(module)
        self.supported_states = ["merged"]
        self.payload = module.params
        self.version_details = self.load_version_based_json("dnacsdk_verison.json")

    def load_version_based_json(self, json_file_name=str):
        """
        This funciton used to load the json file to string.
        """
        if not json_file_name:
            self.log("SDK json version based file input missing.", "ERROR")

        try:
            with open(json_file_name, 'r') as file:
                data = json.load(file)
            return data
        except Exception as e:
            self.msg = "Unable to open the Json file '{0}'.".format(json_file_name)
            self.log(self.msg + str(e), "WARNING")
            self.module.fail_json(msg=self.msg)

    def check_payload_with_uplifted(self, payload=any, family=str, function=str, version=str):
        """
        This function used to check with the uplifted Version have the below function in the file.
        Parameters:
            self (object): An instance of a class for Cisco Catalyst Center interaction.
            payload (dict): Dictionary containing input param which used to pass as payload of API.
            family (str): sdk family to call the API
            function (str): sdk function to call the API
            version (str): SDK version to call

        Returns:
            True or False (Boolean) : Return status of the available in uplifted
            version (str) : Used to update the version details.

        Description:
            This function used to check with the uplifted Version have the below function in the file.
        """
        if self.check_family_function_in_uplifted(family, function, version):
            required_keys = self.version_details["updated_version"]["required"]
            self.check_required_keys(payload, required_keys)
            optional_req_keys = self.version_details["updated_version"]["required_optional"]
            self.check_required_optional_keys(payload, optional_req_keys)
            if self.check_required_keys(payload, required_keys) and\
               self.check_required_optional_keys(payload, optional_req_keys):
                return True, version

            return False, version

    def check_family_function_in_uplifted(self, family=str, function=str, version=str):
        """
        Check the Family, Function and Versions are in the uplifted.
        """
        if not family or not function or not version:
            self.log("missing family: {0}, function: {1}, version: {2}".format(
                family, function, version), "ERROR")
            return None
        else:
            key_format = family + "^" + function + "^" + version
            if not self.version_details["updated_version"].get(key_format):
                return True
            else:
                self.log("Family and Funtion are not in Uplifted version.", "DEBUG")
                return False

    def check_required_keys(self, payload=any, required_keys=list):
        """
        Check the Required field key is matching with the payload of the input
        """
        # Checking Required key in the payload
        all_required_key_count = len(required_keys)
        payload_match_key_count = 1
        for each_key in required_keys:
            if self.depth_search_key(payload, each_key):
                payload_match_key_count += 1
            else:
                self.msg = "Required key '{0}' is missing in the payload.".format(each_key)
                self.log(self.msg, "DEBUG")
                self.module.fail_json(msg=self.msg)
        if all_required_key_count == payload_match_key_count:
            return True
        else:
            return False

    def check_required_optional_keys(self, payload=any, required_optional_keys=list):
        """
        Check the Optional but any only the field key required
        """
        # Checking Required optional key in the payload
        all_required_optional_key_count = len(required_optional_keys)
        payload_unmatch_key_count = 1
        for each_key in required_optional_keys:
            if self.depth_search_key(payload, each_key):
                return True
            else:
                self.msg = "Optionsal key '{0}' is not there in the payload.".format(each_key)
                self.log(self.msg, "DEBUG")
                payload_unmatch_key_count += 1

        if all_required_optional_key_count == payload_unmatch_key_count:
            return False

    def format_version(self, version):
        """
        Converts version from '2.3.5.3' to 'v2_3_5_3'.
        
        Parameters:
        version (str): The version string in 'X.Y.Z.W' format.
        
        Returns:
        str: The formatted version string.
        """
        formatted_version = 'v' + version.replace('.', '_')  # Replace dots with underscores and prefix with 'v'
        return formatted_version

    def validate_version(self, version):
        """
        Validates if the provided version is among the known versions.
        
        Parameters:
        version (str): The version string to be validated.
        
        Raises:
        VersionError: If the version is not among the known versions.
        """
        valid_versions = self.version_details["valid_versions"]  # List of known versions

        # Check if the provided version is in the list of valid versions
        if version not in valid_versions:
            raise self.VersionError(
                'Unknown API version, known versions are: {0}'.format(str(valid_versions))
            )

    def depth_search_key(self, payload, search_key):
        """
        this function used the serarch specific key in the payload.
        """
        input_dict = payload
        target_string = search_key

        if isinstance(input_dict, dict):
            for key, value in input_dict.items():
                if key == target_string:
                    return True
                result = self.depth_search_key(value, target_string)
                if result is not None:
                    return result
        elif isinstance(input_dict, list):
            for item in input_dict:
                result = self.depth_search_key(item, target_string)
                if result is not None:
                    return result
        return None

    def list_defined_methods(self, cls_obj):
        """Lists all methods of a given class."""
        methods = []
        
        # Iterate over all members of the class
        for name, obj in inspect.getmembers(cls_obj, inspect.isfunction):
            print(name, obj)
            # Check if the function is defined in the class's module
            if obj.__module__ == cls_obj.__module__:
                # If it is, add the method name to the methods list
                methods.append(name)
        
        return methods

    def find_closest_family(self, module, family):
        """
        Finds the closest matching family name from available modules.
        """
        available_families = self.get_available_families(module)
        closest_matches = difflib.get_close_matches(family, available_families)
        if closest_matches:
            return closest_matches[0]

    def get_available_families(self, module):
        """Gets the names of all modules available in the given module's directory."""
        available_families = []
        for _, name, _ in pkgutil.iter_modules(module.__path__):
            available_families.append(name)
        return available_families

    def try_import_module(self, version, family):
        """Attempts to import a module dynamically based on the family name and version."""
        formatted_version = self.format_version(version)
        module_path = "dnacentersdk.api.{}".format(formatted_version)

        try:
            base_module = importlib.import_module(module_path)
            family_name = self.find_closest_family(base_module, family)
            if family_name:
                submodule_path = "{}.{}".format(module_path, family_name)
                return importlib.import_module(submodule_path)
            else:
                raise ImportError("Module for family '{}' not found in version '{}'.".format(family, version))
        except ImportError as e:
            raise ImportError("Module for version '{}' not found: {}.".format(version, e))

    def filter_methods_by_hint(self, methods, hint):
        """Filters methods to include only those containing the hint in their name."""
        matching_methods = []
        
        # Iterate over each method name in the methods list
        for method in methods:
            # Check if the hint is a substring of the method name
            if hint in method:
                # If it is, add the method name to the matching_methods list
                matching_methods.append(method)
        
        return matching_methods

    def get_class_names(self, module):
        """Gets the names of all classes defined in the given module."""
        class_names = []
        
        # Iterate over all members of the module
        for name, obj in inspect.getmembers(module, inspect.isclass):
            # Check if the class is defined in the given module
            if obj.__module__ == module.__name__:
                class_names.append(name)
        
        return class_names

    def call_function(self, version, family, hint):
        """Checks if a specific function exists in the first class found in the module."""
        try:
            self.validate_version(version)
            module = self.try_import_module(version, family)
            print("Successfully imported {}".format(module.__name__))

            # Use the expanded function to get class names
            class_names = self.get_class_names(module)
            if class_names:
                family_class = getattr(module, class_names[0])
                methods = self.list_defined_methods(family_class)
                matching_methods = self.filter_methods_by_hint(methods, hint)

                if matching_methods:
                    print("Yes, function '{}' is available.".format(matching_methods[0]))
                    return matching_methods[0]  # Return the matched function name
                else:
                    print("No matching function for hint '{}' in version '{}'.".format(hint, version))
                    return None
            else:
                print("No classes found in module '{}'.".format(module.__name__))
                return None
        except ImportError as e:
            print("ImportError: {}.".format(e))
            return None

    def try_import_module_from_json(self, version, family):
        """
        get the function based on the versions
        """
        modules = {
            '2.3.5.3': {
                'user_and_roles': self.version_details["functions_v2_3_5_3"]
            },
            '2.3.7.6': {
                'user_and_roles': self.version_details["functions_v2_3_7_6"]
            }
        }
    
        if version in modules:
            module_dict = modules[version]
            if family in module_dict:
                return module_dict[family]
            else:
                raise ImportError(f"Family '{family}' not found in version '{version}'.")
        else:
            raise ImportError(f"Version '{version}' not found.")

    def get_function(self, version, family, function_key):
        """
        Load the family and function and verify
        """
        if self.validate_version(version):
            try:
                methods_dict = self.try_import_module_from_json(version, family)
                if function_key in methods_dict:
                    return methods_dict[function_key]
                else:
                    print(f"No function found '{function_key}' in version '{version}'.")
                    return None
            except ImportError as e:
                print(f"ImportError: {e}")
                return None

    class VersionError(Exception):
        """Exception raised for invalid DNA Center API versions."""
        pass