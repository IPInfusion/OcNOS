

| Mode            | Configuration                       | Description                                                  |
| --------------- | ----------------------------------- | :----------------------------------------------------------- |
| config          | hostname CE2                   | Configures the hostname                                      |
| config      | hardware-profile filter cfm-domain-name-str enable | Enable hardware profile for cfm                |
| config      | hardware-profile statistics ingress-acl enable     | Enable hardware profile for ingress-acl enable |
| config      | hardware-profile statistics cfm-lm enable          | Enable profile for CFM LM                      |
| config      | hardware-profile statistics cfm-ccm enable         | Enable profile for CFM CCM                     |
| config | interface l0 | Configure interface loopback |
| config | ip address 2.2.2.2/32 secondary | Configures IP address for loopback |
| config | bridge 1 protocol rstp vlan enable | Create bridge as RSTP bridge |
| config | vlan database | Configure VLAN |
| config-vlan | vlan 100 bridge 1 state enable | Create VLAN 100 in Bridge 1 |
| config | interface E02 | Go to Interface mode |
| config-if | switchport | Enable as port layer2 |
| config-if | bridge-group 1 | Associate the port to bridge group1 |
| config-if | switchport mode trunk | Configure the port as trunk port |
| config-if | switchport mode trunk allowed vlan all | Allow all vlan on the trunk port |
| config | ethernet cfm domain-type character-string domain-name DOMNAM level 4 mip-creation default bridge 1 | Create a CFM MD and assign a level to it |
| config-ether-cfm | service ma-type string ma-name MANAM vlan 100 mip-creation default | Create a Maintenance Associattion |
| config-ether-cfm-ma | ethernet cfm mep down mpid 1 active true local-vid 100 E02 | Create a down MEP ID 1 for VID 100 |
| config-ether-cfm-ma-mep | cc multicast state enable | Enable CC multicast |
| config-ether-cfm-ma | mep crosscheck mpid 1 | Enable MEP crosscheck |
|    |                                     |                                                 |
|    |                                     |                                                 |
|    |                                     |                                                 |
|    |                                     |                                                 |
|    |                                     |                                                 |


