

| Mode             | Configuration                                                | Description                                           |
| ---------------- | ------------------------------------------------------------ | :---------------------------------------------------- |
| config           | hostname spine1                                              | Configures the hostname                               |
| config           | interface lo                                                 | Configure loopback interface                          |
| config-if        | ip address 20.20.20.20/32 secondary                          | Configure ip address                                  |
| config           | interface e01                                                | Configure interface connected  to Leaf1               |
| config-if        | description ** connected to Leaf1**                          | Configure interface description                       |
| config-if        | ip address 10.20.1.0/31                                      | Configure interface IP address                        |
| config           | interface e11                                                | Configure interface connected to Leaf2                |
| config-if        | description ** connected to Leaf2 **                         | Configure interface description                       |
| config-if        | ip address 11.20.1.0/31                                      | Configure interface IP address                        |
| config           | interface e21                                                | Configure interface connected to Leaf3                |
| config-if        | description ** connected to Leaf3 **                         | Configure interface description                       |
| config           | ip address 12.20.1.0/31                                      | Configure interface IP address                        |
| config           | interface e31                                                | Configure interface connected to Leaf4                |
| config-if        | description ** connected to Leaf4 **                         | Configure interface description                       |
| config           | ip address 13.20.1.0/31                                      | Configure interface IP address                        |
| config           | interface e41                                                | Configure interface connected to Leaf5                |
| config-if        | description ** connected to Leaf5 **                         | Configure interface description                       |
| config           | ip address 14.20.1.0/31                                      | Configure interface IP address                        |
| config           | interface e51                                                | Configure interface connected to Leaf6                |
| config-if        | description ** connected to Leaf6 **                         | Configure interface description                       |
| config           | ip address 15.20.1.0/31                                      | Configure interface IP address                        |
| config           | interface e61                                                | Configure interface connected to Leaf7                |
| config-if        | description ** connected to Leaf7 **                         | Configure interface description                       |
| config           | ip address 16.20.1.0/31                                      | Configure interface IP address                        |
| config           | interface e71                                                | Configure interface connected to Leaf8                |
| config-if        | description ** connected to Leaf8 **                         | Configure interface description                       |
| config           | ip address 17.20.1.0/31                                      | Configure interface IP address                        |
| config           | load-balance rtag7                                           | Configure load balance fields during hashing          |
| config           | load-balance rtag7 macro-flow                                | Configure load balance fields during hashing          |
| config           | load-balance rtag7 ipv4 dest-ipv4 src-ipv4 destl4-port srcl4-port protocol-id | Configure load balance fields during hashing          |
| config           | load-balance rtag7 ipv6 dest-ipv6 src-ipv6 destl4-port srcl4-port next-hdr | Configure load balance fields during hashing          |
| config           | load-balance rtag7 l2 dest-mac src-mac ether-type vlan       | Configure load balance fields during hashing          |
| config           | load-balance rtag7 vxlan inner-l3 dest-ip src-ip             | Configure load balance fields during hashing          |
| config           | load-balance rtag7 vxlan inner-l2 dest-mac src-mac           | Configure load balance fields during hashing          |
| config           | router bgp 64601                                             | Configure BGP with local AS number in private AS.     |
| config-router    | bgp bestpath as-path multipath-relax                         | Disable as multipath check                            |
| config-router    | bgp log-neighbor-changes                                     | Enable log neighbor changes                           |
| config-router    | max-paths ebgp 8                                             | Set max ecmp ebgp paths                               |
| config-router    | timers bgp 3 9                                               | Set bgp timers for fast convergence                   |
| config-router    | neighbor 10.20.1.0 remote-as 65500                           | Configure eBGP neighbors Leaf1                        |
| config-router    | neighbor 10.20.1.0 fall-over bfd                             | Enable BFD for BGP                                    |
| config-router    | neighbor 10.20.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates  |
| config-router    | neighbor 11.20.1.0 remote-as 65501                           | Configure eBGP neighbors Leaf2                        |
| config-router    | neighbor 11.20.1.0 fall-over bfd                             | Enable BFD for BGP                                    |
| config-router    | neighbor 11.20.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates  |
| config-router    | neighbor 12.20.1.0 remote-as 65502                           | Configure eBGP neighbors Leaf3                        |
| config-router    | neighbor 12.20.1.0 fall-over bfd                             | Enable BFD for BGP                                    |
| config-router    | neighbor 12.20.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates  |
| config-router    | neighbor 13.20.1.0 remote-as 65503                           | Configure eBGP neighbors Leaf4                        |
| config-router    | neighbor 13.20.1.0 fall-over bfd                             | Enable BFD for BGP                                    |
| config-router    | neighbor 13.20.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates  |
| config-router    | neighbor 14.20.1.0 remote-as 65504                           | Configure eBGP neighbors Leaf5                        |
| config-router    | neighbor 14.20.1.0 fall-over bfd                             | Enable BFD for BGP                                    |
| config-router    | neighbor 14.20.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates  |
| config-router    | neighbor 15.20.1.0 remote-as 65505                           | Configure eBGP neighbors Leaf6                        |
| config-router    | neighbor 15.20.1.0 fall-over bfd                             | Enable BFD for BGP                                    |
| config-router    | neighbor 15.20.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates  |
| config-router    | neighbor 16.20.1.0 remote-as 65506                           | Configure eBGP neighbors Leaf7                        |
| config-router    | neighbor 16.20.1.0 fall-over bfd                             | Enable BFD for BGP                                    |
| config-router    | neighbor 16.20.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates  |
| config-router    | neighbor 17.20.1.0 remote-as 65507                           | Configure eBGP neighbors Leaf8                        |
| config-router    | neighbor 17.20.1.0 fall-over bfd                             | Enable BFD for BGP                                    |
| config-router    | neighbor 17.20.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updatesu |
| config-router    | address-family l2vpn evpn                                    | Configure address family for EVPN                     |
| config-router-af | neighbor  10.20.1.0 activate                                 | Activate BGP neighbor                                 |
| config-router-af | neighbor  11.20.1.0 activate                                 | Activate BGP neighbor                                 |
| config-router-af | neighbor  12.20.1.0 activate                                 | Activate BGP neighbor                                 |
| config-router-af | neighbor  13.20.1.0 activate                                 | Activate BGP neighbor                                 |
| config-router-af | neighbor  14.20.1.0 activate                                 | Activate BGP neighbor                                 |
| config-router-af | neighbor  15.20.1.0 activate                                 | Activate BGP neighbor                                 |
| config-router-af | neighbor  16.20.1.0 activate                                 | Activate BGP neighbor                                 |
| config-router-af | neighbor  17.20.1.0 activate                                 | Activate BGP neighbor                                 |

