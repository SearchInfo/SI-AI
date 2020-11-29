from bayes import BayesianFilter
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

def filters(text):
# 예측
    result, scorelist = f.predict(text)
    print("결과 =", result)
    print(scorelist)
