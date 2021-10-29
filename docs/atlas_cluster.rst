.. _atlas_cluster_module:


atlas_cluster -- Manage database clusters in Atlas
==================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

The clusters module provides access to your cluster configurations.

The module lets you create, edit and delete clusters.

`API Documentation <https://docs.atlas.mongodb.com/reference/api/clusters/>`_






Parameters
----------

  name (True, str, None)
    Name of the cluster as it appears in Atlas. Once the cluster is created, its name cannot be changed.


  mongoDBMajorVersion (optional, str, None)
    Version of the cluster to deploy.

    Atlas always deploys the cluster with the latest stable release of the specified version.

    You can upgrade to a newer version of MongoDB when you modify a cluster.


  clusterType (optional, str, REPLICASET)
    Type of the cluster that you want to create.


  replicationFactor (optional, int, 3)
    Number of replica set members. Each member keeps a copy of your databases, providing high availability and data redundancy.


  autoScaling (False, dict, None)
    Configure your cluster to automatically scale its storage and cluster tier.


    diskGBEnabled (optional, bool, None)
      Specifies whether disk auto-scaling is enabled. The default is true.



  providerSettings (True, dict, None)
    Configuration for the provisioned servers on which MongoDB runs.

    The available options are specific to the cloud service provider.


    providerName (True, str, None)
      Cloud service provider on which the servers are provisioned.


    regionName (True, str, None)
      Physical location of your MongoDB cluster.


    instanceSizeName (True, str, None)
      Atlas provides different cluster tiers, each with a default storage capacity and RAM size.

      The cluster you select is used for all the data-bearing servers in your cluster tier.



  diskSizeGB (optional, int, None)
    Capacity, in gigabytes, of the host's root volume. Increase this number to add capacity, up to a maximum possible value of 4096 (i.e., 4 TB). This value must be a positive integer.


  providerBackupEnabled (optional, bool, None)
    Flag that indicates if the cluster uses Cloud Backups for backups.


  pitEnabled (optional, bool, None)
    Flag that indicates the cluster uses continuous cloud backups.


  apiUsername (True, str, None)
    The username for use in authentication with the Atlas API.

    Can use API users and tokens (public key is username)


  apiPassword (True, str, None)
    The password for use in authentication with the Atlas API.

    Can use API users and tokens (private key is password)


  groupId (True, str, None)
    Unique identifier for the Atlas project.


  state (optional, str, present)
    State of the ressource.









Examples
--------

.. code-block:: yaml+jinja

    
        - name: test cluster
          atlas_cluster:
            apiUsername: "API_user"
            apiPassword: "API_passwort_or_token"
            groupId: "GROUP_ID"
            name: "testcluster"
            mongoDBMajorVersion: "4.0"
            clusterType: "REPLICASET"
            providerSettings:
              providerName: "GCP"
              regionName: "EUROPE_WEST_3"
              instanceSizeName: "M10"
    ...





Status
------




- This module is not guaranteed to have a backwards compatible interface. *[preview]*


- This module is maintained by community.



Authors
~~~~~~~

- Martin Schurz (@schurzi)

