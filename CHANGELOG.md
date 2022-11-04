# Changelog

## [0.3.4](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/tree/0.3.4) (2022-11-04)

[Full Changelog](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/compare/0.3.3...0.3.4)

**Merged pull requests:**

- use reusable workflow [\#29](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/pull/29) ([rndmh3ro](https://github.com/rndmh3ro))

## [0.3.3](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/tree/0.3.3) (2022-07-29)

[Full Changelog](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/compare/0.3.2...0.3.3)

**Fixed bugs:**

- API: handle 404 error [\#27](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/pull/27) ([Raznak](https://github.com/Raznak))

**Merged pull requests:**

- update list of ansible and python versions to be tested [\#28](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/pull/28) ([schurzi](https://github.com/schurzi))

## [0.3.2](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/tree/0.3.2) (2022-06-10)

[Full Changelog](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/compare/0.3.1...0.3.2)

**Implemented enhancements:**

- Allow new mongodb atlas versions [\#21](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/pull/21) ([hack3d](https://github.com/hack3d))

**Merged pull requests:**

- Update actions/setup-python action to v4 [\#26](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/pull/26) ([renovate[bot]](https://github.com/apps/renovate))
- Update github-actions-x/commit action to v2.9 [\#25](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/pull/25) ([renovate[bot]](https://github.com/apps/renovate))
- Update charmixer/auto-changelog-action action to v1.4 [\#23](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/pull/23) ([renovate[bot]](https://github.com/apps/renovate))
- Configure Renovate [\#20](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/pull/20) ([renovate[bot]](https://github.com/apps/renovate))
- fix documentation workflow [\#19](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/pull/19) ([schurzi](https://github.com/schurzi))
- add workflow job to autgenerate documentation [\#18](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/pull/18) ([schurzi](https://github.com/schurzi))

## [0.3.1](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/tree/0.3.1) (2021-08-18)

[Full Changelog](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/compare/0.3.0...0.3.1)

**Implemented enhancements:**

- atlas\_user - set correct scope if empty parameter  [\#17](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/pull/17) ([schurzi](https://github.com/schurzi))

## [0.3.0](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/tree/0.3.0) (2021-08-17)

[Full Changelog](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/compare/0.2.0...0.3.0)

**Implemented enhancements:**

- add scope to user, so permissions can be restricted to clusters [\#16](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/pull/16) ([schurzi](https://github.com/schurzi))

**Merged pull requests:**

- Improve Release Action [\#15](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/pull/15) ([schurzi](https://github.com/schurzi))
- use version for github action, short sha is no longer supported [\#14](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/pull/14) ([schurzi](https://github.com/schurzi))
- fix galaxy-release action [\#13](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/pull/13) ([rndmh3ro](https://github.com/rndmh3ro))
- update GitHub workflow [\#12](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/pull/12) ([schurzi](https://github.com/schurzi))
- add doc\_fragment for global options [\#11](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/pull/11) ([schurzi](https://github.com/schurzi))

## [0.2.0](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/tree/0.2.0) (2021-01-01)

[Full Changelog](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/compare/0.1.0...0.2.0)

**Implemented enhancements:**

- new module atlas\_ldap\_user for DB Users authenticated via LDAP [\#10](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/pull/10) ([derekgiri](https://github.com/derekgiri))

**Closed issues:**

- Remove unwanted files from release-tarball  [\#5](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/issues/5)
- mixing of camel case and underscore variable names [\#2](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/issues/2)

**Merged pull requests:**

- Create runtime.yml [\#9](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/pull/9) ([rndmh3ro](https://github.com/rndmh3ro))
- Create LICENSE [\#8](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/pull/8) ([rndmh3ro](https://github.com/rndmh3ro))
- run tests on a schedule [\#7](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/pull/7) ([rndmh3ro](https://github.com/rndmh3ro))
- add build\_ignore to filter unneeded files from release [\#6](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/pull/6) ([schurzi](https://github.com/schurzi))

## [0.1.0](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/tree/0.1.0) (2020-08-14)

[Full Changelog](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/compare/0.0.1...0.1.0)

**Implemented enhancements:**

- Use a loop to manage optional parameters [\#1](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/issues/1)
- use loop for optional parameters [\#3](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/pull/3) ([schurzi](https://github.com/schurzi))

**Merged pull requests:**

- change all variables to camel case [\#4](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/pull/4) ([schurzi](https://github.com/schurzi))

## [0.0.1](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/tree/0.0.1) (2020-08-14)

[Full Changelog](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/compare/0.0.0...0.0.1)

## [0.0.0](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/tree/0.0.0) (2020-08-14)

[Full Changelog](https://github.com/T-Systems-MMS/ansible-collection-mongodb-atlas/compare/bcc2143900b453d307cab84cc0547804c0492570...0.0.0)



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
