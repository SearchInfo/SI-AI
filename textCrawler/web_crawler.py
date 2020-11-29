# 수집할 정보에 대응하는 CSS선택자를 각각 문자열 하나로 만들고, 이들을 딕셔너리 객체에 모아서 BeautifulSoup select함수와 사용하는 기법
# Content는 \
import requests
from bs4 import BeautifulSoup
import os, codecs, re

# 저장할 폴더 위치를 상대경로로 지정
os.chdir('./textClassification')

class Content:
    '''
    글/페이지 전체에 사용할 기반 클래스
    '''

    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body

    def print(self):
        '''
        출력 결과를 원하는 대로 바꿀 수 있는 함수
        '''
        print('URL: {}'.format(self.url))
        print('TITLE: {}'.format(self.title))
        print('BODY: {}'.format(self.body))
    
    def save_text(self, filename):
        '''
        결과를 *.txt파일로 저장하는 함수
        '''
        f = codecs.open(filename, 'w', encoding='utf-8')
        f.write(self.body + '\n')
        f.close()

# Website 클래스는 각 페이지에서 수집한 정보를 저장하는 것이 아니라, 해당 데이터를 수집하는 방법에 대한 지침을 저장합니다.
class Website:
    '''
    웹사이트 구조에 관한 정보를 저장할 클래스
    '''

    def __init__(self, name, url, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag

# ----- 


class Crawler:

    def getPage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BeautifulSoup(req.text, 'html.parser')
    def safeGet(self, pageObj, selector):
        '''
        BeautifulSoup객체와 선택자를 받아 콘텐츠 문자열을 추출하는 함수
        주어진 선택자로 검색된 결과가 없다면 빈 문자열을 반환합니다.
        '''
        selectedElems = pageObj.select(selector)
        if selectedElems is not None and len(selectedElems) > 0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''
    def parse(self, site, url):
        '''
        URL을 받아 콘텐츠를 추출합니다.
        '''
        bs = self.getPage(url)
        if bs is not None:
            title = self.safeGet(bs, site.titleTag)
            body = self.safeGet(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(url, title, body)
                content.print()
                content.save_text('target_script.txt')

# -----
# 타겟 페이지의 내부링크를 리스트형으로 리턴하는 함수
def get_links():
    all_links = []
    
    # 전체 목록을 보여주는 페이지로의 요청(Request) 객체를 생성합니다.
    req = requests.get('https://www.mofa.go.jp/region/asia-paci/takeshima/index.html')
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    
    for link in soup.find('ul', {'class' : 'menu1'}).findAll('a'):
        if 'href' in link.attrs: # 내부에 있는 항목들을 리스트로 가져옵니다.
            #print(link.attrs['href'])
            links = link.attrs['href']
            all_links.append('https://www.mofa.go.jp' + links)

    return all_links

links = get_links()   # 내부 링크 리스트로 subjects에 할당
print('총 ', len(links), '개의 링크를 찾았습니다..')
# print(links) # 내부 링크 출력

crawler = Crawler()
siteData = [
    ['Japanese Territory', 'https://www.mofa.go.jp', 'h2', 'div#maincol p']
]
websites = []
'''
urls = [
    'https://www.mofa.go.jp/region/asia-paci/takeshima/index.html',
    'https://www.mofa.go.jp/a_o/na/takeshima/page1we_000014.html'
]
'''
for row in siteData:
    websites.append(Website(row[0], row[1], row[2], row[3]))

#crawler.parse(websites[0], urls[0])
#crawler.parse(websites[0], urls[1])

for link in links:
    crawler.parse(websites[0], link)


# .txt파일에 있는 문장을 정규표현식으로 문장단위로 자르기 정규식 : [\w\W\s,-]+?[.]
f = codecs.open('target_script.txt', 'r', encoding='utf-8')
script = f.read()
# 불필요한 ()내용 삭제
test = re.sub(r'[(].+?[)]', '', script)
# 마침표를 만나는 문장단위로 잘라 리스트형으로 저장
test = re.findall(r'[^\s][\w\W\s,-]+?[.]', test)
f.close()

f = codecs.open('target_script.txt', 'w', encoding='utf-8')
# test 리스트에 저장된 문장별로 줄넘김문자를 포함해 쓰기
for line in test:
    f.write(line + '\n')
f.close()

f = codecs.open('target_script.txt', 'r', encoding='utf-8')
# 파일 라인 수 구하기 1. read함수이용
print('read함수 : {}'.format(f.read().count('\n')+1))   # 162리턴
# 파일 읽기 위치 첫번째 라인으로 돌아가기
f.seek(0)
# 파일 라인 수 구하기 2. readlines함수이용
print('readlines함수 : {}'.format(len(f.readlines())))
f.close()