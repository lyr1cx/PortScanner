# Simple Port Scanner
import sys
import socket
from datetime import datetime

#Target
if (len(sys.argv))== 2:
    target=socket.gethostbyname(sys.argv[1]) #Translating to IPv4
else:
    print('Invalid Syntax!')
    print('Syntax: python3 scanner.py <ip>')

#Fancy-Banner-Print
print('-' * 50)
print('Scanning target ' +target)
print('Time started: '+str(datetime.now()))
print('-' * 50)

try:
    for port in range(1,999):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        print('Checking port {}'.format(port)) #Printing results live, if not wanted -delete this line.
        if result == 0:
                print('Port {} is open'.format(port))
        s.close()

#Closing if Ctrl + Z
except KeyboardInterrupt:
    print('\nExiting Program.')
    sys.exit()

#Closing if not resolved
except socket.gaierror:
    print('Hostname could not be resolved.')
    sys.exit()

#Closing if cannot connect
except socket.error:
    print('Could not connect to server.')
    sys.exit()
