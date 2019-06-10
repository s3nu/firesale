# Phone Number Lookup Tool
import re , sys
import urllib.request

#BYTE CONTROL
def encodeString(string) : return string.encode('utf-8')
def decodeString(string) : return string.decode('utf-8')

def action(msg)    : print('[#] - ' + msg)
def alert(msg)     : print('[+] - ' + msg)
def error(msg)     : print('[!] - ' + msg)
def errorExit(msg) : raise SystemExit('[!] - ' + msg)

#GET BETWEEN
def getBetween(source, start, stop):
    """
    """
    search = encodeString(start + '(.*?)' + stop)
    data   = re.compile(search).search(source)
    if data:
        found = decodeString(data.group(1))
        return found.replace('\n', '')
    else:
        return False

#GET CARRIER
def getCarrier(number):
    """
    """
    source   = urllib.request.urlopen('http://www.fonefinder.net/findome.php?npa=' + number[:3] + '&nxx=' + number[3:6] + '&thoublock=' + number[6:]).read()
    carrier  = getBetween(source, '</A><TD><A HREF=\'http://fonefinder.net/', '\'>')
    if carrier == 'att.php':
        alert('Carrier : AT&T')
        alert('SMS Gateway : ' + number + '@txt.att.net')
    elif carrier == 'metropcs.php':
        alert('Carrier : Metro PCS')
        alert('SMS Gateway : ' + number + '@mymetropcs.com')
    elif carrier == 'sprint.php':
        alert('Carrier : Sprint')
        alert('SMS Gateway : ' + number + '@messaging.sprintpcs.com')
    elif carrier == 'tmobile.php':
        alert('Carrier : T-Mobile')
        alert('SMS Gateway : ' + number + '@tmomail.net')
    elif carrier == 'verizon.php':
        alert('Carrier : Verizon')
        alert('SMS Gateway : ' + number + '@vtext.com')
    else:
        errorExit('Carrier : Unknown')
        errorExit('SMS Gateway : Unknown')

#VERIFY PHONE
def verifyPhone(number):
    if len(number) == 10 and number.isdigit() == True:
        return True
    else:
        return False

#VERSION CHECK
def versionCheck():
    if sys.version_info.major != 3 or sys.version_info.minor != 3:
        errorExit('Requires Python version 3.3 to be installed.')

#START
if len(sys.argv) != 2:
    error('Missing command line arguments!')
    errorExit('Usage : phonetrak.py <number>')
number = sys.argv[1]
if verifyPhone(number) == True:
    try:
        getCarrier(number)
    except:
        errorExit('Failed to retrieve carrier!')
else:
    error('Invalid phone number!')
    errorExit('Usage : phonetrak.py <number>')