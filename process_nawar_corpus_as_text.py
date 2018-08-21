
with open('./nawar.txt', mode='w', encoding="utf-8") as wf:
    with open("./nawar.csv", encoding="utf-8") as rf:
        lines = [val[6:] for idx, val in enumerate(rf.readlines()) if 0<=idx<700 or 888<idx<1095 ]
        wf.writelines(lines)
