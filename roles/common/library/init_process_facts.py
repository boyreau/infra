#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_test

short_description: Retrieves information about the init (PID-1) process.

version_added: "0.0.1"

description: This modules lets you handle different init system (systemd, sysVinit, runit, upstart...) easily by putting the init process name in ansible facts.

options:

author:
    - Boyreau (@boyreau)
'''

EXAMPLES = r'''
# Pass in a message
- name: Test with a message
  my_namespace.my_collection.my_test:
    name: hello world

# pass in a message and have changed true
- name: Test with a message and changed output
  my_namespace.my_collection.my_test:
    name: hello world
    new: true

# fail the module
- name: Test failure of the module
  my_namespace.my_collection.my_test:
    name: fail me
'''

RETURN = r'''
# These are examples of possible return values, and in general should use other names for return values.
'''

from ansible.module_utils.basic import AnsibleModule
import subprocess


def run_module():
    # seed the result dict in the object
    # we primarily care about changed and state
    # changed is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        ansible_facts=dict(
            init_process_name='',
        ),
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(
        argument_spec=dict(),
        supports_check_mode=False
    )

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)
    p = subprocess.run(["ps","-q","1","-o","comm="], capture_output=True, text=True)
    result['ansible_facts']['init_process_name'] = p.stdout[:-1] # Trims a newline

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()


