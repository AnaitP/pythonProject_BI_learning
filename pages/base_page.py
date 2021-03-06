class BasePage():
    def __init__(self, browser, url, timeout=30):
        self.browser = browser
        self.url = url
        self.browser.maximize_window()
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True