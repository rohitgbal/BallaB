#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 12:04:09 2020

@author: rgb
"""

import os
import subprocess
out = subprocess.Popen(['sudo', 'ovs-vsctl', 'list-br'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT);
folder='switch/'
stdout,stderr = out.communicate()
if (stdout !=''):
    switches=stdout.split()
    for switch in switches:
        ovsswitch = subprocess.Popen(['sudo', 'ovs-vsctl', 'get-controller', switch],stdout=subprocess.PIPE,stderr=subprocess.STDOUT);
        stdout,stderr = ovsswitch.communicate()
        #print (stdout)
        if(stdout!= ''):
            #print(switch)
            sfolder=folder+switch
            os.mkdir(sfolder)
            ovsport = subprocess.Popen(['sudo', 'ovs-vsctl', 'list-ports', switch],stdout=subprocess.PIPE,stderr=subprocess.STDOUT);
            stdout,stderr = ovsport.communicate()
            ports=stdout.split()
            for port in ports:
                pfolder=sfolder+'/'+port
                os.mkdir(pfolder)
                
            #for port in ports:
                #print (port)
        else:
            print("No OVS configured in network")
else:
    print("No Network in mininet")
        #print ('Switches {} ={}'.format(i,switch))
        #i=i+1;