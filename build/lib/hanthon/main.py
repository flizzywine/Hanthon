import re
import subprocess
import sys
code_file = sys.argv[1]

table = open('table.org').read()
# 怎么才能改成相对引用, 而不是把路径写死

code = open(code_file).read()

en2zh = {}
zh2en = {}
for line in table.splitlines():
    attr = list(filter(None, line.split('|')))
    attr = list(map(str.strip, attr))
    if len(attr):
        en2zh[attr[0]] = attr[1]
        zh2en[attr[1]] = attr[0]




pat = re.compile("(\w+)")

def trans2zh(mo):
    en = mo.group()
    if en in en2zh:
        return en.replace(en, en2zh[en])
    # print(mo.group())
    return mo.group()

def trans2en(mo):
    zh = mo.group()
    if zh in zh2en:
        return zh.replace(zh, zh2en[zh])
    return mo.group()

code = pat.sub(trans2en, code)

with open('hancache.py', 'w') as f:
    f.write(code)

    

subprocess.run(["python3", "hancache.py"])
