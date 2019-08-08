

| Mode          | Configuration                                         | Description                                                |
| ------------- | ----------------------------------------------------- | :--------------------------------------------------------- |
| config        | hostname PE1                                          | Configures the hostname                                    |
| config        | interface l0                                          | Configure interface loopback                               |
| config-if     | ip address 10.10.10.10/32 secondary                   | Configures IP address for loopback                         |
| config        | interface e02                                         | Confiure the interface connecte to P-1                     |
| config-if     | ip address 120.1.1.1/24                               | Configure IP address                                       |
| config-if     | label-switching                                       | Enable mpls label switching                                |
| config-if     | enable-ldp ipv4                                       | Configure LDP a the transport protocol                     |
| config        | interface e03                                         | Confiure the interface connecte to PE-2                    |
| config-if     | ip address 130.1.1.1/24                               | Configure IP address                                       |
| config-if     | label-switching                                       | Enable mpls label switching                                |
| config-if     | enable-ldp ipv4                                       | Configure LDP a the transport protocol                     |
| config        | interface po1                                         | Configure port channel interface                           |
| config-if     | switchport                                            | Make the port as layer2                                    |
| config        | interface e01                                         | Configure the attachmet circuit interface                  |
| config-if     | switchport                                            | Make the port as layer2                                    |
| config-if     | channel-group 1 mode active                           | Make this part of the port channel                         |
| config-if     | interface po1                                         | Switch to port channel mode                                |
| config        | router ospf 1                                         | Enable ospf                                                |
| config-router | network 120.1.1.1/24 area 0                           | Attach the interface over which ospf has to run            |
| config-router | network 130.1.1.1/24 area 0                           | Attach the interface over which ospf has to run            |
| config        | router-ldp                                            | Switch to router LDP mode                                  |
| config-router | targetted-peer ipv4 30.30.30.30                       | Configure the PE3 as one Targetted peer                    |
| config-router | targetted-peer ipv4 60.60.60.60                       | Configure the PE4 as Targetted peer                        |
| config        | mpls layer2-circuit t1 100 30.30.30.30                | Create a MPLS layer2 circuit with VCID 100 towards PE3     |
| config        | mpls layer2-circuit t2 110 60.60.60.60                | Create a MPLS layer2 circuit with VCID 110 towards PE4     |
| config        | service-template sv1                                  | Create a service template for matching the ingress traffic |
| config-svc    | match-all                                             | Create the match criteria                                  |
| config        | interface p0                                          | Configure port channel interface mode                      |
| config-if     | mpls-l2-circuit t1 100 service-template sv1           | Attach the VCID 100 as primary to portchannel              |
| config        | mpls-l2-circuit t1 110 service-template sv1 secondary | Attach the VCID 110 as secondary to the portchannel        |

​	