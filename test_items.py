import time
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
from selenium.common.exceptions import NoSuchElementException

def test_ExistsButtonSendToBasket(browser):
    browser.get(link)
    time.sleep(5)
    try:
        button = browser.find_element_by_xpath('//*[@id="add_to_basket_form"]/button')
    except NoSuchElementException:
        return False
    return True

