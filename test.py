
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

command.sort()
print(*command[0:6], sep='\t')
print(*command[6:12], sep='\t')