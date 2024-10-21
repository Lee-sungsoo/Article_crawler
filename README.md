# Article_crawler

이 코드는 특정 웹사이트(railway-news)의 article을 crawling하는 코드 입니다.
해당 crawler는 동적 사이트에서 데이터 수집을 위해 selenium 라이브러리를 사용하여 수집하고자 하는 url에 접근하여 beautifulsoup 라이브러리를 사용하여 해당 정보드를 수집하는 방식으로 작동합니다.

## 목적
- 지정된 웹사이트에서 지난 1년간의 기사를 자동으로 수집
- 각 기사의 title, content, upload_date 등을 수집하여 csv 형태로 저장

## 사용법
```
python crawling.py -u <url>
```

### example
```
python crawling.py -u "http://railway-news.com/"
```

## 주요기능
- 기사 URL 수집: 주어진 웹사이트에서 upload data를 참고하여 지난 1년간의 기사 URL을 수집
- 기사 내용 크롤링: 각 기사 페이지에서 title, content, upload date 등 추출
- 데이터 저장: 추출한 데이터를 csv형태로 저장