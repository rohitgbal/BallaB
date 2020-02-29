#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.cli import CLI
from mininet.node import UserSwitch
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:55:26 2020

@author: rgb
"""


def myNetwork():

    net = Mininet( topo=None,
                   build=False)

    info( '*** Adding controller\n' )
    c0=net.addController(name='c0', controller=RemoteController, ip="192.168.1.2", protocol='tcp',port=6634)
    #c0=net.addController(name='c0')

    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', cls=UserSwitch, inNamespace=True)
    s2 = net.addSwitch('s2', cls=UserSwitch, inNamespace=True, failMode='standalone')
    s3 = net.addSwitch('s3', cls=UserSwitch, inNamespace=True, failMode='standalone')
    s4 = net.addSwitch('s4', cls=UserSwitch, inNamespace=True)
    s5 = net.addSwitch('s5', cls=UserSwitch, inNamespace=True, failMode='standalone')
    s6 = net.addSwitch('s6', cls=UserSwitch, inNamespace=True, failMode='standalone')
    s7 = net.addSwitch('s7', cls=UserSwitch, inNamespace=True)
    s8 = net.addSwitch('s8', cls=UserSwitch, inNamespace=True, failMode='standalone')
    s9 = net.addSwitch('s9', cls=UserSwitch, inNamespace=True, failMode='standalone')
  
    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='192.168.10.1', defaultRoute='via 192.168.10.254',mac='00:00:00:00:00:01')
    h2 = net.addHost('h2', cls=Host, ip='192.168.10.2', defaultRoute='via 192.168.10.254',mac='00:00:00:00:00:02')
    h3 = net.addHost('h3', cls=Host, ip='192.168.20.1', defaultRoute='via 192.168.20.254',mac='00:00:00:00:00:03')
    h4 = net.addHost('h4', cls=Host, ip='192.168.20.2', defaultRoute='via 192.168.20.254',mac='00:00:00:00:00:04')
    h5 = net.addHost('h5', cls=Host, ip='192.168.30.1', defaultRoute='via 192.168.30.254',mac='00:00:00:00:00:05')
    h6 = net.addHost('h6', cls=Host, ip='192.168.30.2', defaultRoute='via 192.168.30.254',mac='00:00:00:00:00:06')
    h7 = net.addHost('h7', cls=Host, ip='192.168.40.1', defaultRoute='via 192.168.40.254',mac='00:00:00:00:00:07')
    h8 = net.addHost('h8', cls=Host, ip='192.168.40.2', defaultRoute='via 192.168.40.254',mac='00:00:00:00:00:08')
    h9 = net.addHost('h9', cls=Host, ip='192.168.50.1', defaultRoute='via 192.168.50.254',mac='00:00:00:00:00:09')
    h10 = net.addHost('h10', cls=Host, ip='192.168.50.2', defaultRoute='via 192.168.50.254',mac='00:00:00:00:00:10')
    h11 = net.addHost('h11', cls=Host, ip='192.168.60.1', defaultRoute='via 192.168.60.254',mac='00:00:00:00:00:11')
    h12 = net.addHost('h12', cls=Host, ip='192.168.60.2', defaultRoute='via 192.168.60.254',mac='00:00:00:00:00:12')
    s = net.addHost('s', cls=Host, ip='192.168.100.1', defaultRoute='via 192.168.100.254',mac='10:00:00:00:00:00')   
    
    info( '*** Add links\n')
    net.addLink(s1, s4)
    net.addLink(s4, s7)
    net.addLink(s7, s1)
    net.addLink(s1, s2)
    net.addLink(s1, s3)
    net.addLink(s4, s5)
    net.addLink(s4, s6)
    net.addLink(s7, s8)
    net.addLink(s7, s9)
    
    net.addLink(s2, h1)
    net.addLink(s2, h2)
    net.addLink(s3, h3)
    net.addLink(s3, h4)
    net.addLink(s5, h5)
    net.addLink(s5, h6)
    net.addLink(s6, h7)
    net.addLink(s6, h8)
    net.addLink(s8, h9)
    net.addLink(s8, h10)
    net.addLink(s9, h11)
    net.addLink(s9, h12)
    net.addLink(s4, s)



    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([c0])
    net.get('s2').start([])
    net.get('s3').start([])
    net.get('s4').start([c0])
    net.get('s5').start([])
    net.get('s6').start([])
    net.get('s7').start([c0])
    net.get('s8').start([])
    net.get('s9').start([])

    info( '*** Post configure switches and hosts\n')
    s1.cmd('ifconfig s1-eth2 192.168.10.254')
    s1.cmd('ifconfig s1-eth3 192.168.20.254')
    s4.cmd('ifconfig s4-eth3 192.168.30.254')
    s4.cmd('ifconfig s4-eth4 192.168.40.254')
    s7.cmd('ifconfig s7-eth2 192.168.50.254')
    s7.cmd('ifconfig s7-eth3 192.168.60.254')
    s4.cmd('ifconfig s4-eth5 192.168.100.254')
    
    s1.cmd('ifconfig s1 192.168.1.100')
    s4.cmd('ifconfig s4 192.168.1.101')
    s7.cmd('ifconfig s7 192.168.1.102')
    
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
