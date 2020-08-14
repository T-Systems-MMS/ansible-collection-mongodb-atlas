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
module: atlas_cluster
short_description: Manage database clusters in Atlas
description:
   - The clusters module provides access to your cluster configurations.
   - The module lets you create, edit and delete clusters.
   - API Documentation: U(https://docs.atlas.mongodb.com/reference/api/clusters/)
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
  name:
    description:
      - Name of the cluster as it appears in Atlas. Once the cluster is created, its name cannot be changed.
    type: str
    required: True
  mongoDBMajorVersion:
    description:
      - Version of the cluster to deploy.
      - Atlas always deploys the cluster with the latest stable release of the specified version. 
      - You can upgrade to a newer version of MongoDB when you modify a cluster.
    choices: [ "3.6", "4.0", "4.2", "4.4" ]
    type: str
  clusterType:
    description:
      - Type of the cluster that you want to create.
    choices: [ "REPLICASET", "SHARDED" ]
    default: "REPLICASET"
    type: str
  replicationFactor:
    description:
      - Number of replica set members. Each member keeps a copy of your databases, providing high availability and data redundancy. 
    choices: [ 3, 5, 7 ]
    default: 3
    type: int
  autoScaling:
    description:
      - Configure your cluster to automatically scale its storage and cluster tier. 
      - ' - C(diskGBEnabled) (bool): Specifies whether disk auto-scaling is enabled. The default is true.
    required: False
    type: list
  providerSettings:
    description:
      - Configuration for the provisioned servers on which MongoDB runs.
      - The available options are specific to the cloud service provider.
      - ' - C(providerName) (string): Cloud service provider on which the servers are provisioned.
      - ' - C(regionName) (string): Physical location of your MongoDB cluster.
      - ' - C(instanceSizeName) (string): Atlas provides different cluster tiers, each with a default storage capacity and RAM size.
            The cluster you select is used for all the data-bearing servers in your cluster tier.
    required: True
    type: list
  diskSizeGB:
    description:
      - Capacity, in gigabytes, of the host’s root volume. Increase this number to add capacity, 
        up to a maximum possible value of 4096 (i.e., 4 TB). This value must be a positive integer.
    type: int
  providerBackupEnabled:
    description:
      - Flag that indicates if the cluster uses Cloud Backups for backups.
    type: bool
  pitEnabled:
    description:
      - Flag that indicates the cluster uses continuous cloud backups.
    type: bool
"""

EXAMPLES = """
    - name: test cluster
      atlas_cluster:
        api_username: "API_user"
        api_password: "API_passwort_or_token" 
        groupid: "GROUP_ID"
        name: "testcluster"
        mongoDBMajorVersion: "4.0"
        clusterType: "REPLICASET"
        providerSettings:
          providerName: "GCP"
          regionName: "EUROPE_WEST_3"
          instanceSizeName: "M10"
...
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
        name=dict(required=True),
        mongoDBMajorVersion=dict(choices=[ "3.6", "4.0", "4.2", "4.4" ]),
        clusterType=dict(default="REPLICASET", choices=[ "REPLICASET", "SHARDED" ]),
        replicationFactor=dict(default=3, type="int", choices=[ 3, 5, 7 ]),
        autoScaling=dict(type="dict", options= dict(
          diskGBEnabled=dict(type="bool"),
        )),
        providerSettings=dict(type="dict", required=True, options= dict(
          providerName=dict(required=True),
          regionName=dict(required=True),
          instanceSizeName=dict(required=True),
        )),
        diskSizeGB=dict(type="int"),
        providerBackupEnabled=dict(type="bool"),
        pitEnabled=dict(type="bool"),
    )

    # Define the main module
    module = AnsibleModule(
        argument_spec=argument_spec, supports_check_mode=True
    )


    data = {
        "name": module.params["name"],
        "clusterType": module.params["clusterType"],
        "replicationFactor": module.params["replicationFactor"],
        "providerSettings": module.params["providerSettings"],
    }

    # handle optional options
    if "mongoDBMajorVersion" in module.params:
      data.update({"mongoDBMajorVersion": module.params["mongoDBMajorVersion"]})

    if "autoScaling" in module.params:
      data.update({"autoScaling": module.params["autoScaling"]})

    if "diskSizeGB" in module.params:
      data.update({"diskSizeGB": module.params["diskSizeGB"]})

    if "providerBackupEnabled" in module.params:
      data.update({"providerBackupEnabled": module.params["providerBackupEnabled"]})

    if "pitEnabled" in module.params:
      data.update({"pitEnabled": module.params["pitEnabled"]})

    try:
        atlas = AtlasAPIObject(
            module=module, path="/clusters", 
            object_name="name",
            groupid=module.params["groupid"],
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
