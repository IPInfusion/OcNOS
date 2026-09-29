# OcNOS: YANG models, SNMP MIBs and Ansible files

OcNOS is the network operating system from [IP Infusion](https://www.ipinfusion.com/products/ocnos/)
for service provider and data center networks on open hardware. This repository publishes the
machine-readable files you need to automate it: YANG models, SNMP MIBs and Ansible content, one
branch per OcNOS release.

## Find the files for your release

`master` holds only this README. Each release has its own branch, named by product line and version:

| Product line | Branch pattern | Example |
|---|---|---|
| OcNOS Data Center | `OcNOS-DC-<version>` | `OcNOS-DC-7.0.2` |
| OcNOS Service Provider | `OcNOS-SP-<version>` | `OcNOS-SP-7.0.2` |
| OcNOS OTN | `OCNOS-OTN-<version>` | `OCNOS-OTN-6.5.2` |

Check your release with `show version` on the device, then switch to the matching branch in the
branch menu above, or clone just that branch:

```
git clone --branch OcNOS-DC-7.0.2 --single-branch https://github.com/IPInfusion/OcNOS.git
```

Each branch contains:

- `yang-files/`: the YANG models the release implements
- `mibs/`: SNMP MIB files to load into your NMS
- `ansible/`: Ansible modules, on older release branches only. For current releases use the collection below.

## Automation

- Ansible collection: [IPInfusion/ocnos-ansible-collection](https://github.com/IPInfusion/ocnos-ansible-collection) (`ipinfusion.ocnos` on Ansible Galaxy)
- Example playbooks: [IPInfusion/ocnos-ansible-playbooks](https://github.com/IPInfusion/ocnos-ansible-playbooks)
- NETCONF and YANG on OcNOS: https://www.ipinfusion.com/technology/netconf-yang/
- Network automation overview: https://www.ipinfusion.com/automation/

## Try OcNOS

- Free OcNOS virtual machine and demos: https://www.ipinfusion.com/free-software-demos/
- Run OcNOS in EVE-NG: https://www.ipinfusion.com/eve-ng/
- Product documentation: https://documentation.ipinfusion.com/home/Content/LibraryPages/Library.htm

## Questions and support

Found a problem with a file in this repository? Open an issue and name the branch.
For product support, use https://www.ipinfusion.com/support/. Issues here are not a support channel.
