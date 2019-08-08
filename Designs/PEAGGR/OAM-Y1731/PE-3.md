

| Mode            | Configuration                         | Description                                         |
| --------------- | ------------------------------------- | :-------------------------------------------------- |
| config          | hostname PE3                         | Configures the hostname                             |
| config    | hardware-profile filter cfm-domain-name-str enable | Enable hardware profile for cfm                |
| config    | hardware-profile statistics ingress-acl enable     | Enable hardware profile for ingress-acl enable |
| config    | hardware-profile statistics cfm-lm enable          | Enable profile for CFM LM                      |
| config    | hardware-profile statistics cfm-ccm enable         | Enable profile for CFM CCM                     |
| config          | interface l0                          | Configure interface loopback                        |
| config-if       | ip address 30.30.30.30/32 secondary | Configures IP address for loopback                  |
| config | bridge 1 protocol rstp vlan enable | Create bridge as RSTP bridge |
| config | vlan database | Configure VLAN |
| config-vlan | vlan 100 bridge 1 state enable | Create VLAN 100 in Bridge 1 |
| config          | interface e02                        | Confiure the interface connecte to P-1              |
| config-if       | ip address 140.1.1.2/24             | Configure IP address                                |
| config-if       | label-switching                       | Enable mpls label switching                         |
| config          | mpls vpls dm1 100                     | Configure a vpls domain with ID 100                 |
| config-vpls     | signalling bgp                        | Enable signalling using BGP                         |
| config-vpls-bgp | ve-id 10                              | Configure VE-ID                                     |
| config          | interface e01                      | Configure the attachmet circuit interface           |
| config-if       | switchport                            | Make the port as layer2                             |
| config-if | bridge-group 1 | Associate the port to bridge group1 |
| config-f | switchport mode trunk | Configure the port as trunk port |
| config-if | switchport mode trunk allowed vlan all | Allow all vlan on the trunk port |
| config | ethernet cfm domain-type character-string domain-name DOMNAM2 level 2 mip-creation default bridge 1 | Create a CFM MD and assign a level to it |
| config-ether-cfm | service ma-type string ma-name MANAM vlan 100 mip-creation default | Create a Maintenance Associattion |
| config-ether-cfm-ma | ethernet cfm mep up mpid 1 active true local-vid 100 E02 | Create a down MEP ID 1 for VID 100 |
| config-ether-cfm-ma-mep | cc multicast state enable | Enable CC multicast |
| config-ether-cfm-ma | mep crosscheck mpid 1 | Enable MEP crosscheck |
| config-if       | mpls-vpls dm1                         | Make this part of the VPLS domain                   |
| config          | router ldp                            | Configure LDP as the transport protocol             |
| config          | interface e02                        | Configure LDP on the interface mode                 |
| config-if       | enable-ldp ipv4                       | Configure LDP as tranport on the interface          |
| config          | router ospf 1                         | Enable ospf                                         |
| config-router   | network 140.1.1.1/24 area 0          | Attach the interface over which ospf has to run     |
| confg           | router bgp 100                        | Configure router bgp                                |
| config-router   | neighbor 10.10.10.10 remote-as 100 | Configure bgp neighbor                              |
| config-router   | neighbor 10.10.10.10 update-source l0 | Configure bgo to use loopback as the source address |
| confg-router    | address-family 2vpn vpls              | Enable address family for L2VPN                     |
| config-router   | neighbor 10.10.10.10 activate     | Activate PE2 in the VPLS address family             |
|                 |                                       |                                                     |
|                 |                                       |                                                     |

