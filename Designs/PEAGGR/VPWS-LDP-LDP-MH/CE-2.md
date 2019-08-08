

| Mode            | Configuration                       | Description                                                  |
| --------------- | ----------------------------------- | :----------------------------------------------------------- |
| config          | hostname CE-2                 | Configures the hostname                                      |
| config          | interface p01                  | Configure interface port channel          |
| config-if | switchport | Make the portchannel  as Layer2 |
| config          | interface E01                   | Configure interface                                 |
| config-if | switchport | Make the port as Layer2 |
| config-if | channel-group 1 mode active | Add this part of a port channel |
| config | interface E04 | Configure interface |
| config-if | switchport | Make the port as Layer2 |
| config-if | channel-group 1 mode active | Add this part of a port channel |



