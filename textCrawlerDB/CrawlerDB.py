import csv
import requests
import sqlite3
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from html import unescape


# https://www.mofa.go.jp/ -- 루트url
# 모든 내부 링크를 가져오는 함수
def get_subjects():
    subjects = []

    # 전체 주제 목록을 보여주는 페이지로의 요청(Request) 객체를 생성합니다.
    req = requests.get('https://www.mofa.go.jp/region/asia-paci/takeshima/index.html')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    for link in soup.find('ul', {'class': 'menu1'}).findAll('a'):
        if 'href' in link.attrs:  # 내부에 있는 항목들을 리스트로 가져옵니다.
            # print(link.attrs['href'])
            subject = link.attrs['href']
            subjects.append(subject)

    return subjects


# csv 파일에 저장
def csvsave():
    i = 1
    with open('datas.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['url', 'data'])
        for qna in qnas:
            writer.writerows([
                qna.text, 'fuck the ,<- is bad ?'
            ])
        i = i + 1

# 매개 변수로 전달받을 url 기반으로 웹페이지 추출
def fetch(url):
    f = urlopen(url)
    # http 헤더를 기반으로 인코딩 형식을 추출
    encoding = f.info().get_content_charset(failobj="utf-8")
    # 추출한 인코딩 형식을 기반으로 문자열을 디코딩
    htmls = f.read().decode(encoding)
    return htmls

# 매개 변수로 받은 html을 기반으로 정규 표현식을 사용해 모든 값들을 추출
def scrape(html):
    datas = []
    # html을 이용해 데이터를 추출
    for partial_html in re.findall(r'<td class="left"><a.*?</td>', html, re.DOTALL):
        #url을 추출
        url = re.search(r'<a href="(.*?)">', partial_html).group(1)
        url = 'https://www.mofa.go.jp/' + url
        #태그를 제거해 데이터 추출출        title = re.sub(r'<.*?>', '', partial_html)
        title = unescape(title)
        datas.append({'url': url, 'title': title})

    return datas


# db에 저장하는 함수
def save(db, datas):
    # db를 열고 연결을 변수에 저장
    conn = sqlite3.connect(db)
    # 커서를 추출
    c = conn.cursor()
    # 스크립트를 여러번 사용해도 같은 결과를 사용하게 테이블이 존재하는 경우 제거
    c.execute('DROP TABLE IF EXISTS datas')
    # 테이블을 생성
    c.execute('''
        CREATE TABLE datas(
            text text,
            url text
        )
    ''')
    # 여러 개의 파라미터를 리스트로 지정해서 sql구문을 실행
    c.executemany('INSERT INTO datas VALUES(:text, :url)', datas)
    # 저장한 데이터를 추출
    for row in c.execute("SELECT * FROM datas"):
        print(row)
    # 변경사항을 커밋(저장)
    conn.commit()
    # 연결을 닫음
    conn.close()


subjects = get_subjects()  # 내부 링크 리스트로 subjects에 할당
print('총 ', len(subjects), '개의 링크를 찾았습니다..')
print(subjects)  # 내부 링크 출력

# -------------------

i = 1

# 모든 내용에 접근
for sub in subjects:
    print('(', i, '/', len(subjects), ')', sub)
    # 각 내부url(sub)을 루트url(https://www.mofa.go.jp/)로 순회
    req = requests.get('https://www.mofa.go.jp/' + sub)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    # - <div id = 'container'>의 자손<p>태그에 주요 내용이 담겨있기에 가져옴
    qnas = soup.find('div', {'id': 'container'}).findAll('p')

    # 각각의 내용에 모두 접근합니다.
    for qna in qnas:
        print(qna.text)
    i = i + 1

print('end of programm')
csvsave()
# fetch의 html을 str 자료형의 형태로 대입
htmls = fetch('https://www.mofa.go.jp/')
#htmls의 html을 기반으로 데이터 값을 추출해 대입
datas = scrape(htmls)
save('datas.db', datas)