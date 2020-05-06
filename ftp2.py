import os
import sys
from ftplib import FTP
import ftplib
import argparse
import getpass


parser = argparse.ArgumentParser(description='FTP Client.')
parser.add_argument('ftp_server')
args = parser.parse_args()

if args.ftp_server == sys.argv[1]:
    with FTP(args.ftp_server) as ftp:
        username = input('Username (%s): ' % args.ftp_server )
        password = getpass.getpass(prompt='Password: ', stream=None)
        ftp.login(user=username, passwd=password)
        print(ftp.getwelcome())


def ls():
    print(str(ftp.dir()))


while True:
    cmd = input('ftp> ')

    if cmd == 'ls':
        ls()
    
