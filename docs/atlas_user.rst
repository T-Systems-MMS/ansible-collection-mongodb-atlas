.. _atlas_user_module:


atlas_user -- Manage database users in Atlas
============================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

The atlas_users module lets you create, modify and delete the database users in your cluster.

Each user has a set of roles that provide access to the project's databases.

A user's roles apply to all the clusters in the project

if two clusters have a products database and a user has a role granting read access on the products database,

the user has that access on both clusters.

`API Documentation <https://docs.atlas.mongodb.com/reference/api/database-users/>`_






Parameters
----------

  databaseName (optional, str, admin)
    Database against which Atlas authenticates the user.


  username (True, str, None)
    Username for authenticating to MongoDB.


  password (True, str, None)
    User's password.


  roles (True, list, None)
    Array of this user's roles and the databases / collections on which the roles apply.

    A role must include following elements


    databaseName (True, str, None)
      Database on which the user has the specified role.

      A role on the admin database can include privileges that apply to the other databases.


    roleName (True, str, None)
      Name of the role. This value can either be a built-in role or a custom role.



  scopes (False, list, [])
    List of clusters and Atlas Data Lakes that this user can access.

    Atlas grants database users access to all resources by default.


    name (True, str, None)
      Name of the cluster or Atlas Data Lake that the database user can access.


    type (optional, str, CLUSTER)
      Type of resource that the database user can access.



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





Status
------




- This module is not guaranteed to have a backwards compatible interface. *[preview]*


- This module is maintained by community.



Authors
~~~~~~~

- Martin Schurz (@schurzi)

