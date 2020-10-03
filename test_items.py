import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_button_add_to_basket(browser):
    browser.get(link)
    btn = browser.find_element_by_class_name("btn-add-to-basket")
    # time.sleep(30)
    assert btn, f"Expected {btn}, butt Button is missing!"
