from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OrangeHRMLogin:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.username = "Admin"
        self.password = "admin123"

    def login(self):
        username_field = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-input")))
        username_field.clear()
        username_field.send_keys(self.username)

        password_field = self.driver.find_element(By.CLASS_NAME, "oxd-input--active")
        password_field.clear()
        password_field.send_keys(self.password)

        login_button = self.driver.find_element(By.XPATH, '//button[contains(@class, "orangehrm-login-button")]')
        login_button.click()

        print("Login successful!")

    def close_browser(self):
        self.driver.quit()

# Usage:
if __name__ == "__main__":
    orangehrm_login = OrangeHRMLogin()
    orangehrm_login.login()
    orangehrm_login.close_browser()

