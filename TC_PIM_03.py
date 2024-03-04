import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TC_PIM_03 (unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        username_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-input")))
        password_input = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-input--active")))
        login_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "orangehrm-login-button")]')))
        username_input.send_keys("Admin")
        password_input.send_keys("admin123")
        login_button.click()

    def test_delete_employee(self):
        self.login()

        pim_module = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')))
        pim_module.click()

        employee_list_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a')))
        employee_list_element.click()

        employee_list = self.driver.find_elements(By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div')

        if len(employee_list) > 0:
            employee_to_delete = employee_list[0]
            delete_button = employee_to_delete.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[1]')
            delete_button.click()

            delete_button_confirm = self.driver.find_element(By.CLASS_NAME, "oxd-icon bi-trash")
            delete_button_confirm.click()

            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, "dialogDeleteBtn")))
            confirm_delete_button = self.driver.find_element(By.ID, "dialogDeleteBtn")
            confirm_delete_button.click()

            success_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//*[@id="oxd-toaster_1"]')))
            self.assertIn("Successfully Deleted", success_message.text)

    def tearDown(self):
        try:
            self.driver.quit()
        finally:
            print("SUCCESSFULLY DELETED")


if __name__ == "__main__":
    unittest.main()