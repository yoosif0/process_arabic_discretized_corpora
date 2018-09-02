# Process arabic corpora for pronouncing dictionary

## Pre-usage

#### Tashkeela
* Add corpus in a folder named "tashkeela-raw" in the root folder

#### Nawar's Halabi Corpus
* Add corpus in a folder named "tashkeela-raw" in the root folder

#### Kasct Corpus
* Add corpus in a folder named "kasct-raw" in the root folder 
* Open both files and in VS Code
    * Reopen with encoding "Arabic Windows(1256)"
    * Save with encoding "utf-8"

## Usage
* python .\process_corpus.py --corpus nawar
* python .\process_corpus.py --corpus kasct
* python .\process_corpus.py --corpus tashkeela
* python .\concat_corpora.py 


## Post Usage
* Use ara pronounciaiton tool to produce the dict file using `python corpus2cmudict.py -i output_with_last_haraka.txt -p haraka`
