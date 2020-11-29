# SI-AI

1. Introduce
2. Crawlier
   - python module
3. Machine Learning
   - Bayesian recursive fillter
4. Output Configuration
   - flask
   - pythonanywhere

---
Web
===
---

<http://searchinfo.pythonanywhere.com/>


---
Introduce
---

최근 한일 간 동해 표기 신경전에서 IHQ 측의 바다 지명 표기가 고유 번호로 바뀌는 이슈가 있었고
해외 웹 사이트에 올바른 정보가 표기되었다면 예방할 수 있었던 문제였다고 생각합니다.
저희는 지금까지 경험을 토대로 개발한 인공지능 기반 웹을 통해 이런 문제점을 해결해보고자 프로젝트에 참여하게 됐습니다.
저희는 파이썬을 이용하여 해외 온라인상 대한민국 관련 정보 표기 오류에 대한 검색을 위한 인공지능 기반의 웹을 개발하였습니다. 

인공지능과 크롤링을 위한 다양한 라이브러리를 제공하는 파이썬을 활용하여
관련 사이트의 URL을 입력을 통해 독도와 동해에 대한 명확한 표기를 체크했습니다.


---
Crawler
---

python 기반의 모듈을 통해 작성하였습니다.
 * Requests
 * Regular Expression
 * Beautifulsoup

코드에 대한 내용은 

[crawler.py] (https://github.com/SearchInfo/SI-AI/blob/main/searchinfoWeb/web_crawler_fin.py ,"web_crawler_fin.py")  참조

---
Machine Learning
---

Bayes' theorem 기반으로 카테고리화 시켜 분석하였습니다.
특히 bayesian recursive fillter 기법을 사용하였습니다.

코드에 대한 내용은
[bayes] (https://github.com/SearchInfo/SI-AI/blob/main/searchinfoWeb/bayes.py , " Classification ")
bayes, fillter, main 확인

---
Output Configuration
---

python 라이브러리인 flask 패키지를 사용하여 웹을 구성하였습니다.
server가 되는 python 파일 생성 후 정적으로 바인딩하여
fillter application for python file 들을 Import 하여 사용합니다.

Pythonanywhere 무료 호스팅 API를 사용하여 웹을 구현하였습니다.

---
except
---

 - 누구나 손쉽게 접근가능한 웹페이지로써 접근성에 특화됩니다.
 - URL을 복사하여 붙여넣기만 하면 결과가 나옴으로써 편의성이 좋습니다.
 - 이러한 캠페인을 통하여 대한민국의 표기오류가 점차 감소될 수 있습니다.
 - 잘못된 표기들을 개선해 나감으로써 그로부터 파생될 수 있는 많은 문제들의 예방 효과를 기대할 수 있습니다.

*developmental*
 - 텍스트 뿐 아니라 이미지, 영상의 분석으로 개발하여 더욱 확장성 있는 애플리케이션이 될 수 있습니다.
 - 더욱 많은 언어들과 데이터셋들을 학습시켜서 정확성과 영어만이 아닌 다른 언어들도 분석 할 수 있습니다.
 - 위와 같은 과정을 통해 발전시킨다면 대한민국의 표기 오류에 대해 더욱더 많이 줄여나갈 수 있습니다.
 
 
 ---
 
Contact us

<youngjun1996@naver.com>


