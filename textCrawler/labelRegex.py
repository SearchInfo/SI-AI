import re, os, codecs, csv


# 정규표현식으로 레이블 추출
f = codecs.open('crawlingResult.txt', 'r', encoding='utf-8')
p = re.compile(r'takeshima is.+?[,|.]', re.I)
#print(f.read())
script = f.read()
labels = p.findall(script)
print(labels)
f.close()

f = codecs.open('label_result.txt', 'w', encoding='utf-8')
for i in labels:
    f.write(i + '\n')
f.close()