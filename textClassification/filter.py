from bayes import BayesianFilter
f = BayesianFilter()


# 영어텍스트 지도 학습(정답, 오류)
f.fit("Takeshima.", "오류")
f.fit("Takeshima is chinese.", "오류")
f.fit("Takeshima is Japan.", "오류")
f.fit("the ROK claims to be the former name of Takeshima, was not used.", "오류")
f.fit("Government and that the islands would be officially named Takeshima.", "오류")
f.fit("jurisdiction of the Oki Islands branch office of the Shimane Prefectural Government and that the islands would be officially named Takeshima.", "오류")
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
    pre, scorelist = f.predict(text1)
    print("결과 =", pre)
    print(scorelist)
