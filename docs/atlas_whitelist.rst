.. _atlas_whitelist_module:


atlas_whitelist -- Manage IP whitelists in Atlas
================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

The whitelist module manages a Atlas project's IP whitelist.

`API Documentation <https://docs.atlas.mongodb.com/reference/api/whitelist/>`_






Parameters
----------

  cidrBlock (True, str, None)
    Whitelist entry in Classless Inter-Domain Routing (CIDR) notation.


  comment (optional, str, created by Ansible)
    Optional Comment associated with the whitelist entry.


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

    
        - name: test whitelist
          atlas_whitelist:
            apiUsername: "API_user"
            apiPassword: "API_passwort_or_token"
            groupId: "GROUP_ID"
            cidrBlock: "192.168.0.0/24"
            comment: "test"





Status
------




- This module is not guaranteed to have a backwards compatible interface. *[preview]*


- This module is maintained by community.



Authors
~~~~~~~

- Martin Schurz (@schurzi)

