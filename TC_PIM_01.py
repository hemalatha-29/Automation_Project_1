from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrangeHRM:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 60)

    def login(self, username, password):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        username_input = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-input")))
        password_input = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-input--active")))
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "orangehrm-login-button")]')))

        username_input.send_keys("Admin")
        password_input.send_keys("admin123")
        login_button.click()

    def add_employee(self, input_name, employee_id):
        pim_module_link = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[2]/a')))
        pim_module_link.click()

        add_employee_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[1]/header/div[2]/nav/ul/li[3]')))
        add_employee_button.click()

        name_parts = input_name.split()
        first_name = name_parts[0]
        middle_name = name_parts[1] if len(name_parts) > 2 else ""
        last_name = name_parts[-1]

        employee_first_name_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[1]/div[2]/input')))
        employee_first_name_input.clear()
        employee_first_name_input.send_keys("John")

        employee_middle_name_input = self.wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[2]/div[2]/input')))
        employee_middle_name_input.clear()
        employee_middle_name_input.send_keys("Deo")

        employee_last_name_input = self.wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[1]/div/div/div[2]/div[3]/div[2]/input')))
        employee_last_name_input.clear()
        employee_last_name_input.send_keys("Smith")

        employee_id_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')))
        employee_id_input.clear()
        employee_id_input.send_keys(employee_id)

        save_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]')))
        save_button.click()

        success_message = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="oxd-toaster_1"]')))
        print("Successful employee addition:", success_message.text)

    def quit_driver(self):
        self.driver.quit()



if __name__ == "__main__":
    orangehrm = OrangeHRM()
    orangehrm.login("Admin", "admin123")
    orangehrm.add_employee("John Deo Smith", "12345")
    orangehrm.quit_driver()
