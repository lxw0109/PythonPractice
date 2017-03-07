#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#References: https://pypi.python.org/pypi/selenium

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import unittest
import time
import datetime
import urllib2
import sys
import traceback
import os
import logging
logging.basicConfig(level=logging.DEBUG, filemode="w")

#UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-10: ordinal not in range(128)
reload(sys)
sys.setdefaultencoding("utf-8")

class YahooTestCase(unittest.TestCase):
    """
    HAVE NO NEED TO CARE TOO MUCH ABOUT THIS DEMO.
    Selenium WebDriver is often used as a basis for testing web applications.
    Here is a simple example uisng Python’s standard unittest library
    """
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get("http://www.yahoo.com")
        self.assertIn("Yahoo", self.browser.title)


def searchInYahoo(url):
    """
    browser.get("http://www.baidu.com")
    #browser.get("www.baidu.com")    #Cannot navigate to invalid URL. NOTE: http:// is essential.
    """
    browser.get(url)
    #print "browser.title:", browser.title
    assert "Yahoo" in browser.title
    #elem = browser.find_element_by_name("p") #[OK]Find the search box
    elem = browser.find_element_by_xpath('//*[@id="uh-search-box"]') #[OK]Find the search box
    elem.send_keys("lxw0109" + Keys.RETURN)
    #print "Keys.RETURN:", Keys.RETURN
    time.sleep(3)


def csdnDemo():
    browser.get("http://www.yahoo.com") # Load page
    assert "Yahoo" in browser.title
    elem = browser.find_element_by_name("p") # Find the query box
    elem.send_keys("seleniumhq" + Keys.RETURN)
    time.sleep(3) # Let the page load, will be added to the API
    #browser.implicitly_wait(3) # 智能等待
    try:
        newUrl = browser.find_element_by_xpath("//a[contains(@href,'http://www.seleniumhq.org')]")
        #newUrl = browser.find_element_by_xpath('//*[@id="yucs-login_signIn"]')
        ActionChains(browser).click(newUrl).perform() #鼠标左键. ".perform()" is essential. 
        #print newUrl #<selenium.webdriver.remote.webelement.WebElement (session="e4d91ee08e7bcc7e89844a0464051f53", element="0.6900426994876563-1")>
    except NoSuchElementException:
        assert 0, "can't find seleniumhq"
        print traceback.format_exc()
    time.sleep(3)
    browser.close()


def basicOperations(url):
    """
    browser.maximize_window()
    browser.set_window_size()
    browser.find_element_by_xpath()/browser.find_element_by_id()/browser.find_element_by_name()/...
    browser.back()
    browser.forward()
    browser.title

    get_attribute("type")
    send_keys()
    click()
    clear()
    text
    size
    """
    browser.get(url)
    assert u"百度" in browser.title #u"搜狗"

    text = browser.find_element_by_xpath('//*[@id="cp"]').text  #'//*[@id="query"]'
    print "copyright text:", text

    searchBar = browser.find_element_by_xpath('//*[@id="kw"]')
    searchBar.send_keys(u"lxw0109")
    #打印搜索框的大小
    print "searchBar.size:", searchBar.size #searchBar.size: {'width': 494, 'height': 22}
    print "searchBar.get_attribute(\"type\"):", searchBar.get_attribute("type")     #searchBar.get_attribute("type"): text

    browser.find_element_by_xpath('//*[@id="su"]').click()
    time.sleep(3)

    browser.set_window_size(800, 600)
    browser.get("http://www.cnblogs.com/lxw0109")
    time.sleep(3)

    browser.maximize_window()
    browser.back()
    time.sleep(3)
    browser.forward()

    browser.get("http://www.renren.com")
    email = browser.find_element_by_xpath('//*[@id="email"]')
    email.send_keys("531958897@qq.comm")
    time.sleep(1)
    email.send_keys(Keys.BACK_SPACE)
    browser.find_element_by_xpath('//*[@id="password"]').send_keys("liuxiaoweii")
    time.sleep(1)
    browser.find_element_by_xpath('//*[@id="password"]').send_keys(Keys.BACK_SPACE)
    browser.find_element_by_xpath('//*[@id="password"]').clear()
    #browser.find_element_by_xpath('//*[@id="password"]').send_keys("liuxiaowei")
    browser.find_element_by_xpath('//*[@id="password"]').send_keys("6Liuxiaowei")
    time.sleep(1)

    email.send_keys(Keys.CONTROL, "a")
    time.sleep(1)
    email.send_keys(Keys.CONTROL, "x")
    time.sleep(1)
    email.send_keys(Keys.CONTROL, "v")

    #browser.find_element_by_xpath('//*[@id="login"]').click()  #OK
    browser.find_element_by_xpath('//*[@id="login"]').send_keys(Keys.ENTER)
    time.sleep(3)
    article = browser.find_element_by_link_text(u"人人综艺")
    #ActionChains(browser).move_to_element(article).perform()   #not working
    #ActionChains(browser).context_click(article).perform() #鼠标右键
    ActionChains(browser).click(article).perform() #鼠标左键 ".perform()" is essential.


def getSourceCode(url):
    try:
        reqHeader = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0"}
        request = urllib2.Request(url=url, headers=reqHeader)
        response = urllib2.urlopen(request)
        sourceCode = response.read()
        return sourceCode
    except Exception as e:
        print traceback.format_exc()
        return ""

def generateLogger(loggerName):
    pageSrcLogger = logging.getLogger(loggerName)
    fh = logging.FileHandler(os.path.join(os.getcwd(), loggerName + ".log"))
    formatter = logging.Formatter("%(message)s")
    fh.setFormatter(formatter)
    pageSrcLogger.addHandler(fh)
    return pageSrcLogger


if __name__ == '__main__':
    #0. unittest demo:
    #unittest.main(verbosity=2)

    """
    browser = webdriver.Chrome()	#Get local session of chrome
    #print type(browser) #<class 'selenium.webdriver.chrome.webdriver.WebDriver'>
    browser.maximize_window() #浏览器窗口最大化
    """

    """
    #1. search in Yahoo automatically
    searchInYahoo("http://www.yahoo.com")
    browser.quit()
    """

    #2. http://blog.csdn.net/carolzhang8406/article/details/6925588
    #csdnDemo()

    #3. https://my.oschina.net/yangyanxing/blog/280871?p=1
    #basicOperations("https://www.baidu.com/")   #NOTE: "https://" is essential.

    #4. PhantomJS demo
    print datetime.datetime.now()
    driver = webdriver.PhantomJS(service_args=["--load-images=no"])
    #driver = webdriver.Chrome()
    driver.get("http://hotel.qunar.com/")
    title = driver.title
    print "title:", title
    pageSource = driver.page_source     #得到的页面源码不标准 ?但没有发现不标准的地方
    pageSrcLogger = generateLogger("driver.page_source")
    pageSrcLogger.debug(pageSource)

    #RECOMMENDED
    pageSource = driver.find_element_by_xpath("//*").get_attribute("outerHTML")
    slashSlashStarLLogger = generateLogger("slashSlashStar")
    slashSlashStarLLogger.debug(pageSource)

    pageSource = driver.find_element_by_xpath("*").get_attribute("outerHTML")
    starLogger = generateLogger("star")
    starLogger.debug(pageSource)

    sourceCode = getSourceCode("http://hotel.qunar.com/")   #urlopen: 好多信息提取不出来
    urlopenLogger = generateLogger("urlopen")
    urlopenLogger.debug(sourceCode)

    print datetime.datetime.now()

