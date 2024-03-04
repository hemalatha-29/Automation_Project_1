from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class OrangeHRMTest:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 60)

    def login(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        username_input = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-input")))
        password_input = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-input--active")))
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "orangehrm-login-button")]')))
        username_input.send_keys("Admin")
        password_input.send_keys("admin123")
        login_button.click()

    def navigate_to_pim_module(self):
        pim_module_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')))
        pim_module_link.click()

    def edit_employee_information(self):
        employee_list_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[9]/div/button[2]/i')))
        employee_list_link.click()
        first_employee_checkbox = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[1]/div[2]/input')))
        first_employee_checkbox.click()
        edit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[1]/div[2]/input')))
        edit_button.click()
        first_name_field = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,'#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > div > div.orangehrm-edit-employee-content > div.orangehrm-horizontal-padding.orangehrm-vertical-padding > form > div:nth-child(1) > div > div > div > div.--name-grouped-field > div:nth-child(1) > div:nth-child(2) > input')))
        first_name_field.send_keys(Keys.CONTROL + "a")  # Select all text
        first_name_field.send_keys(Keys.DELETE)
        first_name_field.send_keys("JOHN DOE")
        save_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/button|//button[@class="oxd-button oxd-button--medium oxd-button--secondary orangehrm-left-space"]')))
        save_button.click()
        success_message = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oxd-toaster_1"]')))
        print("successful employee details addition Message:", success_message.text)

    def run_test(self):
        self.login()
        self.navigate_to_pim_module()
        self.edit_employee_information()
        self.driver.quit()

test = OrangeHRMTest()
test.run_test()
