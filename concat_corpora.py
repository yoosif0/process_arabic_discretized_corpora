from service import get_files

def concat(directory, newFile):
    with open(newFile, 'w', encoding="utf-8") as outFile:
        for f in get_files(directory):
            with open(directory+f, encoding="utf-8") as infile:
                outFile.write(infile.read())
        outFile.close()

if __name__ == '__main__':
    concat('./cleaned/', 'output.txt')