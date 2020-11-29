import re, os, codecs, csv
os.chdir('./textClassification')

# 정규표현식으로 레이블 추출
f = codecs.open('target_script.txt', 'r', encoding='utf-8')
p = re.compile(r'.*(takeshima is).*?[,|.]', re.I)
#print(f.read())
script = f.read()
labels = p.findall(script)
print(labels)
f.close()

f = codecs.open('label_result.txt', 'w', encoding='utf-8')
for i in labels:
    f.write(i + '\n')
f.close()

# crawlingResult.txt를 라인별로 읽어들이기
'''
f = codecs.open('crawlingResult.txt', 'r', encoding='utf-8')
print('-'*50)
lines = f.readlines()
for line in lines:
    print(line)
f.close()
'''