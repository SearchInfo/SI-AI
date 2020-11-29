import requests
from bs4 import BeautifulSoup
import codecs, re, os

os.chdir('./textClassification')
# https://www.mofa.go.jp/ -- 루트url
# 모든 내부 링크를 가져오는 함수
def get_subjects():
    subjects = []
    
    # 전체 주제 목록을 보여주는 페이지로의 요청(Request) 객체를 생성합니다.
    req = requests.get('https://www.mofa.go.jp/region/asia-paci/takeshima/index.html')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    
    for link in soup.find('ul', {'class' : 'menu1'}).findAll('a'):
        if 'href' in link.attrs: # 내부에 있는 항목들을 리스트로 가져옵니다.
            #print(link.attrs['href'])
            subject = link.attrs['href']
            subjects.append(subject)

    return subjects

subjects = get_subjects()   # 내부 링크 리스트로 subjects에 할당
print('총 ', len(subjects), '개의 링크를 찾았습니다..')
print(subjects) # 내부 링크 출력

# -------------------

i = 1
f = codecs.open('crawlingResultDelete().txt', 'w', encoding='utf-8')
p = re.compile(r'[(].+?[)]')
# 모든 내용에 접근
for sub in subjects:
    print('(', i, '/', len(subjects), ')', sub)
    # 각 내부url(sub)을 루트url(https://www.mofa.go.jp/)로 순회
    req = requests.get('https://www.mofa.go.jp/' + sub)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    
    # - <div id = 'container'>의 자손<p>태그에 주요 내용이 담겨있기에 가져옴
    qnas = soup.find('div', {'id' : 'container'}).findAll('p')
    
    # 각각의 내용에 모두 접근합니다.
    for qna in qnas:
        #f.write(qna.text + '\n')
        #()안에 들어있는 문장 삭제 후 저장
        result = re.sub(r'[(].+?[)]', '', qna.text)
        f.write(result + '\n')
        
    i = i + 1

#f.write(p.sub(r'[(].+?[)]', '', f))

f.close()
print(os.getcwd())

print(os.getcwd())
print('end of programm')

