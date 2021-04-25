from selenium import webdriver
import time
from openpyxl import Workbook
import pandas as pd

wb = Workbook()
ws = wb.create_sheet()
driver = webdriver.Chrome()

final = {}

# keyword_list에 추출할 연관검색어 쿼리 기입
keyword_list = ['쿼리1', '쿼리2', '쿼리3']

# 쿼리별 연관검색어 추출하기
for i in range(len(keyword_list)):
    URL = "https://search.naver.com/search.naver?ie=UTF-8&sm=whl_hty&query={}".format(keyword_list[i])
    driver.get(URL)

    searches = driver.find_elements_by_css_selector(".lst_related_srch li")

    temp = []

    for keyword in searches:
        result = keyword.text
        temp.append(result)

    final[keyword_list[i]] = pd.Series(temp)

df = pd.DataFrame(final)

# 파일명에 원하는 이름의 파일명 기입
df.to_excel('파일명.xlsx')

driver.quit()


