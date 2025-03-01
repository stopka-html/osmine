inp = ['test']
import requests
import global_var
def update():
    print(inp[0])
def install():
    print(inp[0])
def remove():
    print(inp[0])

def main():
    if inp[0] == 'update':
        update()
    if len(inp) > 1:
        if inp[0] == 'install':
            install(inp[1:])
        elif inp[0] == 'remove':
            remove(inp[1:])