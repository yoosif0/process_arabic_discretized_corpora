from process_corpus_service import   cleanFile
from service import get_files
import os, errno
import argparse


def crateOutputDirectory(dir):
    try:
        os.makedirs(dir)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

def cleanNawarsCorpus(oldFile, newFile):
    with open(newFile, mode='w', encoding="utf-8") as wf:
        with open(oldFile, encoding="utf-8") as rf:
            lines = [val[6:] for idx, val in enumerate(rf.readlines()) if 0<=idx<700 or 888<idx<1095 ]
            wf.writelines(lines)


def clean(directory, newDirecotry, rawFilesEncoding="utf-8"):
    for idx, x in enumerate(get_files(directory)):
        cleanFile(directory+x, newDirecotry+x, rawFilesEncoding) 



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--corpus')
    args = parser.parse_args()
    crateOutputDirectory('./cleaned')
    if args.corpus == 'nawar':
        cleanNawarsCorpus("./nawar-raw/nawar.csv", './cleaned/nawar.txt')
        print('Done')
    if args.corpus == 'kasct':
        clean('./kasct-raw/', './cleaned/' )
    if args.corpus == 'tashkeela':
        clean('./tashkeela-raw/', './cleaned/')


