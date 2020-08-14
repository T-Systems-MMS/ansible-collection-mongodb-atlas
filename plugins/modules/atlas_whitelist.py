#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: atlas_whitelist
short_description: Manage IP whitelists in Atlas
description:
   - The whitelist module manages a Atlas project’s IP whitelist.
   - API Documentation: U(https://docs.atlas.mongodb.com/reference/api/whitelist/)
author: Martin Schurz
options:
  api_username:
    description:
      - The username for use in authentication with the Atlas API.
      - Can use API users and tokens (public key is username)
    type: str
    required: True
  api_password:
    description:
      - The password for use in authentication with the Atlas API.
      - Can use API users and tokens (private key is password)
    type: str
    required: True
  state:
    description:
      - State of the ressource.
    choices: [ "present", "absent" ]
    default: present
    type: str
  groupid:
    description:
      - Unique identifier for the Atlas project.
    type: str
    required: True
  cidrBlock:
    description:
      - Whitelist entry in Classless Inter-Domain Routing (CIDR) notation. 
    type: str
    required: True
  comment:
    description:
      - Optional Comment associated with the whitelist entry.
    type: str
    default: "created by Ansible"
"""

EXAMPLES = """
    - name: test whitelist
      atlas_whitelist:
        api_username: "API_user"
        api_password: "API_passwort_or_token" 
        groupid: "GROUP_ID"
        cidrBlock: "192.168.0.0/24"
        comment: "test"
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.urls import url_argument_spec
from ansible_collections.t_systems_mms.mongodb_atlas.plugins.module_utils.atlas import (
    AtlasAPIObject,
)


# ===========================================
# Module execution.
#
def main():
    # add our own arguments
    argument_spec= dict(
        state=dict(default="present", choices=["absent", "present"]),
        api_username=dict(required=True),
        api_password=dict(required=True,no_log=True),
        url_password=dict(no_log=True),
        groupid=dict(required=True),
        cidrBlock=dict(required=True),
        comment=dict(default="created by Ansible"),
    )

    # Define the main module
    module = AnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True
    )

    data = {
        "cidrBlock": module.params["cidrBlock"],
        "comment": module.params["comment"],
    }

    try:
        atlas = AtlasAPIObject(
            module=module, path="/whitelist", 
            object_name="cidrBlock",
            groupid=module.params["groupid"],
            data=data, 
            data_is_array=True,
        )
    except Exception as e:
        module.fail_json(
            msg="unable to connect to Atlas API. Exception message: %s" % e
        )

    changed, diff = atlas.update(module.params["state"])
    module.exit_json(
        changed=changed,
        data=atlas.data,
        diff=diff,
    )


# import module snippets
if __name__ == "__main__":
    main()
