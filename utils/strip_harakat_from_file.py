from pyarabic.araby import  strip_harakat

with open('./nawar-raw/nawar.csv', encoding='utf-8') as f:
    with open('nawar_stripped.txt', mode='w', encoding="utf-8") as fw:
        fw.write(strip_harakat(f.read()))
