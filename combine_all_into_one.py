def getFileNamesAndConcat(dirName):
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir(dirName) if isfile(join(dirName, f))]
    
    outfile = open(dirName+'output_with_last_haraka.txt', 'w', encoding="utf-8")
    for fname in onlyfiles:
            with open(dirName+fname, encoding="utf-8") as infile:
                outfile.write(infile.read())
    outfile.close()

    getFileNamesAndConcat('outputs/')