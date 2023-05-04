from library.custom_wait import outer


class Generic:
    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    def enter_text(self, locator, *, value):
        self.driver.find_element(*locator).send_keys(value)
