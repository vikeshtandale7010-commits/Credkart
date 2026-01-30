"""
Testcases :
1. Login
2. Registration
3. Checkout
4. Amount Verification
5. Login with params
6. Login with Excel
7. Registration wih params
8. Registration with Excel

Mostly all you are Sanity and Smoke testcases are in automation list.
"""
import pytest
from faker import Faker
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.Login_Page import Login_Page_Class
from pageObjects.Registration_Page import Registration_Page_Class
from utilities.Logger import log_generator_class
from utilities.ReadProperties import ReadConfigClass


@pytest.mark.usefixtures("browser_setup") # New
class Test_User_Profile :
    driver = None
    email = ReadConfigClass.get_data_for_email()
    password  = ReadConfigClass.get_data_for_password()
    login_url = ReadConfigClass.get_data_for_login_url()
    registration_url =ReadConfigClass.get_data_for_registration_url()
    log = log_generator_class.log_gen_method()

    @pytest.mark.smoke
    @pytest.mark.flaky(reruns=1, rerun_delay=1)
    @pytest.mark.dependency(name = "test_verify_Credkart_url_001")
    @pytest.mark.order(1)
    def test_verify_Credkart_url_001(self):
        # self.log.debug("This is debug log")
        # self.log.info("This is info log")
        # self.log.warning("This is warning log")
        # self.log.error("This is error log")
        # self.log.critical("This is critical log")
        self.log.info("Testcase test_verify_Credkart_url_001 is started")
        self.driver.get(self.login_url)
        self.log.info(f"Opening browser and getting {self.login_url}")
        self.log.info(f"Checking driver title")
        if self.driver.title == "CredKart":
            self.log.info(f"Testcase test_verify_Credkart_url_001 is passed")
            self.log.info(f"Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_verify_Credkart_url_001_pass.png")
        else:
            self.log.info(f"Testcase test_verify_Credkart_url_001 is failed")
            self.log.info(f"Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\test_verify_Credkart_url_001_fail.png")
            assert False
        self.log.info(f"Testcase test_verify_Credkart_url_001 is completed")

    @pytest.mark.smoke
    @pytest.mark.flaky(reruns=1, rerun_delay=1)
    #@pytest.mark.dependency(depends=["test_verify_Credkart_url_001"])
    @pytest.mark.order(2)
    def test_Credkart_login_002(self):
        self.log.info("Testcase test_Credkart_login_002 is started")
        self.driver.get(self.login_url)
        self.log.info(f"Opening browser and getting {self.login_url}")

        # email_id = "Credencetest@test.com"
        # pass_word = "Credence@123"
        self.lp = Login_Page_Class(self.driver) # login page class object and now we can access the methods

        # Enter Username
        # email = self.driver.find_element(By.XPATH, "//input[@id='email']")
        # email.send_keys(email_id)
        self.log.info(f"Entering the Email {self.email}")
        self.lp.Enter_Email(self.email)


        # Enter Password
        # password = self.driver.find_element(By.XPATH, "//input[@id='password']")
        # password.send_keys(pass_word)
        self.log.info(f"Entering the password")
        self.lp.Enter_Password(self.password)

        # Click on Login button
        # login_button = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        # login_button.click()
        self.log.info(f"Clicking on login button")
        self.lp.Click_Login_Register_Button()

        # wait = WebDriverWait(self.driver, 5)
        # try:
        #     wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div/div[1]/p[1]")))
        #     element = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]")
        #     print("User Login Successful")
        #     # driver.save_screenshot(f"User Login Successful_{email_id}.png")
        #     menu = self.driver.find_element(By.XPATH, "//a[@role='button']")
        #     menu.click()
        #     logout = self.driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
        #     logout.click()
        #
        #
        # except:
        #     print("User Login Fail")
        #     # driver.save_screenshot(f"User Login Fail_{email_id}.png")
        #     assert False, "User Login Fail"

        self.log.info(f"Checking the login status")
        if self.lp.verify_menu_button_visibility() == "pass":
            self.log.info(f"User login successful and taking screenshot")
            self.driver.save_screenshot(f".\\Screenshots\\User Login Successful_{self.email}.png")
            self.log.info(f"Clicking on menu button")
            self.lp.Click_Menu_button()
            self.log.info(f"Clicking on logout button")
            self.lp.Click_Logout_button()
        else:
            self.log.info(f"User login fail and taking screenshot")
            self.driver.save_screenshot(f".\\Screenshots\\User Login Fail_{self.email}.png")
            assert False, "User Login Fail"
        self.log.info(f"Testcase test_Credkart_login_002 is completed")

    @pytest.mark.smoke
    @pytest.mark.flaky(reruns=1, rerun_delay=1)
    #@pytest.mark.dependency(depends=["test_verify_Credkart_url_001"])
    @pytest.mark.order(3)
    def test_Credkart_registration_003(self):
        self.log.info("Testcase test_Credkart_login_002 is started")
        self.driver.get(self.registration_url)
        self.log.info(f"Opening browser and getting {self.registration_url}")
        fake_username = Faker().user_name()# New
        fake_email = Faker().email()# New
        self.log.info(f"Generated fake data for username--> {fake_username} and email --> {fake_email}")
        password_data = "Credence_user_101@123"
        self.rp = Registration_Page_Class(self.driver)
        # Enter Username
        self.log.info(f"Entering the Username--> {fake_username}")
        self.rp.Enter_Name(fake_username)
        # Enter Email
        self.log.info(f"Entering the Email--> {fake_email}")
        self.rp.Enter_Email(fake_email)
        # Enter Password
        self.log.info("Entering the Password")
        self.rp.Enter_Password(password_data)
        # Enter Confirm Password
        self.log.info("Entering the Confirm Password")
        self.rp.Enter_Confirm_Password(password_data)
        # Click on register button
        self.log.info("Clicking on register button")
        self.rp.Click_Login_Register_Button()

        if self.rp.verify_menu_button_visibility() == "pass":
            self.log.info(f"User registration successful and taking screenshot")
            self.driver.save_screenshot(f".\\Screenshots\\User Registration Successful_{fake_username}.png")
            self.log.info(f"Clicking on menu button")
            self.rp.Click_Menu_button()
            self.log.info(f"Clicking on logout button")
            self.rp.Click_Logout_button()
        else:
            self.log.info(f"User registration fail and taking screenshot")
            self.driver.save_screenshot(f".\\Screenshots\\User Registration Fail_{fake_username}.png")
            assert False, "User Registration Fail"
        self.log.info(f"Testcase test_Credkart_registration_003 is completed")

# pytest -v -s -n=auto --html=Html_reports\my_report_28th_jan_2026.html

# 27th jan 2026 --> config, readproperties, html report environment, logger
# 28th logger, excel, rerun failure, markers, dependency, order

# pip install pytest-dependency to create dependency in testcases.
# pip install pytest-order

# 29th jan 2026
# allure report - 15 mints
# jenkins  - installation 30 mints
# git  - installation 30 mints

# 30th Jan 2026--> orange hrm
# 6 am to 9 am

# 1st Feb --> Hr session
# 2nd Feb --> Hr session

# ETL Revision --> After 8th feb


# Batch#23-->