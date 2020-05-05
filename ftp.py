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
    commands = [
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
                'debug'
                ]

    while True:
        cmd = input(prompt)
        if cmd == commands[0]:
            print("""
cd          debug           delete          get         ls
mkdir       pwd             rmdir           send        size
            """)

        if cmd == commands[1]:
            ftp.dir()
        if cmd == commands[2]:
            print(ftp.pwd())
        if cmd.split()[0] == commands[3]:
            dir = cmd.split()[1]
            print(ftp.cwd(dir))
        if cmd.split()[0] == commands[4]:
            filename = cmd.split()[1]
            print(ftp.retrbinary("RETR " + filename, open(str(filename), 'wb').write))
        if cmd.split()[0] == commands[5]:
            filename = cmd.split()[1]
            print(ftp.storbinary("STOR " + filename, open(filename, 'rb'), callback=None))
        if cmd.split()[0] == (commands[6]):
            dirname = cmd.split()[1]
            print(ftp.mkd(dirname))
        if cmd.split()[0] == (commands[7]):
            dirname = cmd.split()[1]
            print(ftp.rmd(dirname))
        if cmd.split()[0] == (commands[8]):
            filename = cmd.split()[1]
            print(ftp.delete(filename))
        if cmd.split()[0] == (commands[9]):
            filename = cmd.split()[1]
            print(ftp.size(filename))
        if cmd.split()[0] == (commands[10]):
            level = cmd.split()[1]
            print(ftp.set_debuglevel(int(level)))
        if cmd == 'clear':
            os.system("clear")

        if cmd in ('q', 'quit', 'exit'):
            return True
        if cmd.split()[0] not in commands:
            print(reminder)
        


if args.ftp_server == sys.argv[1]:
    with FTP(args.ftp_server) as ftp:
        try:
            username = input('Username (%s): ' % args.ftp_server )
            password = getpass.getpass(prompt='Password: ', stream=None)
            ftp.login(user=username, passwd=password)
            print(ftp.getwelcome())
            cli('ftp> ')
    
        except ftplib.all_errors as error:
            print('FTP error: ', error)
            cli('ftp> ')  
else:
    print("Please enter a valid argument")