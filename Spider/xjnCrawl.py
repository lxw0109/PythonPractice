def xjnCrawl():
    browser.get("http://xiujinniu.com/") #Load page
    assert "嗅金牛" in browser.title
    ele = browser.find_element_by_xpath("//*[@id='searchBar']")
    pass
