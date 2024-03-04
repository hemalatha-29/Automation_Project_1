from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

username = "Admin"
username_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "oxd-input")))
username_field.clear()
username_field.send_keys("Admin")

password = "incorrect_password"
password_field = driver.find_element(By.CLASS_NAME, "oxd-input--active")
password_field.clear()
password_field.send_keys(password)

login_button = driver.find_element(By.XPATH, '//button[contains(@class, "orangehrm-login-button")]')
login_button.click()

try:
    error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "spanMessage")))
    print("Login failed! Reason:", error_message.text)
except:
    print("Login failed! invaild credential.")

driver.quit()
