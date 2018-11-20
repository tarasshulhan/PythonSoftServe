def list_animals(animals):
    l = ''
    for i in range(len(animals)):
        l += str(i + 1) + '. ' + animals[i] + '\n'
    return l