import os
import shutil

arquivo = open("codigo.bat", "r")

for terminal in arquivo:
    terminal = terminal.splitlines()
    auxiliar = "".join(terminal)
    vetor = auxiliar.split(' ')

    if vetor[0]== "cd":
        cd=vetor[1]+"/"
        print(auxiliar[::])

    elif vetor[0]=="md":
        os.mkdir(cd+vetor[1])

    elif vetor[0]=="copy":
        copy="".join(vetor[1])
        copy=cd+copy
        shutil.copy2(copy,vetor[2])

    elif vetor[0]=="move":
        move="".join(vetor[1])
        move=cd+move
        shutil.move(move,vetor[2])

    elif vetor[0] == "ECHO":
        print(auxiliar[4::])

arquivo.close()
