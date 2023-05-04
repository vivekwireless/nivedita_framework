import datetime
import pytest
from POM.register_page import Register
from time import sleep
# from library.reading_excel import read_testdata
from library.config import Config

data = [("vivek", "jadhav", "kdlsdskjh@gmail.com", "nxbc@4567")]

# data = read_testdata(Config.REG_PAGE_DATA)


@pytest.mark.parametrize("f_name, l_name, email, pwd1", data)
def test_reg(f_name, l_name, email, pwd1, initialize_driver):
    res = initialize_driver
    r_obj = Register(res)
    r_obj.sign_up_link()
    r_obj.scrollpage()
    sleep(10)
    r_obj.register_new_user_link()
    r_obj.enter_firstname(f_name)
    r_obj.enter_lastname(l_name)
    r_obj.enter_email(email)
    r_obj.enter_password(pwd1)
    r_obj.click_checkbox()
    r_obj.click_reg_btn()
    try:
        r_obj.captcha_handle()
        print("capcha handled")
    except:
        print("no capcha found")



# pytest test_register_page.py -vs --html="path\report_name.html"
