#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:55:26 2020

@author: rgb
"""

from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False)

    info( '*** Adding controller\n' )
    #c0=net.addController(name='c0', controller=RemoteController, ip="192.168.1.2", protocol='tcp',port=6633)
    c0=net.addController(name='c0')

    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s11 = net.addSwitch('s11', cls=OVSKernelSwitch, failMode='standalone')
    s12 = net.addSwitch('s12', cls=OVSKernelSwitch, failMode='standalone')
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s21 = net.addSwitch('s21', cls=OVSKernelSwitch, failMode='standalone')
    s22 = net.addSwitch('s22', cls=OVSKernelSwitch, failMode='standalone')
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s31 = net.addSwitch('s31', cls=OVSKernelSwitch, failMode='standalone')
    s32 = net.addSwitch('s32', cls=OVSKernelSwitch, failMode='standalone')
    
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
    h10 = net.addHost('h10', cls=Host, ip='192.168.50.2', defaultRoute='via 192.168.50.254',mac='00:00:00:00:00:0A')
    h11 = net.addHost('h11', cls=Host, ip='192.168.60.1', defaultRoute='via 192.168.60.254',mac='00:00:00:00:00:0B')
    h12 = net.addHost('h12', cls=Host, ip='192.168.60.2', defaultRoute='via 192.168.60.254',mac='00:00:00:00:00:0C')
    
    
    info( '*** Add links\n')
    net.addLink(s1, s2)
    net.addLink(s3, s2)

    net.addLink(s1, s11)
    net.addLink(s1, s12)
    net.addLink(s2, s21)
    net.addLink(s2, s22)
    net.addLink(s3, s31)
    net.addLink(s3, s32)
    
    net.addLink(s11, h1)
    net.addLink(s11, h2)
    net.addLink(s12, h3)
    net.addLink(s12, h4)
    net.addLink(s21, h5)
    net.addLink(s21, h6)
    net.addLink(s22, h7)
    net.addLink(s22, h8)
    net.addLink(s31, h9)
    net.addLink(s31, h10)
    net.addLink(s32, h11)
    net.addLink(s32, h12)



    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([c0])
    net.get('s11').start([])
    net.get('s12').start([])
    net.get('s2').start([c0])
    net.get('s21').start([])
    net.get('s22').start([])
    net.get('s3').start([c0])
    net.get('s31').start([])
    net.get('s32').start([])

    info( '*** Post configure switches and hosts\n')
    s1.cmd('ifconfig s1-eth1 192.168.100.1', mac='10:00:00:00:00:01')
    s1.cmd('ifconfig s1-eth2 192.168.10.254', mac='10:00:00:00:00:02')
    s1.cmd('ifconfig s1-eth3 192.168.20.254', mac='10:00:00:00:00:03')
    s2.cmd('ifconfig s2-eth1 192.168.100.2', mac='20:00:00:00:00:01')   
    s2.cmd('ifconfig s2-eth2 192.168.200.1', mac='20:00:00:00:00:02')
    s2.cmd('ifconfig s2-eth3 192.168.30.254', mac='20:00:00:00:00:03')
    s2.cmd('ifconfig s2-eth4 192.168.40.254', mac='20:00:00:00:00:04')
    s3.cmd('ifconfig s3-eth3 192.168.200.2', mac='30:00:00:00:00:01')
    s3.cmd('ifconfig s3-eth3 192.168.50.254', mac='30:00:00:00:00:02')
    s3.cmd('ifconfig s3-eth3 192.168.60.254', mac='30:00:00:00:00:03')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()
