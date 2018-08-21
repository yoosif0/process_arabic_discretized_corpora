import pandas as pd
file_name =  './kasct_corpus.xls'
sheet =  'files-transcription'


with open("kacst_corpus.txt", mode="w", encoding="utf-8")as f:
    df = pd.read_excel(io=file_name, sheet_name=sheet)
    s = df.to_string()
    print(len(s))
    print(s[:100])
    f.write(s)
