if len(inp) >= 1:
    if inp[0][0] == '$':
        print(eval(''.join(inp[0][1:])))
    else:
        print(''.join(inp))   