# cse3461 lab2
# Weizi Cai (cai.590)
# Instructor: Angel Rivera

#server program

import socket
import os
import sys
import hashlib


# 1. get and store incoming Port, we just need the unviversal IP for this computer

server_IP = ''
print(server_IP)
server_Port =int(sys.argv[1])


rec_dir = "receive_data/"    # create a folder to store it

if not os.path.exists(rec_dir):
    os.makedirs(rec_dir)
    
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM, 0)
serverSocket.bind((server_IP, server_Port))

serverSocket.listen(1)      # set the max socket number you can have before end

(clientSocket, address) = serverSocket.accept()   # clientSocket is a new serverSocket object usable to send and receive data on the clientSocket, 
                                    # and address is the address bound to the serverSocketet on the other end of the clientSocketection.

print("established the clientSocketection with ", address)

# now we ready to receive things

# get the file size, 4 bytes
size = clientSocket.recv(4)
print("file size is", size.decode('utf-8'))

# get the filename, 20 bytes
name = clientSocket.recv(20)

filename = name.decode('utf-8')

print("the received file name is ", filename)

file = open(rec_dir+filename.strip(), 'wb')            #write in binary


while True:
    piece = clientSocket.recv(1000)
    if piece == b'':
        break
    file.write(piece)
    
    
    
clientSocket.close()
file.close()
# Use md5sum to ensure that the transferred file is the same as the original one.


old_file = open(filename.strip(),'rb')
new_file = open(rec_dir + filename.strip(),'rb')

old_hash = hashlib.md5()
new_hash = hashlib.md5()

chunksize = 1000
while True:
    old_data = old_file.read(chunksize)
    new_data = new_file.read(chunksize)
    if old_data:
        old_hash.update(old_data)
        new_hash.update(new_data)

    else:
        break

print("The uploaded file is same as original file: " + str(old_hash.hexdigest() == new_hash.hexdigest()))


old_file.close()
new_file.close()
