

| Mode            | Configuration                         | Description                                         |
| --------------- | ------------------------------------- | :-------------------------------------------------- |
| config          | hostname PE1                          | Configures the hostname                             |
| config          | interface l0                          | Configure interface loopback                        |
| config-if       | ip address 10.10.10.10/32 secondary   | Configures IP address for loopback                  |
| config          | interface e02                         | Confiure the interface connecte to PE-2             |
| config-if       | ip address 110.1.1.1/24               | Configure IP address                                |
| config-if       | label-switching                       | Enable mpls label switching                         |
| config-if       | enable-ldp ipv4                       | Enable LDP on the interface mode                    |
| config          | interface e03                         | Configure the interface connected to P1             |
| config-if       | ip address 120.1.1.1/24               | Configure IP address                                |
| config-if       | label-switching                       | Enable mpls label switching                         |
| config-if       | enable-ldp ipv4                       | Enable LDP on the interface mode                    |
| config          | mpls vpls dm1 100                     | Configure a vpls domain with ID 100                 |
| config-vpls     | signalling bgp                        | Enable signalling using BGP                         |
| config-vpls-bgp | ve-id 10                              | Configure VE-ID                                     |
| config          | interface e01                         | Configure the attachmet circuit interface           |
| config-if       | switchport                            | Make the port as layer2                             |
| config-if       | mpls-vpls dm1                         | Make this part of the VPLS domain                   |
| config          | router ospf 1                         | Enable ospf                                         |
| config-router   | network 120.1.1.0/24 area 0           | Attach the interface over which ospf has to run     |
| config-router   | network 110.1.1.1/24 area 0           | Attach the interface over which ospf has to run     |
| confg           | router bgp 100                        | Configure router bgp                                |
| config-router   | neighbor 30.30.30.30 remote-as 100    | Configure bgp neighbor                              |
| config-router   | neighbor 30.30.30.30 update-source l0 | Configure bgo to use loopback as the source address |
| config-router   | neighbor 40.40.40.40 remote-as 100    | Configure bgp neighbor                              |
| config-router   | neighbor 40.40.40.40 update-source l0 | Configure bgo to use loopback as the source address |
| config-router   | neighbor 60.60.60.60 remote-as 100    | Configure bgp neighbor                              |
| config-router   | neighbor 60.60.60.60 update-source l0 | Configure bgo to use loopback as the source address |
| confg-router    | address-family 2vpn vpls              | Enable address family for L2VPN                     |
| config-router   | neighbor 60.60.60.60 activate         | Activate PE4 in the VPLS address family             |
| config-router   | neighbor 30.30.30.30 activate         | Activate PE3 in the VPLS address family             |
| config-router   | neighbor 40.40.40.40 activate         | Activate PE2 in the VPLS address family             |

