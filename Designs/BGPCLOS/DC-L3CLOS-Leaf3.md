

| Mode          | Configuration                                                | Description                                          |
| ------------- | ------------------------------------------------------------ | :--------------------------------------------------- |
| config        | hostname leaf3                                               | Configures the hostname                              |
| config        | interface l0                                                 | Configure interface loopback                         |
| config-if     | ip address 12.12.12.12                                       | Configure IP address                                 |
| config        | interface e21                                                | Configure interface connected  to Spine1             |
| config-if     | description ** connected to spine1**                         | Configure interface description                      |
| config-if     | ip address 12.20.1.1/31                                      | Configure interface IP address                       |
| config        | interface e22                                                | Configure interface connected to Spine2              |
| config-if     | description ** connected to spine2 **                        | Configure interface description                      |
| config-if     | ip address 12.21.1.1/31                                      | Configure interface IP address                       |
| config        | interface e23                                                | Configure interface connected to Spine3              |
| config-if     | description ** connected to spine3 **                        | Configure interface description                      |
| config        | ip address 12.22.1.1/31                                      | Configure interface IP address                       |
| config        | interface e24                                                | Configure interface connected to Spine4              |
| config-if     | description ** connected to spine4 **                        | Configure interface description                      |
| config        | ip address 12.23.1.1/31                                      | Configure interface IP address                       |
| config        | load-balance rtag7                                           | Configure load balance fields during hashing         |
| config        | load-balance rtag7 macro-flow                                | Configure load balance fields during hashing         |
| config        | load-balance rtag7 ipv4 dest-ipv4 src-ipv4 destl4-port srcl4-port protocol-id | Configure load balance fields during hashing         |
| config        | load-balance rtag7 ipv6 dest-ipv6 src-ipv6 destl4-port srcl4-port next-hdr | Configure load balance fields during hashing         |
| config        | forwarding profile lpm-profile                               | Configure  forwarding profile                        |
| config        | router bgp 65502                                             | Configure BGP with local AS number in private AS.    |
| config-router | bgp bestpath as-path multipath-relax                         | Disable as multipath check                           |
| config-router | bgp log-neighbor-changes                                     | Enable log neighbor changes                          |
| config-router | max-paths ebgp 8                                             | Set max ecmp ebgp paths                              |
| config-router | timers bgp 3 9                                               | Set bgp timers for fast convergence                  |
| config-router | neighbor 12.20.1.0 remote-as 64601                           | Configure eBGP neighbors Spine1                      |
| config-router | neighbor 12.20.1.0 fall-over bfd                             | Enable BFD for BGP                                   |
| config-router | neighbor 12.20.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates |
| config-router | neighbor 12.21.1.0 remote-as 64601                           | Configure eBGP neighbors Spine2                      |
| config-router | neighbor 12.21.1.0 fall-over bfd                             | Enable BFD for BGP                                   |
| config-router | neighbor 12.21.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates |
| config-router | neighbor 12.22.1.0 remote-as 64601                           | Configure eBGP neighbors Spine 3                     |
| config-router | neighbor 12.22.1.0 fall-over bfd                             | Enable BFD for BGP                                   |
| config-router | neighbor 12.22.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates |
| config-router | neighbor 12.23.1.0 remote-as 64601                           | Configure eBGP neighbors Spine 4                     |
| config-router | neighbor 12.23.1.0 fall-over bfd                             | Enable BFD for BGP                                   |
| config-router | neighbor 12.23.1.0 advertisement-interval 0                  | Set advertisement interval to zero for quick updates |

