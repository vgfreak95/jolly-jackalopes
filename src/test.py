from operator import index
import random
import os

def randomFile(number):
    try: 
        int(number)
    except ValueError:
        return "Mismatched Input"

    currentDir = os.getcwd()
    dirList1 = os.listdir(currentDir)
    dirList2 = [i for i in dirList1 if not i.endswith(".py")]

    output = []

    for i in range(0, number):
        randNum = random.randint(0, len(dirList2) - 1);
        f = open(dirList2[randNum], "r")
        output.append(f.read())

    return output