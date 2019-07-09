from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time

option = webdriver.FirefoxOptions()
option.headless = True

browser = webdriver.Firefox(options=option)

browser.get('https://book.douban.com/subject_search?search_text= 9787115445353&cat=1001/')
# assert 'Yahoo' in browser.title

elem = browser.find_element_by_class_name("title-text")
print(elem.get_attribute('href'))

# time.sleep(5)
browser.quit()
