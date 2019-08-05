

| Mode        | Configuration                           | Description                                                  |
| ----------- | --------------------------------------- | :----------------------------------------------------------- |
| config      | hostname leaf2                          | Configures the hostname                                      |
| config      | interface E02                           | Configure the interface                                      |
| config-if   | description **connects to the serverA** | Configure description this connects to  ServerA              |
| config-if   | exit                                    | Exit config interface mode                                   |
| config      | interface E11                           | Configure the interface                                      |
| config-if   | description **connects to the serverB** | Configure description this connects to  ServerB              |
| config-if   | exit                                    | Exit config interface mode                                   |
| config      | interface E05                           | Configure the interface                                      |
| config-if   | description **connects to the Leaf1**   | Configure description this connects to  Leaf2 and is the IDL link |
| config-if   | exit                                    | Exit config interface mode                                   |
| config      | vlan database                           | Configure vlan's                                             |
| config-vlan | vlan 100 bridge 1 state enable          | Add VLAN 100 to signify the VRRP group-1 connection towards ServerA |
| config-vlan | vlan 101 bridge 1 state enable          | Add VLAN 101 to signify the VRRP group-2 connection towards ServerB |
| config-vlan | exit                                    | Exit the vlan mode                                           |
| config      | interface po1                           | Configure the interface port channel                         |
| config-if   | switchport                              | Configure switchport to make it as Layer2                    |
| config-if   | switchport mode hybrid                  | This allows for tagged and untagged packets                  |
| config-if   | switchport mode allowed vlan 100        | This allows for VLAN 100 to be a part of PO1                 |
| config-if   | interface mlag1                         | This adds PO1 as part of MLAG-1                              |
| config-if   | exit                                    | Exit the interface mode                                      |
| config      | interface E02                           | Configure the interface connected to the Server A            |
| config-if   | channel-group 1 mode active             | This make the port member of port channel 1                  |
| config      | interface po2                           | Configure the interface port channel                         |
| config-if   | switchport                              | Configure switchport to make it as Layer2                    |
| config-if   | switchport mode hybrid                  | This allows for tagged and untagged packets                  |
| config-if   | switchport mode allowed vlan 101        | This allows for VLAN 101 to be a part of PO2                 |
| config-if   | interface mlag2                         | This adds PO2 part of MLAG-2                                 |
| config-if   | exit                                    | Exit the interface mode                                      |
| config      | interface E11                           | Configure the interface connected to the Server B            |
| config-if   | channel-group 2 mode active             | This make the port member of port channel 2                  |
| config-if   | exit                                    | Exit the interface mode                                      |
| config      | interface mlag1                         | Configure the MLAG-1 interface                               |
| config-if   | switchport                              | Configure the port as Layer2                                 |
| config-if   | switchport mode allowed vlan 100        | Add vlan 100 to the MLAG-1                                   |
| config-if   | exit                                    | Exit the interface mode                                      |
| config-if   | interface vlan1.100                     | Configure the VLAN as a SVI                                  |
| config-if   | no switchport                           | Make the interface as Layer3                                 |
| config-if   | ip address 120.1.1.6/24                 | Configure the IP address on SVI                              |
| config-if   | exit                                    | Exit the interface mode                                      |
| config-if   | interface vlan1.101                     | Configure the VLAN as a SVI                                  |
| config-if   | no switchport                           | Make the interface as Layer3                                 |
| config-if   | ip address 130.1.1.6/24                 | Configure the IP address on SVI                              |
| config-if   | exit                                    | Exit the interface mode                                      |
| config      | router vrrp 10 vlan 1.100               | Configure  VRRP  for MLAG-1                                  |
| config-vrrp | virtual-ip 120.1.1.6                    | Configure a VRRP-IP for MLAG-1                               |
| config-vrrp | exit                                    | Exit the interface mode                                      |
| config      | router vrrp 11 vlan 1.101               | Configure  VRRP  for MLAG-2                                  |
| config-vrrp | virtual-ip 130.1.1.6                    | Configure a VRRP-IP for MLAG-2                               |
| config-vrrp | exit                                    | Exit the interface mode                                      |
| config      | interface E05                           | Configure the IDL interface                                  |
| config-if   | switchport                              | Configure the interface as Layer2 mode                       |
| config-if   | switchport mode trunk allowed vlan all  | Configure the port to allow all VLAN's in the interface      |
| config-if   | exit                                    | Exit the interface mode                                      |
| config      | mcec domain configure                   | Configure for MLAG domain                                    |
| config-mcec | domain-address 2222.2222.2222           | The domain address should match on both MLAG ends            |
| config-mcec | domain-system-number 2                  | Configure the domain system number ID                        |
| config-mcec | intra-domain-link E05                   | Configure the IDL link for MLAG                              |
| config-mcec | exit                                    | Exit the interface mode                                      |
|             |                                         |                                                              |
|             |                                         |                                                              |

