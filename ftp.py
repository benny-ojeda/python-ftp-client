import os
import sys
from ftplib import FTP
import ftplib
import argparse
import getpass

parser = argparse.ArgumentParser(description='FTP Client.')
parser.add_argument('ftp_server')
args = parser.parse_args()

def cli(prompt, reminder='Please type a valid command'):
    command = [
                'help',
                'ls', 
                'pwd', 
                'cd', 
                'get', 
                'send', 
                'mkdir', 
                'rmdir', 
                'delete', 
                'size', 
                'debug',
                'clear'
                ]

    while True:
        cmd = input(prompt)
        try:
            if cmd == command[0]:
                print("""
cd          debug           delete          get         ls
mkdir       pwd             rmdir           send        size
""")
            if cmd == command[1]:
                ftp.dir()
            if cmd == command[2]:
                print(ftp.pwd())
            if cmd.split(' ', 1)[0] == command[3]:
                dirname = cmd.split(' ', 1)[1]
                print(ftp.cwd(dirname))
            if cmd.split(' ', 1)[0] == command[4]:
                filename = cmd.split(' ', 1)[1]
                print(ftp.retrbinary("RETR " + filename, open(str(filename), 'wb').write))
            if cmd.split(' ', 1)[0] == command[5]:
                filename = cmd.split(' ', 1)[1]
                print(ftp.storbinary("STOR " + filename, open(filename, 'rb'), callback=None))
            if cmd.split(' ', 1)[0] == command[6]:
                dirname = cmd.split(' ', 1)[1]
                print(ftp.mkd(dirname))
            if cmd.split(' ', 1)[0] == command[7]:
                dirname = cmd.split(' ', 1)[1]
                print(ftp.rmd(dirname))
            if cmd.split(' ', 1)[0] == command[8]:
                filename = cmd.split(' ', 1)[1]
                print(ftp.delete(filename))
            if cmd.split(' ', 1)[0] == command[9]:
                filename = cmd.split(' ', 1)[1]
                print(ftp.size(filename))
            if cmd.split(' ', 1)[0] == command[10]:
                level = cmd.split(' ', 1)[1]
                print(ftp.set_debuglevel(int(level)))
            if cmd == command[11]:
                os.system("clear")
            if cmd in ('q', 'quit', 'exit'):
                return True
            if cmd.split(' ', 1)[0] not in command:
                print(reminder)
        except ftplib.all_errors as error:
                print('FTP error: ', error)

if args.ftp_server:
    try:
        with FTP(args.ftp_server) as ftp:
            username = input('Username (%s): ' % args.ftp_server )
            password = getpass.getpass(prompt='Password: ', stream=None)
            ftp.login(user=username, passwd=password)
            print(ftp.getwelcome())
            cli('ftp> ')
    except ftplib.all_errors as error:
        print('FTP error: ', error)