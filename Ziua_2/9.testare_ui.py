from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime

URL = "https://bnr.ro"

driver = webdriver.Chrome()
driver.get(URL)
input()

xpath_euro = '//*[@id="784"]/div/div[1]/div/div/div[3]/div/div[2]/span'
euro_span = driver.find_element(By.XPATH, xpath_euro)
print(euro_span.text)
with open("euro.txt", "a") as fwriter:
    fwriter.write(f"{euro_span.text} - {datetime.datetime.now()}")


input()