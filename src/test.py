import os
import random

def randomFile(number):
    try: 
        int(number)
    except ValueError:
        return "Mismatched Input"

    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # change working directory to directory of test.py
    currentDir = os.getcwd()
    dirList1 = os.listdir(currentDir)
    dirList2 = [i for i in dirList1 if not i.endswith(".py")]
    # excludes python files

    output = []

    for i in range(0, number):
        randNum = random.randint(0, len(dirList2) - 1);
        f = open(dirList2[randNum], "r")
        output.append(f.read())

    return output
    
