## naver_related_search_crawler
쿼리별 네이버 연관검색어를 엑셀 파일로 저장해주는 크롤러이다.

## 사용방법
- keyword_list에 추출할 연관검색어 쿼리를 기입한다.
- 파일명에 원하는 이름의 파일명을 기입한다.

## 사용 라이브러리
- Selenium
- Pandas

## 작동 방식
- 네이버 검색 결과페이지를 업로드 하여 쿼리별 연관검색어를 추출한다. 
- 쿼리별 연관검색어를 데이터프레임에 저장한다. 
- 데이터프레임을 엑셀 파일로 저장한다. 