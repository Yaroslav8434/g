from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("yandexdriver.exe")
driver.get("https://yandex.ru/")
g = driver.find_element_by_name("text")
g.send_keys("gg", Keys.ENTER)







