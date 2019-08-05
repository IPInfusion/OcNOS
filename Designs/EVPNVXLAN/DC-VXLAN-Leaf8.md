

| Mode             | Configuration                                                | Description                                          |
| ---------------- | ------------------------------------------------------------ | :--------------------------------------------------- |
| config           | hostname leaf8                                               | Configures the hostname                              |
| config           | nvo vxlan enable                                             | Enable VXLAN                                         |
| config           | mac vrf vrfred                                               | Create a Mac-VRF for VXLAN                           |
| config-vrf       | rd 111:8                                                     | Create a Route Distinguisher for EVPN VXLAN routes   |
| config-vrf       | route-target both 111:1                                      | Create a Route Target for EVPN VXLAN routes          |
| config           | interface lo                                                 | Configure interface loopback                         |
| config-if        | ip address 17.17.17.17/32 secondary                          | Configure IP address                                 |
| config           | interface e71                                                | Configure interface connected  to Spine1             |
| config-if        | description ** connected to spine1**                         | Configure interface description                      |
| config-if        | ip address 17.20.1.1/31                                      | Configure interface IP address                       |
| config           | interface e72                                                | Configure interface connected to Spine2              |
| config-if        | description ** connected to spine2 **                        | Configure interface description                      |
| config-if        | ip address 17.21.1.1/31                                      | Configure interface IP address                       |
| config           | interface e73                                                | Configure interface connected to Spine3              |
| config-if        | description ** connected to spine3 **                        | Configure interface description                      |
| config           | ip address 17.22.1.1/31                                      | Configure interface IP address                       |
| config           | interface e74                                                | Configure interface connected to Spine4              |
| config-if        | description ** connected to spine4 **                        | Configure interface description                      |
| config           | ip address 17.23.1.1/31                                      | Configure interface IP address                       |
| config           | interface e75                                                | Configure interface connected to Server              |
| config-if        | switchport                                                   | Set interface to layer2 mode                         |
| config           | load-balance rtag7                                           | Configure load balance fields during hashing         |
| config           | load-balance rtag7 macro-flow                                | Configure load balance fields during hashing         |
| config           | load-balance rtag7 ipv4 dest-ipv4 src-ipv4 destl4-port srcl4-port protocol-id | Configure load balance fields during hashing         |
| config           | load-balance rtag7 ipv6 dest-ipv6 src-ipv6 destl4-port srcl4-port next-hdr | Configure load balance fields during hashing         |
| config           | load-balance rtag7 l2 dest-mac src-mac ether-type vlan       | Configure load balance fields during hashing         |
| config           | load-balance rtag7 vxlan inner-l3 dest-ip src-ip             | Configure load balance fields during hashing         |
| config           | load-balance rtag7 vxlan inner-l2 dest-mac src-mac           | Configure load balance fields during hashing         |
| config           | router bgp 65507                                             | Configure BGP with local AS number in private AS.    |
| config-router    | bgp bestpath as-path multipath-relax                         | Disable as multipath check                           |
| config-router    | bgp log-neighbor-changes                                     | Enable log neighbor changes                          |
| config-router    | max-paths ebgp 8                                             | Set max ecmp ebgp paths                              |
| config-router    | timers bgp 3 9                                               | Set bgp timers for fast convergence                  |
| config-router    | neighbor 17.20.1.0 remote-as 64601                           | Configure eBGP neighbors Spine1                      |
| config-router    | neighbor 17.20.1.0 fall-over bfd                             | Enable BFD for BGP                                   |
| config-router    | neighbor 17.20.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates |
| config-router    | neighbor 17.21.1.0 remote-as 64601                           | Configure eBGP neighbors Spine2                      |
| config-router    | neighbor 17.21.1.0 fall-over bfd                             | Enable BFD for BGP                                   |
| config-router    | neighbor 17.21.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates |
| config-router    | neighbor 17.22.1.0 remote-as 64601                           | Configure eBGP neighbors Spine 3                     |
| config-router    | neighbor 17.22.1.0 fall-over bfd                             | Enable BFD for BGP                                   |
| config-router    | neighbor 17.22.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates |
| config-router    | neighbor 17.23.1.0 remote-as 64601                           | Configure eBGP neighbors Spine 4                     |
| config-router    | neighbor 17.23.1.0 fall-over bfd                             | Enable BFD for BGP                                   |
| config-router    | neighbor 17.23.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates |
| config-router    | address-family l2vpn evpn                                    | Configure address family for EVPN                    |
| config-router-af | neighbor 17.20.1.0 activate                                  | Activate BGP neighbor                                |
| config-router-af | neighbor 17.21.1.0 activate                                  | Activate BGP neighbor                                |
| config-router-af | neighbor 17.22.1.0 activate                                  | Activate BGP neighbor                                |
| config-router-af | neighbor 17.23.1.0 activate                                  | Activate BGP neighbor                                |
| config           | nvo vxlan vtep-ip-global 17.17.17.17                         | Configure VTEP global IP address                     |
| config           | nvo vxlan id 65 ingress-replication inner-vid-disabled       | Configure VNID                                       |
| config-vxlan     | vxlan host-reachability-protocol evpn-bgp vrfred             | Associate MAC VRF with VNID                          |
| config-vxlan     | nvo vxlan access-if port-vlan e75 65                         | Bind VNID with VXLAN access port                     |
| config-vxlan     | map vnid 65                                                  | Map the VNID with access interface                   |

