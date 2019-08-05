

| Mode          | Configuration                                                | Description                                          |
| ------------- | ------------------------------------------------------------ | :--------------------------------------------------- |
| config        | hostname spine2                                              | Configures the hostname                              |
| config        | interface l0                                                 | Configure interface loopback                         |
| config-if     | ip address 21.21.21.21/32                                    | Configure IP address                                 |
| config        | interface e02                                                | Configure interface connected  to Leaf1              |
| config-if     | description ** connected to Leaf1**                          | Configure interface description                      |
| config-if     | ip address 10.21.1.0/31                                      | Configure interface IP address                       |
| config        | interface e12                                                | Configure interface connected to Leaf2               |
| config-if     | description ** connected to Leaf2 **                         | Configure interface description                      |
| config-if     | ip address 11.21.1.0/31                                      | Configure interface IP address                       |
| config        | interface e22                                                | Configure interface connected to Leaf3               |
| config-if     | description ** connected to Leaf3 **                         | Configure interface description                      |
| config-if     | ip address 12.21.1.0/31                                      | Configure interface IP address                       |
| config        | interface e32                                                | Configure interface connected to Leaf4               |
| config-if     | description ** connected to Leaf4 **                         | Configure interface description                      |
| config-if     | ip address 13.21.1.0/31                                      | Configure interface IP address                       |
| config        | interface e42                                                | Configure interface connected to Leaf5               |
| config-if     | description ** connected to Leaf5 **                         | Configure interface description                      |
| config-if     | ip address 14.21.1.0/31                                      | Configure interface IP address                       |
| config        | interface e52                                                | Configure interface connected to Leaf6               |
| config-if     | description ** connected to Leaf6 **                         | Configure interface description                      |
| config-if     | ip address 15.21.1.0/31                                      | Configure interface IP address                       |
| config        | interface e62                                                | Configure interface connected to Leaf7               |
| config-if     | description ** connected to Leaf7 **                         | Configure interface description                      |
| config-if     | ip address 16.21.1.0/31                                      | Configure interface IP address                       |
| config        | interface e72                                                | Configure interface connected to Leaf8               |
| config-if     | description ** connected to Leaf8 **                         | Configure interface description                      |
| config-if     | ip address 17.21.1.0/31                                      | Configure interface IP address                       |
| config        | load-balance rtag7                                           | Configure load balance fields during hashing         |
| config        | load-balance rtag7 macro-flow                                | Configure load balance fields during hashing         |
| config        | load-balance rtag7 ipv4 dest-ipv4 src-ipv4 destl4-port srcl4-port protocol-id | Configure load balance fields during hashing         |
| config        | load-balance rtag7 ipv6 dest-ipv6 src-ipv6 destl4-port srcl4-port next-hdr | Configure load balance fields during hashing         |
| config        | forwarding profile lpm-profile                               | Configure  forwarding profile                        |
| config        | router bgp 64601                                             | Configure BGP with local AS number in private AS.    |
| config-router | bgp bestpath as-path multipath-relax                         | Disable as multipath check                           |
| config-router | bgp log-neighbor-changes                                     | Enable log neighbor changes                          |
| config-router | max-paths ebgp 8                                             | Set max ecmp ebgp paths                              |
| config-router | timers bgp 3 9                                               | Set bgp timers for fast convergence                  |
| config-router | neighbor 10.21.1.0 remote-as 65500                           | Configure eBGP neighbors Leaf1                       |
| config-router | neighbor 10.21.1.0 fall-over bfd                             | Enable BFD for BGP                                   |
| config-router | neighbor 10.21.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates |
| config-router | neighbor 11.21.1.0 remote-as 65501                           | Configure eBGP neighbors Leaf2                       |
| config-router | neighbor 11.21.1.0 fall-over bfd                             | Enable BFD for BGP                                   |
| config-router | neighbor 11.21.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates |
| config-router | neighbor 12.21.1.0 remote-as 65502                           | Configure eBGP neighbors Leaf3                       |
| config-router | neighbor 12.21.1.0 fall-over bfd                             | Enable BFD for BGP                                   |
| config-router | neighbor 12.21.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates |
| config-router | neighbor 13.21.1.0 remote-as 65503                           | Configure eBGP neighbors Leaf4                       |
| config-router | neighbor 13.21.1.0 fall-over bfd                             | Enable BFD for BGP                                   |
| config-router | neighbor 13.21.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates |
| config-router | neighbor 14.21.1.0 remote-as 65504                           | Configure eBGP neighbors Leaf5                       |
| config-router | neighbor 14.21.1.0 fall-over bfd                             | Enable BFD for BGP                                   |
| config-router | neighbor 14.21.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates |
| config-router | neighbor 15.21.1.0 remote-as 65505                           | Configure eBGP neighbors Leaf6                       |
| config-router | neighbor 15.21.1.0 fall-over bfd                             | Enable BFD for BGP                                   |
| config-router | neighbor 15.21.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates |
| config-router | neighbor 16.21.1.0 remote-as 65506                           | Configure eBGP neighbors Leaf7                       |
| config-router | neighbor 16.21.1.0 fall-over bfd                             | Enable BFD for BGP                                   |
| config-router | neighbor 16.21.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates |
| config-router | neighbor 17.21.1.0 remote-as 65507                           | Configure eBGP neighbors Leaf8                       |
| config-router | neighbor 17.21.1.0 fall-over bfd                             | Enable BFD for BGP                                   |
| config-router | neighbor 17.21.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates |


