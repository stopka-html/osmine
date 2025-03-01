if inp[0] == '..':
    os.chdir('..')
else:
    os.chdir(os.getcwd() +'/'+inp[0])