
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
from utilities.XLUtils import Excel_methods


@pytest.mark.usefixtures("browser_setup") # New
class Test_User_Profile :
    driver = None
    email = ReadConfigClass.get_data_for_email()
    password  = ReadConfigClass.get_data_for_password()
    login_url = ReadConfigClass.get_data_for_login_url()
    registration_url =ReadConfigClass.get_data_for_registration_url()
    log = log_generator_class.log_gen_method()
    excel_path = ".\\Test_Data\\Credkart_Test_Data.xlsx"
    sheet_name = "login_data"

    @pytest.mark.smoke
    @pytest.mark.flaky(reruns = 1, rerun_delay = 1)
    #@pytest.mark.dependency(depends=["test_verify_Credkart_url_001"])
    @pytest.mark.order(4)
    def test_Credkart_login_excel_ddt_004(self):
        self.log.info("Testcase test_Credkart_login_excel_ddt_004 is started")
        self.lp = Login_Page_Class(self.driver) # login page class object and now we can access the methods
        self.log.info("Reading data from excel")
        self.rows = Excel_methods.get_count_rows(self.excel_path, self.sheet_name)
        self.log.info(f"Number of rows in excel is {self.rows}")

        result_list = []
        for i in range(2,self.rows +1):
            self.driver.get(self.login_url)
            self.log.info(f"Opening browser and getting {self.login_url}")
            self.email = Excel_methods.read_data_from_excel(self.excel_path, self.sheet_name,i, 2)
            self.password = Excel_methods.read_data_from_excel(self.excel_path, self.sheet_name,i, 3)
            self.expected_result = Excel_methods.read_data_from_excel(self.excel_path, self.sheet_name,i, 4)

            self.log.info(f"Entering the Email {self.email}")
            self.lp.Enter_Email(self.email)
            self.log.info(f"Entering the password")
            self.lp.Enter_Password(self.password)
            self.log.info(f"Clicking on login button")
            self.lp.Click_Login_Register_Button()
            self.log.info(f"Checking the login status")
            if self.lp.verify_menu_button_visibility() == "pass" :
                self.log.info(f"User login successful and taking screenshot")
                self.driver.save_screenshot(f".\\Screenshots\\User Login Successful_{self.email}.png")
                self.log.info(f"Clicking on menu button")
                self.lp.Click_Menu_button()
                self.log.info(f"Clicking on logout button")
                self.lp.Click_Logout_button()
                actual_result = "login_pass"
                Excel_methods.write_data_from_excel(self.excel_path, self.sheet_name, i, 5, actual_result)
            else:
                self.log.info(f"User login fail and taking screenshot")
                self.driver.save_screenshot(f".\\Screenshots\\User Login Fail_{self.email}.png")
                actual_result = "login_fail"
                Excel_methods.write_data_from_excel(self.excel_path, self.sheet_name, i, 5, actual_result)

            if self.expected_result == actual_result:
                Test_status = "Pass"
                Excel_methods.write_data_from_excel(self.excel_path, self.sheet_name, i, 6, Test_status)
            else :
                Test_status = "Fail"
                Excel_methods.write_data_from_excel(self.excel_path, self.sheet_name, i, 6, Test_status)

            result_list.append(Test_status)

        if "Fail" not in result_list:
            self.log.info("All the testcases are passed")
        else:
            self.log.info("Some of the testcases are failed")
            assert False

        self.log.info(f"Testcase test_Credkart_login_excel_ddt_004 is completed")

#