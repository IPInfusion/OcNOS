

| Mode          | Configuration                          | Description                                                  |
| ------------- | -------------------------------------- | :----------------------------------------------------------- |
| config        | hostname PE4                           | Configures the hostname                                      |
| config        | interface l0                           | Configure interface loopback                                 |
| config-if     | ip address 40.40.40.40/32 secondary    | Configures IP address for loopback                           |
| config        | router ldp                             | Configure LDP                                                |
| config-router | targetted-peer ipv4 10.10.10.10        | Configure the targetted peer on PE-4                         |
| config        | interface e02                          | Confiure the interface connected to P2                       |
| config-if     | ip address 140.1.1.2/24                | Configure IP address                                         |
| config-if     | label-switching                        | Enable mpls label switching                                  |
| config-if     | enabled ldp-ipv4                       | Enable LDP protocol                                          |
| config        | router ospf 1                          | Enable ospf                                                  |
| config-router | network 140.1.1.2/32 area 0            | Attach the interface over which ospf has to run              |
| config        | mpls layer2-circuit t1 100 10.10.10.10 | Configure mpls layer2 circuit with VC ID as 100              |
| config        | service-template s1                    | Create a service template                                    |
| config-svc    | match all                              | Allow all tagged, untagged traffic types                     |
| config        | interface e01                          | Configure the attachmet circuit interface                    |
| config-if     | switchport                             | Make the port as layer2                                      |
| config-if     | mpls-l2-circuit t1 serice-template s1  | Bind the layer2 port with the VC configured and the service template |
|               |                                        |                                                              |

