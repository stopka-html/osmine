
for item in os.listdir(os.getcwd()):
    if os.path.isfile(os.path.join(os.getcwd(), item)):
        print(item)
    elif os.path.isdir(os.path.join(os.getcwd(), item)):
        print(f"{item} (Папка)")
