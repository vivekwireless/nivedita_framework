from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# driver = webdriver.Chrome(path)
#
# wait_ = WebDriverWait(driver, 10)
# res = wait_.until(EC.visibility_of_element_located(locator))        # webelement

# class CheckVisibilityAndEnablity(EC.visibility_of_element_located):
#
#     def __init__(self, locator, driver):
#         super().__init__(locator)
#         self.driver = driver
#
#     def __call__(self, *args, **kwargs):
#         # wait_ = WebDriverWait(driver, 10)
#         # res = wait_.until(EC.visibility_of_element_located(locator))
#
#         result = super().__call__(self.driver)
#
#         if isinstance(result, WebElement):
#             enability = self.driver.find_element(*self.locator).is_enabled()
#             return enability
#         else:
#             return False
#
#
# def _wait(func):                # func --> click_on_element
#     def wrapper(*args, **kwargs):   # args --> (self, locator)
#         instance, locator = args
#         wait_ = WebDriverWait(instance.driver, 10)
#         wait_.until(CheckVisibilityAndEnablity(locator, instance.driver), message="element is not interactable")
#         return func(*args, **kwargs)
#
#     return wrapper              # click_on_element --> wrapper

##################################################################################################
class VisibilityAndEnability(EC.visibility_of_element_located):
    def __init__(self, locator):
        super().__init__(locator)

    def __call__(self, driver):
        result = super().__call__(driver)

        if isinstance(result, WebElement):
            return result.is_enabled()
        else:
            return False


def _wait(func):
    def wrapper(*args, **kwargs):
        instance, locator = args
        w = WebDriverWait(instance.driver, 10)
        w.until(VisibilityAndEnability(locator), message="element is either invisible or disabled")
        return func(*args, **kwargs)
    return wrapper


###############################################################################################

# def _wait(func):
#     def wrapper(*args, **kwargs):
#         instance, locator = args
#
#         wd = WebDriverWait(instance.driver, 10)
#         result = wd.until(EC.visibility_of_element_located(locator), message="element is not visible")
#
#         if isinstance(result, WebElement):
#             if result.is_enabled():
#                 return func(*args, **kwargs)
#
#         raise ValueError("element is either disabled or invisible")
#     return wrapper

##############################################################################################
# parameterized

class VisibilityAndEnability(EC.visibility_of_element_located):

    def __init__(self, locator):
        super().__init__(locator)

    def __call__(self, driver):
        result = super().__call__(driver)

        if isinstance(result, WebElement):
            return result.is_enabled()
        else:
            return False


def outer(is_alert=False, visibility=True, enability=True):
    def _wait(func):
        def wrapper(*args, **kwargs):
            if is_alert:
                instance = args[0]
                w = WebDriverWait(instance.driver, 10)
                w.until(EC.alert_is_present, message="no such alert")

            elif enability and visibility:
                instance, locator = args
                w = WebDriverWait(instance.driver, 10)
                w.until(VisibilityAndEnability(locator), message="element is invisible or disabled")

            elif visibility:
                instance, locator = args
                w = WebDriverWait(instance.driver, 10)
                w.until(EC.visibility_of_element_located(locator), message="element is invisible")

            return func(*args, **kwargs)
        return wrapper
    return _wait


