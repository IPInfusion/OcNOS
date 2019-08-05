

| Mode          | Configuration                                                | Description                                          |
| ------------- | ------------------------------------------------------------ | :--------------------------------------------------- |
| config        | hostname leaf5                                               | Configures the hostname                              |
| config        | interface l0                                                 | Configure interface loopback                         |
| config-if     | ip address 14.14.14.14                                       | Configure IP address                                 |
| config        | interface e41                                                | Configure interface connected  to Spine1             |
| config-if     | description ** connected to spine1**                         | Configure interface description                      |
| config-if     | ip address 14.20.1.1/31                                      | Configure interface IP address                       |
| config        | interface e42                                                | Configure interface connected to Spine2              |
| config-if     | description ** connected to spine2 **                        | Configure interface description                      |
| config-if     | ip address 14.21.1.1/31                                      | Configure interface IP address                       |
| config        | interface e43                                                | Configure interface connected to Spine3              |
| config-if     | description ** connected to spine3 **                        | Configure interface description                      |
| config        | ip address 14.22.1.1/31                                      | Configure interface IP address                       |
| config        | interface e44                                                | Configure interface connected to Spine4              |
| config-if     | description ** connected to spine4 **                        | Configure interface description                      |
| config        | ip address 14.23.1.1/31                                      | Configure interface IP address                       |
| config        | load-balance rtag7                                           | Configure load balance fields during hashing         |
| config        | load-balance rtag7 macro-flow                                | Configure load balance fields during hashing         |
| config        | load-balance rtag7 ipv4 dest-ipv4 src-ipv4 destl4-port srcl4-port protocol-id | Configure load balance fields during hashing         |
| config        | load-balance rtag7 ipv6 dest-ipv6 src-ipv6 destl4-port srcl4-port next-hdr | Configure load balance fields during hashing         |
| config        | forwarding profile lpm-profile                               | Configure  forwarding profile                        |
| config        | router bgp 65504                                             | Configure BGP with local AS number in private AS.    |
| config-router | bgp bestpath as-path multipath-relax                         | Disable as multipath check                           |
| config-router | bgp log-neighbor-changes                                     | Enable log neighbor changes                          |
| config-router | max-paths ebgp 8                                             | Set max ecmp ebgp paths                              |
| config-router | timers bgp 3 9                                               | Set bgp timers for fast convergence                  |
| config-router | neighbor 14.20.1.0 remote-as 64601                           | Configure eBGP neighbors Spine1                      |
| config-router | neighbor 14.20.1.0 fall-over bfd                             | Enable BFD for BGP                                   |
| config-router | neighbor 14.20.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates |
| config-router | neighbor 14.21.1.0 remote-as 64601                           | Configure eBGP neighbors Spine2                      |
| config-router | neighbor 14.21.1.0 fall-over bfd                             | Enable BFD for BGP                                   |
| config-router | neighbor 14.21.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates |
| config-router | neighbor 14.22.1.0 remote-as 64601                           | Configure eBGP neighbors Spine 3                     |
| config-router | neighbor 14.22.1.0 fall-over bfd                             | Enable BFD for BGP                                   |
| config-router | neighbor 14.22.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates |
| config-router | neighbor 14.23.1.0 remote-as 64601                           | Configure eBGP neighbors Spine 4                     |
| config-router | neighbor 14.23.1.0 fall-over bfd                             | Enable BFD for BGP                                   |
| config-router | neighbor 14.23.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates |

