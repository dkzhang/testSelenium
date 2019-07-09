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
browser.get("http://www.163.com")
print(browser.find_element_by_css_selector('a'))
browser.get_screenshot_as_file(r"./sample.png")
browser.quit()
