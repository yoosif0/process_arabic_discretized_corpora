from pyarabic.araby import  tokenize, is_arabicword, strip_lastharaka
import re
import os
import service

def has_double_shadda(word):
    SHADDA = u'\u0651'
    return True if re.search(SHADDA+SHADDA, word) else False


def cleanFile(oldFile, newFile, rawFilesEncoding):
    with open(oldFile, 'r', encoding='utf-8') as myfile:
        x= myfile.read().split()
        x = [tokenize(word) for word in x if not has_double_shadda(word) and is_arabicword(word)]
        x = service.twoDJoin(x)
        print(oldFile, newFile)
        with open(newFile, 'w', encoding="u")as wF:
            wF.write(x)


