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

def decrypt(key, filename):
    chunksize = 64*1024
    outputFile = filename[0:len(filename)-7]
    
    with open(filename, 'rb') as infile:
        filesize = long(infile.read(16))
        IV = infile.read(16)

        decryptor = AES.new(key, AES.MODE_CBC, IV)

        with open(outputFile, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)

                if len(chunk) == 0:
                    break

                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(filesize)
            


def getKey(password):
    hasher = SHA256.new(password)
    return hasher.digest()
    
                
def allfiles():
        allFiles = []
        for root, subfiles, files in os.walk(os.getcwd() + "\\dir\\"):
                for names in files:
                        allFiles.append(os.path.join(root, names))
        return allFiles

encFiles = allfiles()

def Main():
    password = raw_input("Password: ")
    for file in encFiles:
        try:
            decrypt(getKey(password), file)
            print "\n" + "Decrypted: " + file
        except ValueError:
            print "\n" + file + "   doesn't need decrypted or can't be decrypted"
        

if __name__ == '__main__':
    Main()