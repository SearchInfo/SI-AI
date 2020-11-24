import csv

#쓰기
# a : 추가 w : 매번 지우고 새로 추가
f = open('sample.csv', 'w', encoding='utf-8', newline='') # 인코딩방식에 utf-8이 깨지면 CP949, MS949, EUC-KR
wr = csv.writer(f) #csv 모듈의 writer
wr.writerow([1,2,3])
f.close()

#읽기
f = open('sample.csv', 'r', encoding='utf-8')
rd = csv.reader(f) #csv 모듈의 writer
for i in rd:
    print(i)
