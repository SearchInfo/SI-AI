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

코드에 대한 내용은 [textCrawler] (https://github.com/SearchInfo/SI-AI/tree/main/textCrawler "web_crawler_fin.py") 참조
