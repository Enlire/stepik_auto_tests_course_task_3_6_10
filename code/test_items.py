from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_user_should_see_add_to_basket_button(browser):
    browser.get(link)

    # time.sleep(30)

    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-add-to-basket"))
        )
    except TimeoutException:
        assert False, "'Add to basket' button did not appear within 5 seconds"