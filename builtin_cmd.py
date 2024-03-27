import global_var
import os
def exit(nth):
    
    global_var.running = False
    print('done')

def echo(inp):
    print(*inp)

def ls(inp):
    for item in os.listdir(os.getcwd()):
        if os.path.isfile(os.path.join(os.getcwd(), item)):
            print(item)
        elif os.path.isdir(os.path.join(os.getcwd(), item)):
            print(f"{item} (Папка)")

def cd(inp):
    if inp[0] == '..':
        os.chdir('..')
    else:
        os.chdir(os.getcwd() +'/'+inp[0])
def mkdir(inp):
    os.mkdir(inp[0])
def rm(inp):
    os.remove(inp[0])
def rmdir(inp):
    os.rmdir(inp[0])

def neofetch(inp):
    print(global_var.os_name,global_var.os_version)