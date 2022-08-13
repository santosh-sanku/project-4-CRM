from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import time
import requests

class main():

    url = "https://opensource-demo.orangehrmlive.com/"
    driver = webdriver.Firefox()

    def open_webpage(self):
        self.driver.get(self.url)
        self.driver.find_element(by=By.ID,value='txtUsername').send_keys("Admin")
        self.driver.find_element(by=By.ID,value='txtPassword').send_keys("admin123")
        time.sleep(2)
        self.driver.find_element(by=By.ID,value='btnLogin').click()
        time.sleep(2)

    
    def pim_add_employee(self):
        self.open_webpage()
        time.sleep(3)

        a_t = self.driver.find_element(by=By.ID,value='menu_pim_viewPimModule')
        act = ActionChains(self.driver)
        act.move_to_element(a_t).perform()
        self.driver.find_element(by=By.ID,value='menu_pim_addEmployee').click()
        time.sleep(2)

        self.driver.find_element(by=By.ID,value='firstName').send_keys("")
        self.driver.find_element(by=By.ID,value='middleName').send_keys("")
        self.driver.find_element(by=By.ID,value='lastName').send_keys("")
        self.driver.find_element(by=By.ID,value='employeeId').send_keys("")
        self.driver.find_element(by=By.ID,value='btnSave').click()
        time.sleep(3)
        

        """ personal details edit """
        self.driver.find_element(by=By.ID,value='btnSave').click()
        time.sleep(2)
        self.driver.find_element(by=By.ID,value='personal_optGender_1').click() # male
        
        marital_status = self.driver.find_element(by=By.ID,value='personal_cmbMarital')
        marital_var = Select(marital_status)
        marital_var.select_by_value('Single')

        national = self.driver.find_element(by=By.ID,value='personal_cmbNation')
        national_var = Select(national)
        national_var.select_by_visible_text("Indian")
        
        self.driver.find_element(by=By.ID,value='btnSave').click()
        time.sleep(3)

        # click on the dashboard
        self.driver.find_element(by=By.ID,value='menu_dashboard_index').click()
        time.sleep(3)
        self.driver.close()


    def pim_employee_list(self):
        self.open_webpage()
        time.sleep(2)

        a_t = self.driver.find_element(by=By.ID,value='menu_pim_viewPimModule')
        a_t1 = self.driver.find_element(by=By.ID,value='menu_pim_viewEmployeeList')
        act = ActionChains(self.driver)
        act.move_to_element(a_t).perform()
        a_t1.click()
        time.sleep(3)
        self.driver.close()




    def admin_click(self):
        time.sleep(1)
        
        a_t = self.driver.find_element(by=By.ID,value='menu_admin_viewAdminModule')
        a_t1 = self.driver.find_element(by=By.ID,value='menu_admin_UserManagement')

        act = ActionChains(self.driver)
        act.move_to_element(a_t).perform()
        act.move_to_element(a_t1).perform()
        self.driver.find_element(by=By.ID,value='menu_admin_viewSystemUsers').click()


        self.driver.find_element(by=By.ID,value='btnAdd').click()

        user_role = self.driver.find_element(by=By.ID,value='systemUser_userType')
        select_var = Select(user_role)
        select_var.select_by_visible_text("ESS")
        time.sleep(2)

        self.driver.find_element(by=By.ID,value='systemUser_employeeName_empName').send_keys("")
        self.driver.find_element(by=By.ID,value='systemUser_userName').send_keys("")

        status_role = self.driver.find_element(by=By.ID,value='systemUser_status')
        select_var2 = Select(status_role)
        select_var2.select_by_value('1')

        self.driver.find_element(by=By.ID,value='systemUser_password').send_keys("user1password")
        self.driver.find_element(by=By.ID,value='systemUser_confirmPassword').send_keys("user1password")
        self.driver.find_element(by=By.ID,value='btnSave').click()


    def leave_reports_entitlements(self):
        self.open_webpage()
        time.sleep(2)

        a_t = self.driver.find_element(by=By.ID,value='menu_leave_viewLeaveModule')
        # to generate leave reports
        a_t1 = self.driver.find_element(by=By.ID,value='menu_leave_Reports')
        act = ActionChains(self.driver)
        act.move_to_element(a_t).perform()
        act.move_to_element(a_t1).perform()
        self.driver.find_element(by=By.ID,value='menu_leave_viewLeaveBalanceReport').click()
        time.sleep(2)

        generate_for = self.driver.find_element(by=By.ID,value='leave_balance_report_type')
        generate = Select(generate_for)
        generate.select_by_value("2")
        # Employee
        self.driver.find_element(by=By.ID,value='leave_balance_employee_empName').send_keys("Aaliyah Haq")
        self.driver.find_element(by=By.ID,value='viewBtn').click()
        time.sleep(4)
        



s = main()
time.sleep(3)
s.pim_employee_list()


