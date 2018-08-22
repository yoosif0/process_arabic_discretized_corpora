from pyarabic.araby import  tokenize, is_arabicword, strip_lastharaka
import re
dirName = 'tashkeela-raw/'
SHADDA = u'\u0651'

def has_double_shadda(word):
    return True if re.search(SHADDA+SHADDA, word) else False


def stringifyArr(arr):
    return ' '.join(arr)


def write(fileName, content):
    file = open(fileName, 'w', encoding="utf-8")
    file.write(content)
    file.close()

def getFileNames(dirName):
    from os import listdir
    from os.path import isfile, join
    return [f for f in listdir(dirName) if isfile(join(dirName, f))]


def tokenizeAllFiles():
    onlyfiles = getFileNames(dirName)
    for file in onlyfiles:
        with open(dirName+file, 'r', encoding='utf-8') as myfile:
            data=myfile.read().replace('\n', '')
            t = tokenize(data)
            write(dirName+file, stringifyArr(t))


def stripAllFiles():
    onlyfiles = getFileNames(dirName)
    for file in onlyfiles:
        r = open(dirName+file, encoding='utf-8')
        arr = r.readlines()
        splitted_lines = [line.split() for line in arr]
        x=[[strip_lastharaka(word) for word in sentence if not has_double_shadda(word) and is_arabicword(word)] for sentence in splitted_lines]
        s = [' '.join(sentence) + '\n' for sentence in x]
        e= ''.join(s)
        write(dirName+file, e)    


def stripAllFilesAndKeepLastHaraka():
    onlyfiles = getFileNames(dirName)
    for file in onlyfiles:
        r = open(dirName+file, encoding='utf-8')
        arr = r.readlines()
        splitted_lines = [line.split() for line in arr]
        x=[[word for word in sentence if not has_double_shadda(word) and is_arabicword(word)] for sentence in splitted_lines]
        s = [' '.join(sentence) + '\n' for sentence in x]
        e= ''.join(s)
        write(dirName+file, e)    


tokenizeAllFiles()

stripAllFilesAndKeepLastHaraka()

