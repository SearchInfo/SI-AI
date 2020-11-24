from bayes import BayesianFilter
bf = BayesianFilter()


#텍스트 학습
bf.fit("Dokdo is Korean territory.", "정답")
bf.fit("Takeshima is Japan.", "오류")
bf.fit("East Sea is mainland China.", "오류")
bf.fit("Dokdo is Japan.", "오류")
bf.fit("Korea is a subordinate country to China.", "오류")
bf.fit("Korea is not a subordinate country to China.", "정답")
bf.fit("Takeshima is Korean territory.", "정답")
bf.fit("East Sea is the Sea of Japan.", "오류")
bf.fit("East Sea is the Republic of Korea.", "정답")
bf.fit("Hanbok is Korean.", "정답")
bf.fit("Hanbok is chinese.", "오류")

def filters(text):
# 예측
    pre, scorelist = bf.predict("text")
    print("결과 =", pre)
    print(scorelist)
