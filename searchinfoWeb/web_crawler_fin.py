import requests
from bs4 import BeautifulSoup
import os, codecs, re

# 저장할 폴더 위치를 상대경로로 지정
#os.chdir('./mysite')
print(os.getcwd())
print(os.path.isfile('target_script_origin.txt'))
# target_script_origin.txt파일이 존재한다면 삭제
if os.path.isfile('target_script_origin.txt'):
    os.remove('target_script_origin.txt')

# ----- class Content -----
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
        결과를 target_script.txt파일로 저장하는 함수
        '''
        if not os.path.isfile(filename):
            with codecs.open(filename, 'w', encoding='utf-8') as f:
                f.write(self.body + '\n')
        else:
            with codecs.open(filename, 'a', encoding='utf-8') as f:
                f.write(self.body + '\n')


# ----- class Website -----
class Website:
    '''
    웹사이트 구조에 관한 정보를 저장할 클래스
    '''
    def __init__(self, name, url, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag

# ----- class Crawler -----
class Crawler:
    def getPage(self, url):
        # , headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
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
                content.save_text('target_script_origin.txt')

# ----- main code -----
# 타겟 페이지의 내부링크를 리스트형으로 리턴하는 함수
def get_links(targetUrl, rootUrl, tagName, className):
    '''
    타겟 페이지의 내부링크를 리스트형으로 리턴하는 함수
    '''
    all_links = []  # 내부 링크를 받을 리스트

    # targetUrl 페이지로의 요청(Request) 객체를 생성합니다.
    req = requests.get(targetUrl)
    soup = BeautifulSoup(req.text, 'html.parser')

    for link in soup.find(tagName, {'class' : className}).findAll('a'):
        if 'href' in link.attrs: # link에 href속성이 있다면 그 값을 links에 저장
            links = link.attrs['href']
            all_links.append(rootUrl + links)   # rootUrl과 추출한links를 더해 온전한 URL획득
    return all_links

def webcrawler(url):
    if os.path.isfile('target_script_origin.txt'):
        os.remove('target_script_origin.txt')
    # 내부링크를 얻을 사이트의 정보
    siteInfo = [
        url, # targetUrl
        'http://www.ocrwebservice.com/',   # rootUrl
        'table',                       # tagName of exist <a> tag
        'tbl_style'                     # className of exist <a> tag
    ]
    # 내부 링크를 리스트로 links에 할당
    links = get_links(siteInfo[0], siteInfo[1], siteInfo[2], siteInfo[3])
    print('총 ', len(links), '개의 링크를 찾았습니다..')

    crawler = Crawler()
    # 타이틀과 내용을 얻을 사이트의 정보
    siteData = [
        ['ocrwebservice', url, 'h1', 'h4']
    ]
    # Website class 객체를 받을 리스트
    websites = []

    for row in siteData:
        # Website의 생성자로 siteData의 정보를 각 변수에 할당후 website리스트에 객체 할당
        websites.append(Website(row[0], row[1], row[2], row[3]))

    for link in links:
        # Crawler class 객체인 crawler의 parse()함수로
        crawler.parse(websites[0], link)

    # 정규식을 이용해 target_script_origin.txt를 읽은 후 불필요한 문자열 제거 후 temp에 임시저장
    if os.path.isfile('target_script_origin.txt'):
        with codecs.open('target_script_origin.txt', 'r', encoding='utf-8')as f:
            script = f.read()
            # 불필요한 내용(~~~), (â|â|â¦|â²|è¼) 삭제
            temp = re.sub(r'[(].+?[)]|(â|â|â¦|â²|è¼)', '', script)
            # 정규식을 이용해 마침표를 만나는 문장단위로 잘라 리스트형으로 저장
            temp = re.findall(r'[^\s][\w\W\s,-]+?[.]', temp)

    # temp에서 10자 미만의 불필요한 문자열 제거 후 target_script.txt에 쓰기
    with codecs.open('target_script.txt', 'w', encoding='utf-8') as f:
        # temp 리스트에 저장된 문장별로 줄넘김문자를 포함해 쓰기
        for line in temp:
            if len(line) > 10:
                f.write(line + '\n')
# url = 'http://www.ocrwebservice.com/'
# webcrawler(url)

