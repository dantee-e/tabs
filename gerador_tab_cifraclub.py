def next(notas):
    for i in notas:
        notas[i].append(-1)

def next_mod(notas, gordos):
    j=0
    for i in notas:
        if j not in gordos:
            notas[i].append(-1)
        j+=1
    

def addNote(corda, casa, notas):
    notas[corda].append(casa)

def printCorda(corda): #recebe a lista de notas
    for casa in corda:
        if casa==-1:
            print('-', end='')
        elif casa==-2:
            print('X', end='')
        else:
            print(casa, end='')
    print()


def printTab(notas, n_strings, output):
    if output:
        return printTabToFile(notas, n_strings)
    j=0
    for i in notas:
        j+=1
        if j>n_strings:
            break
        print(i, end=' |-')
        printCorda(notas[i])

def printCordaToFile(corda, file): # Recebe a lista de notas e o arquivo
    for casa in corda:
        if casa == -1:
            file.write('-')
        elif casa == -2:
            file.write('X')
        else:
            file.write(str(casa))
    file.write('\n')

def printTabToFile(notas, n_strings):
    with open('tab.txt', 'a') as file:
        j = 0
        for i in notas:
            j += 1
            if j > n_strings:
                break
            file.write(f"{i} |-")
            printCordaToFile(notas[i], file)
        file.write('\n')