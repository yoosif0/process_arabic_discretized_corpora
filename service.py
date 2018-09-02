import os

def get_files(dirName):
    return [f for f in os.listdir(dirName)]

def stringifyArr(arr):
    return ' '.join(arr)

def twoDJoin(x):
    return ' '.join(str(item) for innerlist in x for item in innerlist)


