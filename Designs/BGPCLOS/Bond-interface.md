Create a bond interface, note the last line which enables LACP;

```text
~]#cd /etc/sysconfig/network-scripts
~]#cat ifcfg-bond1
DEVICE=bond2
TYPE=Ethernet
ONBOOT=yes
USERCTL=no
NM_CONTROLLED=no
MTU=9000
BOOTPROTO=static
IPADDR=120.1.1.2
PREFIX=24
DNS1=<DNS_IP>
BONDING_OPTS="mode=802.3ad miimon=100 lacp_rate=fast xmit_hash_policy=layer2+3"
```

Modify the two ethernet interface scripts to;

```text
~]#cat ifcfg-p0p1
DEVICE=p0p1
BOOTPROTO=none
ONBOOT=yes
SLAVE=yes
USERCTL=no
NM_CONTROLLED=no
MASTER=bond1

~]#cat ifcfg-p0p2
DEVICE=p0p2
BOOTPROTO=none
ONBOOT=yes
SLAVE=yes
USERCTL=no
NM_CONTROLLED=no
MASTER=bond1
```

Do a service network restart to enable and start the LACP on the bond interface;

```text
~]# service network restart

```

Verify if the bonded interface is up by applying command, both the individual member ports MII status should be "Up" and the main port channel MII status should be "Up"

```text
~]# cat /proc/net/bonding/bond0

Bonding Mode: IEEE 802.3ad Dynamic link aggregation
Transmit Hash Policy: layer2+3 (2)
MII Status: up
MII Polling Interval (ms): 100
Up Delay (ms): 0
Down Delay (ms): 0

802.3ad info
LACP rate: fast
Min links: 0
Aggregator selection policy (ad_select): stable
Active Aggregator Info:
  Aggregator ID: 1
  Number of ports: 1
  Actor Key: 9
  Partner Key: 500
  Partner Mac Address: <mac address>

Slave Interface: p0p1
MII Status: up
Speed: 1000 Mbps
Duplex: full
Link Failure Count: 0
Permanent HW addr: <mac address>
Aggregator ID: 1
Slave queue ID: 0

Slave Interface: p0p2
MII Status: up
Speed: 1000 Mbps
Duplex: full
Link Failure Count: 0
Permanent HW addr: <mac address>
Aggregator ID: 2
Slave queue ID: 0
```