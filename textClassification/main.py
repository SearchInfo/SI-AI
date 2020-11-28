from filter import filters
import csv, os, codecs
#filters("Dokdo is japan territory")


# filters("Hanbok is Chinese.")




os.chdir('./textClassification')

f = codecs.open('target_script.txt', 'r', encoding='utf-8')
total_lines = len(f.readlines())+1    # txt파일의 전체 라인 수를 total_lines에 할당
f.seek(0)
for i in range(total_lines): # 전체 라인 읽기위해 total_lines를 카운트변수로 지정
    line = f.readline() # f르 한줄씩 읽음
    filters(line)   # 읽은 line을 필터링
    print(line)     # 읽은 line을 출력
