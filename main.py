from bin.command_list import *
import os
import update
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
            print(os.getcwd()+'>',end='')
            inp = list(input().split())
            print(list_of_commands)
            if inp[0] not in list_of_commands:
                print('command not found')
            else:
                with open(f'{list_of_commands[inp[0]]}', 'r') as f:
                    exec("inp.pop(0) \n"+f.read())
if __name__ == "__main__":   
    smth = OS()