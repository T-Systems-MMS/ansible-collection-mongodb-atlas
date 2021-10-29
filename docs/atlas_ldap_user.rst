.. _atlas_ldap_user_module:


atlas_ldap_user -- Manage database users in Atlas
=================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

The atlas_ldap_user module lets you create LDAP groups on the admin database by mapping LDAP groups to MongoDB roles on your Atlas databases.

Each user or group has a set of roles that provide access to the project's databases.

`API Documentation <https://docs.atlas.mongodb.com/security-ldaps/>`_






Parameters
----------

  databaseName (optional, str, admin)
    Database against which Atlas authenticates the user.


  ldapAuthType (optional, str, GROUP)
    Type of LDAP authorization for the user i.e. USER or GROUP


  username (True, str, None)
    Username for authenticating to MongoDB.


  roles (True, list, None)
    Array of this user's roles and the databases / collections on which the roles apply.

    A role must include folliwing elements


    databaseName (True, str, None)
      Database on which the user has the specified role.

      A role on the admin database can include privileges that apply to the other databases.


    roleName (True, str, None)
      Name of the role. This value can either be a built-in role or a custom role.



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

    
        - name: LDAP Group or Username
          atlas_ldap_user:
            apiUsername: "API_user"
            apiPassword: "API_passwort_or_token"
            atlas_ldap_user: "USER DN or GROUP DN"
            groupId: "GROUP_ID"
            databaseName: "admin"
            username: my_app_user
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

- Martin Schurz (@schurzi) / Derek Giri

