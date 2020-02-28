#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,build=False)


    info( '*** Adding controller\n' )
    c0=net.addController(name='c0', controller=RemoteController, ip="192.168.1.2", protocol='tcp',port=6633)
    c1=net.addController(name='c1', controller=RemoteController, ip="192.168.1.2", protocol='tcp',port=6634)


    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch)
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch)
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch)
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch)
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch)
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch)
    
    s11 = net.addSwitch('s11', cls=OVSKernelSwitch, failMode='standalone')
    s22 = net.addSwitch('s22', cls=OVSKernelSwitch, failMode='standalone')
    s33 = net.addSwitch('s33', cls=OVSKernelSwitch, failMode='standalone')
    s44 = net.addSwitch('s44', cls=OVSKernelSwitch, failMode='standalone')
    s55 = net.addSwitch('s55', cls=OVSKernelSwitch, failMode='standalone')
    s66 = net.addSwitch('s66', cls=OVSKernelSwitch, failMode='standalone')

    
    info( '*** Add hosts\n')
    h6 = net.addHost('h6', cls=Host, ip='60.0.0.100', defaultRoute='60.0.0.1')
    h5 = net.addHost('h5', cls=Host, ip='50.0.0.100', defaultRoute='50.0.0.1')
    h4 = net.addHost('h4', cls=Host, ip='40.0.0.100', defaultRoute='40.0.0.1')
    h3 = net.addHost('h3', cls=Host, ip='30.0.0.100', defaultRoute='30.0.0.1')
    h2 = net.addHost('h2', cls=Host, ip='20.0.0.100', defaultRoute='20.0.0.1')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.100', defaultRoute='10.0.0.1')


    info( '*** Add links\n')
    s11h1 = {'bw':10}
    s22h2 = {'bw':10}
    s33h3 = {'bw':10}
    
    s11s1 = {'bw':10}
    s22s2 = {'bw':10}
    s33s3 = {'bw':10}
    
    net.addLink(s11, h1, cls=TCLink , **s11h1)
    net.addLink(s22, h2, cls=TCLink , **s22h2)
    net.addLink(s33, h3, cls=TCLink , **s33h3)
    
    net.addLink(s11, s1, cls=TCLink , **s11s1)
    net.addLink(s22, s2, cls=TCLink , **s22s2)
    net.addLink(s33, s3, cls=TCLink , **s33s3)
    
    s44h4 = {'bw':10}
    s55h5 = {'bw':10}
    s66h6 = {'bw':10}
    
    s44s4 = {'bw':10}
    s55s5 = {'bw':10}
    s66s6 = {'bw':10}
    
    net.addLink(s44, h4, cls=TCLink , **s44h4)
    net.addLink(s55, h5, cls=TCLink , **s55h5)
    net.addLink(s66, h6, cls=TCLink , **s66h6)
    
    net.addLink(s44, s4, cls=TCLink , **s44s4)
    net.addLink(s55, s5, cls=TCLink , **s55s5)
    net.addLink(s66, s6, cls=TCLink , **s66s6)
    
    s1s2 = {'bw':1,'delay':'1','loss':5,'max_queue_size':100,'jitter':'11','speedup':10}
    s1s3 = {'bw':1,'delay':'1','loss':5,'max_queue_size':100,'jitter':'11','speedup':10}
    s3s2 = {'bw':1,'delay':'1','loss':5,'max_queue_size':100,'jitter':'11','speedup':10}
    net.addLink(s1, s2, cls=TCLink , **s1s2)
    net.addLink(s1, s3, cls=TCLink , **s1s3)
    net.addLink(s3, s2, cls=TCLink , **s3s2)
    
    s4s5 = {'bw':1,'delay':'1','loss':5,'max_queue_size':100,'jitter':'11','speedup':10}
    s4s6 = {'bw':1,'delay':'1','loss':5,'max_queue_size':100,'jitter':'11','speedup':10}
    s6s5 = {'bw':1,'delay':'1','loss':5,'max_queue_size':100,'jitter':'11','speedup':10}
    net.addLink(s4, s5, cls=TCLink , **s4s5)
    net.addLink(s4, s6, cls=TCLink , **s4s6)
    net.addLink(s6, s5, cls=TCLink , **s6s5)
    
    s1s4 = {'bw':100,'delay':'1','loss':5,'max_queue_size':10,'jitter':'1','speedup':10}
    s2s5 = {'bw':100,'delay':'1','loss':5,'max_queue_size':10,'jitter':'1','speedup':10}
    s3s6 = {'bw':100,'delay':'1','loss':5,'max_queue_size':10,'jitter':'1','speedup':10}
    net.addLink(s1, s4, cls=TCLink , **s1s4)
    net.addLink(s2, s5, cls=TCLink , **s2s5)
    net.addLink(s3, s6, cls=TCLink , **s4s6)
    
    
    
    
    s1.cmd('ifconfig s1-eth1 10.0.0.1 up')
    s2.cmd('ifconfig s2-eth1 20.0.0.1 up')
    s3.cmd('ifconfig s3-eth1 30.0.0.1 up')
    s4.cmd('ifconfig s4-eth1 40.0.0.1 up')
    s5.cmd('ifconfig s5-eth1 50.0.0.1 up')
    s6.cmd('ifconfig s6-eth1 60.0.0.1 up')
    
    s1.cmd('ifconfig s1-eth2 1.0.0.1/30 up')
    s2.cmd('ifconfig s2-eth2 1.0.0.2/30 up')
    s3.cmd('ifconfig s3-eth2 2.0.0.2/30 up')
    s4.cmd('ifconfig s4-eth2 4.0.0.1/30 up')
    s5.cmd('ifconfig s5-eth2 4.0.0.2/30 up')
    s6.cmd('ifconfig s6-eth2 5.0.0.2/30 up')
    
    s1.cmd('ifconfig s1-eth3 2.50.0.1/30 up')
    s2.cmd('ifconfig s2-eth3 3.0.0.1/30 up')
    s3.cmd('ifconfig s3-eth3 3.0.0.2/30 up')
    s4.cmd('ifconfig s4-eth3 5.0.0.1/30 up')
    s5.cmd('ifconfig s5-eth3 6.0.0.1/30 up')
    s6.cmd('ifconfig s6-eth3 6.0.0.2/30 up')
    
    s1.cmd('ifconfig s1-eth4 11.0.0.1/30 up')
    s2.cmd('ifconfig s2-eth4 12.0.0.1/30 up')
    s3.cmd('ifconfig s3-eth4 13.0.0.1/30 up')
    s4.cmd('ifconfig s4-eth4 11.0.0.2/30 up')
    s5.cmd('ifconfig s5-eth4 12.0.0.2/30 up')
    s6.cmd('ifconfig s6-eth4 13.0.0.2/30 up')
    
    
        
    info( '*** Starting network\n')
    net.build()


    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([c0])
    net.get('s2').start([c0])
    net.get('s3').start([c0])
    net.get('s4').start([c1])
    net.get('s5').start([c1])
    net.get('s6').start([c1])

    info( '*** Post configure switches and hosts\n')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()