sudo ovs-ofctl add-flow -OOpenFlow13 tcp:192.168.1.100:6634 "in_port=2, nw_dst=192.168.20.0 action=output:3";
sudo ovs-ofctl add-flow -OOpenFlow13 tcp:192.168.1.100:6634 "in_port=3, nw_dst=192.168.10.0 action=output:2";
sudo ovs-ofctl add-flow -OOpenFlow13 tcp:192.168.1.102:6634 "in_port=2, nw_dst=192.168.60.0 action=output:3";
sudo ovs-ofctl add-flow -OOpenFlow13 tcp:192.168.1.102:6634 "in_port=3, nw_dst=192.168.50.0 action=output:2";
sudo ovs-ofctl add-flow -OOpenFlow13 tcp:192.168.1.101:6634 "in_port=3, nw_dst=192.168.30.0 action=output:2";
sudo ovs-ofctl add-flow -OOpenFlow13 tcp:192.168.1.101:6634 "in_port=2, nw_dst=192.168.40.0 action=output:3";