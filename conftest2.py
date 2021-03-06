import selenium
import pytest

password = '123'
new_login = 'test'

@pytest.fixture
def setup_class():
    browser.get('http://ss.dev.bnvt.ru/')

    browser.find_element_by_css_selector("#username").send_keys("netrika")
    browser.find_element_by_css_selector("#password").send_keys("netrika")
    browser.find_element_by_css_selector("input.btn").click()
    browser.get('http://ss.dev.bnvt.ru/superset/dashboard/179')

@pytest.fixture(scope='session')
#def browser():
#    browser = selenium.webdriver.Chrome()
#    browser.implicitly_wait(10)
#    yield browser
#    browser.quit()


@pytest.fixture
def admin_login_fix(browser):
    link = "http://r78-rc-superset.zdrav.netrika.ru/"
    page = LoginPage(browser, link)
    page.admin_login()


@pytest.fixture
def user_login_fix(browser):
    link = "http://r78-rc-superset.zdrav.netrika.ru/"
    page = LoginPage(browser, link)
    page.user_login()

    yield page
    page.quit()
