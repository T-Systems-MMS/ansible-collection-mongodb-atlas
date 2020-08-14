MongoDB Atlas Collection for Ansible
=========

[![ci-ansible-test](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/workflows/ansible-test/badge.svg)](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/actions?query=workflow%3Aansible-test)

This collection contains Ansible [modules](plugins/modules/) to provision and automate the cloud offering of MongoDB via API.

Required Ansible version: 2.9

Installation
------------

These modules are distributed as [collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html).
To install them, run:

```
ansible-galaxy collection install t_systems_mms.mongodb_atlas
```

Alternatively put the collection into a `requirements.yml`-file:

```
---
collections:
- t_systems_mms.mongodb_atlas
```

License
-------

GPLv3

Author Information
------------------

* Martin Schurz
