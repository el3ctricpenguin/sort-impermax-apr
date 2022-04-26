import requests,time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://polygon.impermax.finance/'


driver = webdriver.Firefox()
driver.get(url) #seleniumでurlのページを開く
time.sleep(5)
print("!")

#seleniumで扱いたいものをBSで選択してるのがおかしそう

#soupにhtmlを読み込ませる
soup = BeautifulSoup(driver.page_source,'html.parser')
results = soup.find_all(class_="title")

#特定の文字列を含む要素をクリックしたかった。くやしいが動かん！
#driver.find_element(By.XPATH,"//*[contains(@text,'24 hours average')]").click()
driver.find_element(By.XPATH,'//*[@id="impermax-app"]/div/div/div/div[1]/div[3]/div/div[2]/div/div[2]/span').click()
time.sleep(1)
table = soup.select("div.card-body > .pairs-table")
row = soup.select("#impermax-app div.home > div.mt-2.container   > a.pairs-table-row:nth-child(2)")

driver.find_element(By.XPATH,'//*[@id="impermax-app"]/div/div/div/div[1]/div[3]/div/div[2]/div/div[1]/span').click()
time.sleep(1)


driver.quit()

#print(results)
