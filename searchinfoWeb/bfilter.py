from bayes import BayesianFilter
from numpy import core
from numpy.core import multiarray
from numpy import show_config as show_numpy_config
# from scipy.stats.stats import betai
from nltk.metrics import ContingencyMeasures, BigramAssocMeasures, TrigramAssocMeasures, QuadgramAssocMeasures
from nltk.collocations import *
from web_crawler_fin import *
import codecs
f = BayesianFilter()

# 영어텍스트 지도 학습(정답, 오류)
f.fit("Takeshima is Japan.", "오류")
f.fit("Dokdo is korean", "정답")
f.fit("Dokdo is korea", "정답")
f.fit("Dokdo is korean territory", "정답")
f.fit("Dokdo are korea", "정답")
f.fit("Dokdo is korea", "정답")
f.fit("Dokdo is korea", "정답")
f.fit("Dokdo is chinese", "오류")
f.fit("Dokdo is japanese", "오류")
f.fit("Dokdo is american", "오류")
f.fit("East Sea is mainland China.", "오류")
f.fit("Dokdo is Japan.", "오류")
f.fit("Dokdo is japan territory", "오류")
f.fit("Dokdo is japanese", "오류")
f.fit("Korea is a subordinate country to China.", "오류")
f.fit("Korea is not a subordinate country to China.", "정답")
f.fit("Takeshima is Korean territory.", "정답")
f.fit("East Sea is the Sea of Japan.", "오류")
f.fit("East Sea is the Republic of Korea.", "정답")
f.fit("Hanbok is Korean.", "정답")
f.fit("Hanbok is chinese.", "오류")



def filters(text1):
# 예측
    result, scorelist = f.predict(text1)
    print("결과 =", result)
    print(scorelist)
#import csv, os, codecs
#filters("Dokdo is japan territory")


# filters("Hanbok is Chinese.")



# os.chdir('./mysite')
def runFilter():
    f = codecs.open('target_script.txt', 'r', encoding='utf-8')
    total_lines = len(f.readlines())+1    # txt파일의 전체 라인 수를 total_lines에 할당
    f.seek(0)
    for i in range(total_lines): # 전체 라인 읽기위해 total_lines를 카운트변수로 지정
        line = f.readline() # f르 한줄씩 읽음
        result = filters(line)   # 읽은 line을 필터링
        return result + '\n' + line     # 읽은 line을 출력
'''
print('before filter')
filters("Dokdo is korea")
print('Dokdo is korea')
print('after filter')
'''
