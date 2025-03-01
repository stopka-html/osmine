import json
list_of_commands = {}

def load():
    with open('registered.json', 'r') as f:
        return json.load(f)
def register(name, path):
    list_of_commands[name] = path
    with open('registered.json', 'w') as f:
        json.dump(list_of_commands, f)
list_of_commands = load()
print(list_of_commands)