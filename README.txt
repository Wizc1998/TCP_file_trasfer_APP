Weizi Cai
cai.590@OSU.EDU

CSE 3461 LAB2
TCP socket file transfer

This is the README file

by submitting this file, I certify that all contained files are my original work

To use my program:

1. open cmd window, make sure you have python 
2. run command:
python3 ftps.py <local-port-on-gamma>

3. Then, startftpc.pyonbeta.cse.ohio-state.eduwith the command:
python3 ftpc.py <remote-IP-on-gamma> <remote-port-on-gamma> <local-file-to-transfer>

The ftpc.py client will send all bytes of that local file. 
The ftps.py server should receive the file and then store it.

the program will transfer the file, report length, connection information, and do a checksum
to make sure everything went right

the transfered file will be stored into a new folder in this same directory 
