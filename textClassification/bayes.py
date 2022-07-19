import math, sys
import nltk # 형태소 분석 nltk 사용 자연어 처리를 위한 파이썬 패키지
#nltk.download('punkt') nltk의 punkt다운로드
#nltk.download('averaged_perceptron_tagger') nltk의 averaged_perceptron_tagger 다운로드
from nltk.corpus import stopwords
from nltk.tag import pos_tag 
from nltk.tokenize import word_tokenize


class BayesianFilter:
    # 베이지안 필터
    def __init__(self):
        self.words = set()  # 출현한 단어 기록
        self.word_d= {}  # 카테고리마다 단어 기록
        self.category_d = {}  # 카테고리 출현 횟수 기록

    # 문장 형태소 분석하기
    def split(self, text):
        results =[]
        #단어의 기본형 사용
        x = word_tokenize(text) # text안의 함수를 spaceㄱ단위와 구두점(punctuation)을 기준으로 토큰화 합니다.
        Wlist = pos_tag(x) # 품사를 저장합니다.
        for word in Wlist:
            if not word[1] in ["CC", "PRP", ".", ",", "VBP", "IN", "RB", "DT", "CD", "JJR", "JJS", "MD", "UH"]: # 품사 제외 처리
                # CC : 동위 접속사, PRP : 인칭 대명사, VBP : 1인칭 동사, IN : 전치사, RB : 부사, DT : 한정사, CD : 기수, JJR : 형용사 비교급, JJS : 형용사 최상급, MD : 조동사,
                # UH : 감탄사
                results.append(word[0])
        return results
        
 
    # 단어와 카테고리의 출현 횟수 세기
    def increase_word(self, word, category):
        # 단어를 카테고리에 추가하기
        if not category in self.word_d: # 카테고리 없을시 생성
            self.word_d[category] = {}
        if not word in self.word_d[category]: #카테고리안에 단어 없을시 생성
            self.word_d[category][word] = 0 #초기화

        self.word_d[category][word] += 1 # category안에 word 삽입 +1
        self.words.add(word) # words 세트안에 word를 add

    def increase_category(self, category):
        # 카테고리 계산하기
        if not category in self.category_d: # 카테고리 횟수 없을시 생성
            self.category_d[category] = 0 # category_d 초기화
        self.category_d[category] += 1 # 카테고리 + 1

    # words에 문장의 단어, word_d에 정답과 오류들의 단어들+1(단어들이 몇번나왔는지), category_d에 정답과 오류의 +1




    # 텍스트 학습 시작
    def fit(self, text, category): #매개변수 text, category
        # 텍스트 학습
        word_list = self.split(text) # split을 통해 대입
        for word in word_list: # 형태소 리스트 반복
            self.increase_word(word, category) # word에 대한 category분류
        self.increase_category(category) # 카테고리 분류

    # 단어 리스트에 점수 매기기
    def score(self, words, category):
        # 예시 : words(['Dokdo', 'korea']), category('정답')
        # 점수(확률) : (1) + (2)
        score = self.category_prob(category) # (1)전체 카테고리에 대한 해당 카테고리의 비율 category_d 사용

        # (2) 해당 카테고리 내에서 words 각각의 단어들에 대한 비율
        for word in words:
            score += self.word_prob(word, category) #스코어에 로그취하면서 더해준다
        return score

    # 카테고리 내부의 단어 출현 횟수 구하기
    def get_word_count(self, word, category):
        if word in self.word_d[category]:
            return self.word_d[category][word] # 카테고리안의 word의 밸류값
        else:
            return 0

    # 카테고리 계산 - 해당 카테고리/전체 카테고리
    def category_prob(self, category):
        sum_category = sum(self.category_d.values()) # 카테고리_d의 모든 값의 합
        category_v = self.category_d[category] # 하나의 카테고리 값
        result = category_v / sum_category
        return result

    # 카테고리 내부의 단어 출현 비율 계산
    def word_prob(self, word, category):
        c = self.get_word_count(word, category) + 1  # 가중치, 로그함수로인한 +1 로그0나오지 않게
        d = sum(self.word_d[category].values()) + len(self.words) # word_dict의 모든 values의 합 + words의 수
        return c / d

    # 예측하기
    def predict(self, text): # text : 가져올 문장
        b_category = None # 정답인지 오류인지 모름
        score_list = [] # 점수 정보를 저장하고 있는 리스트
        max_score = -sys.maxsize # 가장 작은수 대입
        words = self.split(text) # text split 문장대입
        
        for category in self.category_d.keys(): # 카테고리 리스트 추출 딕셔너리 내부의 키만큼 반복
            score = self.score(words, category) # 스코어 함수로인한 계산- 2개 출력(정답과 오류)
            # 정답과 오류의 로그를 10^2로 풀면 정답률과 오류율이 나옴
            score_list.append((category, score))
            if score > max_score: # 큰숫자 찾기
                max_score = score
                b_category = category
        return b_category, score_list
  

