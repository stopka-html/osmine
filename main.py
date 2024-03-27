from command_list import *
import os
import builtin_cmd
import global_var
class OS:
    os_name = 'OSMINE'
    os_vers = 'test_build'
    def __init__(self, mode='deafult'):
        self.startup_mode = mode
        print('Welcome to the OSMINE')
        global_var.running = True
        self.bash()
    def bash(self):
        while global_var.running:
            print(os.getcwd(),'>',end='')
            inp = list(input().split())
            if inp[0] not in list_of_commands:
                print('command not found')
            else:
                func = getattr(builtin_cmd,inp[0])
                func(inp[1::])
if __name__ == "__main__":
    
    smth = OS()