#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2020 T-Systems MMS
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
# This module is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this software.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "0.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: atlas_user
short_description: Manage database users in Atlas
description:
  - The atlas_users module lets you create, modify and delete the database users in your cluster.
  - Each user has a set of roles that provide access to the project's databases.
  - A user's roles apply to all the clusters in the project
  - if two clusters have a products database and a user has a role granting read access on the products database,
  - the user has that access on both clusters.
  - L(API Documentation,https://docs.atlas.mongodb.com/reference/api/database-users/)
author: "Martin Schurz (@schurzi)"
extends_documentation_fragment: t_systems_mms.mongodb_atlas.atlas_global_options
options:
  databaseName:
    description:
      - Database against which Atlas authenticates the user.
    choices: ["admin", "$external"]
    default: "admin"
    type: str
  username:
    description:
      - Username for authenticating to MongoDB.
    required: true
    type: str
  password:
    description:
      - User's password.
    required: true
    type: str
  roles:
    description:
      - Array of this user's roles and the databases / collections on which the roles apply.
      - A role must include following elements
    suboptions:
      databaseName:
        required: true
        type: str
        description:
          - Database on which the user has the specified role.
          - A role on the admin database can include privileges that apply to the other databases.
      roleName:
        required: true
        type: str
        description:
          - Name of the role. This value can either be a built-in role or a custom role.
    required: true
    type: list
    elements: dict
  scopes:
    description:
      - List of clusters and Atlas Data Lakes that this user can access.
      - Atlas grants database users access to all resources by default.
    suboptions:
      name:
        required: true
        type: str
        description:
          - Name of cluster and Atlas Data Lake.
      type:
        type: str
        choices: ["CLUSTER", "DATA_LAKE"]
        default: "CLUSTER"
        description:
          - Either "CLUSTER" or "DATA_LAKE" depending on target.
    required: false
    type: list
    elements: dict
"""

EXAMPLES = """
    - name: test user
      atlas_user:
        apiUsername: "API_user"
        apiPassword: "API_passwort_or_token"
        groupId: "GROUP_ID"
        username: my_app_user
        password: SuperSecret!
        roles:
          - databaseName: private_info
            roleName: read
          - databaseName: public_info
            roleName: readWrite
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.t_systems_mms.mongodb_atlas.plugins.module_utils.atlas import (
    AtlasAPIObject,
)


# ===========================================
# Module execution.
#
def main():
    # add our own arguments
    argument_spec = dict(
        state=dict(default="present", choices=["absent", "present"]),
        apiUsername=dict(required=True),
        apiPassword=dict(required=True, no_log=True),
        groupId=dict(required=True),
        databaseName=dict(default="admin", choices=["admin", "$external"]),
        username=dict(required=True),
        password=dict(required=True, no_log=True),
        roles=dict(
            required=True,
            type="list",
            elements="dict",
            options=dict(
                databaseName=dict(required=True),
                roleName=dict(required=True),
            ),
        ),
        scopes=dict(
            required=False,
            type="list",
            elements="dict",
            options=dict(
                name=dict(required=True),
                type=dict(default="CLUSTER", choices=["CLUSTER", "DATA_LAKE"]),
            ),
        ),
    )

    # Define the main module
    module = AnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True
    )

    data = {
        "databaseName": module.params["databaseName"],
        "username": module.params["username"],
        "password": module.params["password"],
        "roles": module.params["roles"],
        "scopes": module.params["scopes"],
    }

    try:
        atlas = AtlasAPIObject(
            module=module,
            path="/databaseUsers",
            object_name="username",
            groupId=module.params["groupId"],
            data=data,
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
