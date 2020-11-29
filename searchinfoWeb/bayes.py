import math, sys
import nltk # 형태소 분석 nltk 사용 자연어 처리를 위한 파이썬 패키지
#nltk.download('punkt') # nltk의 punkt다운로드
#nltk.download('averaged_perceptron_tagger') # nltk의 averaged_perceptron_tagger 다운로드
from nltk.corpus import stopwords
from nltk.tag import pos_tag #
from nltk.tokenize import word_tokenize


class BayesianFilter:
    # 베이지안 필터
    def __init__(self):
        self.words = set()  # 출현한 단어 기록
        self.word_dict = {}  # 카테고리마다의 출현 횟수 기록
        self.category_dict = {}  # 카테고리 출현 횟수 기록

    # 형태소 분석하기 -- (1)
    def split(self, text):
        results =[]
        #단어의 기본형 사용
        x = word_tokenize(text) # text안의 함수를 spaceㄱ단위와 구두점(punctuation)을 기준으로 토큰화 합니다.
        malist = pos_tag(x) # 품사를 저장합니다.
        for word in malist:
            if not word[1] in ["CC", "PRP", ".", ",", "VBP", "IN", "RB", "DT", "CD", "JJR", "JJS", "MD", "UH"]: # 품사 제외 처리
                # CC : 동위 접속사, PRP : 인칭 대명사, VBP : 1인칭 동사, IN : 전치사, RB : 부사, DT : 한정사, CD : 기수, JJR : 형용사 비교급, JJS : 형용사 최상급, MD : 조동사,
                # UH : 감탄사
                results.append(word[0])
        return results



    # 단어와 카테고리의 출현 횟수 세기 -- (2)
    def inc_word(self, word, category):
        # 단어를 카테고리에 추가하기
        if not category in self.word_dict: # 카테고리 없을시 생성
            self.word_dict[category] = {}
        if not word in self.word_dict[category]:
            self.word_dict[category][word] = 0
        self.word_dict[category][word] += 1 # category안에 word 삽입
        self.words.add(word) # words 세트안에 word를 add

    def inc_category(self, category):
        # 카테고리 계산하기
        if not category in self.category_dict:
            self.category_dict[category] = 0
        self.category_dict[category] += 1

    # 텍스트 학습하기 -- (3)
    def fit(self, text, category): #매개변수 text, category
        """ 텍스트 학습 """
        word_list = self.split(text) # split을 통해 대입
        for word in word_list: # 형태소 리스트
            self.inc_word(word, category) # word에 대한 category분류
        self.inc_category(category)

    # 단어 리스트에 점수 매기기-- (4)
    def score(self, words, category):
        score = math.log(self.category_prob(category))
        for word in words:
            score += math.log(self.word_prob(word, category))
        return score

    # 예측하기 -- (5)
    def predict(self, text):
        best_category = None
        max_score = -sys.maxsize # 가장 작은수 대입
        words = self.split(text) #text split
        score_list = []
        for category in self.category_dict.keys(): # 카테고리 분류
            score = self.score(words, category)
            score_list.append((category, score))
            if score > max_score:
                max_score = score
                best_category = category
        return best_category, score_list

    # 카테고리 내부의 단어 출현 횟수 구하기
    def get_word_count(self, word, category):
        if word in self.word_dict[category]:
            return self.word_dict[category][word] # 카테고리안의 word값
        else:
            return 0

    # 카테고리 계산
    def category_prob(self, category):
        sum_categories = sum(self.category_dict.values())
        category_v = self.category_dict[category]
        return category_v / sum_categories

    # 카테고리 내부의 단어 출현 비율 계산 -- (6)
    def word_prob(self, word, category):
        n = self.get_word_count(word, category) + 1  # -- (6a) # 로그함수로인한 +1
        d = sum(self.word_dict[category].values()) + len(self.words) #word_dict의 모든 values의 합 + words의 수
        return n / d
