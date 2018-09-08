
with open('./nawar-raw/nawar.csv', encoding='utf-8') as f:
    lines = [val[6:] for idx, val in enumerate(f.readlines()) if 0<=idx<700 or 888<idx<1095 ]
    s = set(''.join(lines))
    s.remove('.')
    s.remove(' ')
    s.remove('-')
    s.remove('\n')
    x = ''.join(s)
    print(len(x))
    print(len(s))
    print(list(x))
    print(x)
