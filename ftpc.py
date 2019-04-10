# cse3461 lab2
# Weizi Cai (cai.590)
# Instructor: Angel Rivera


#client program

import socket
import os
import sys

# 1. get and store target server IP and Port

server_IP = str(sys.argv[1])
server_Port = int(sys.argv[2])

# 2. make a socket(combination of IP and Port) to achieve our low level server
# note: in the future if we use a larger network framework, we should use socketserver instead
# socket.socket([family[, type[, proto]]])

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.connect((server_IP, server_Port))

# 3. get the filename to transfer

filename =str(sys.argv[3])
#only read in binary, so rb
file = open(filename, 'rb')


# 1 
# first 4 bytes (in network byte order) will contain the number of bytes in the file to follow

countStr = str(os.stat(filename).st_size)    # send it encoded in utf-8

if(len(countStr) < 4):
    while len(countStr) != 4:
        countStr +=' '    
elif(len(str(countStr)) > 4):
    countStr = countStr[0:4]
        
sock.sendall(countStr.encode('utf-8'))   # learning note: sendall() method: sends the entire buffer you pass

# 2 
# The next 20 bytes will contain the name ofthe file (assume the name fits in 20 bytes)

if(len(filename) < 20):
    while len(filename) != 20:
        filename +=' '  
        
elif(len(filename)>20):
    filename = filename[0:20]
    
sock.sendall(filename.encode('utf-8'))     # send it encoded in utf-8 

# 3
# loop through file and send each 1000 byte size data

while True:         # note: keep loop till break
    piece = file.read(1000)
    if piece == b'':
        break
    sock.sendall(piece)

print("transfer success!")

sock.close()
file.close()

