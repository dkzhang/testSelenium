# coding=utf-8

from selenium import webdriver
firefox_capabilities ={
    "browserName": "firefox",
    "version": "",
    "platform": "ANY",
    "javascriptEnabled": True,
    # "marionette": True,
}
browser = webdriver.Remote("http://192.168.100.7:5555/wd/hub", desired_capabilities=firefox_capabilities)
browser.get('https://book.douban.com/subject_search?search_text= 9787115445353&cat=1001/')
elem = browser.find_element_by_class_name("title-text")
print(elem.get_attribute('href'))

# time.sleep(5)
browser.quit()
