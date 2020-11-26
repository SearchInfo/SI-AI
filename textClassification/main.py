from filter import filters

#filters("Dokdo is japan territory")


# filters("Hanbok is Chinese.")


import csv, os, codecs

print(os.getcwd())
os.chdir('./textClassification')
print(os.getcwd())
f = open('crawlingResultDelete().txt', 'r', encoding='utf-8')
for i in range(10):
    line = f.readline()
    filters(line)
    print(line)
filters("Dokdo is korea")
