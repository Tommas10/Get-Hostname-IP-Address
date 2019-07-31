#!/usr/bin/env python

#This is small auto Python script file to get Hostname and IP address.
#This is ways to find hostname and IP address of a local machine.
#Library used – socket: This module provides access to the BSD socket interface. It is available on all modern Unix systems, Windows, MacOS, and probably additional platforms.
#Created by Tommas Huang 
#Created date: 2019-07-31

import socket 
#Importing socket library.
#Sockets are the endpoints of a bidirectional communications channel. Sockets may communicate within a process, between processes on the same machine, or between processes on different continents.
  
def get_Host_name_IP(): 
#The gethostname function retrieves the standard host name for the local computer.
    try: 
        host_name = socket.gethostname() 
        #Use socket and its gethostname() functionality. This will get the hostname of the computer where the Python interpreter is running.
        host_ip = socket.gethostbyname(host_name) 
        #gethostbyname() returns just one ip of the host even though the host  could resolve to multiple IPs from a given location.
        #The returned IP address is an IPv4 address.  
        print("Hostname :  ",host_name) 
        print("IP : ",host_ip) 
    except: 
        print("Unable to get Hostname and IP") 
    #Function to display hostname and IP address. 

get_Host_name_IP() 
#Driver code 
#Function call 
  