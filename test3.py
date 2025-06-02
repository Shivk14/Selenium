from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Start Chrome browser
driver = webdriver.Chrome()

# Go to the login page
driver.get("https://the-internet.herokuapp.com/login")

# Find and fill in the username
username_input = driver.find_element(By.ID, "username")
username_input.send_keys("tomsmith")

# Find and fill in the password
password_input = driver.find_element(By.ID, "password")
password_input.send_keys("SuperSecretPassword!")

# Click the login button
login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()

# Wait to see the result
time.sleep(5)

# Close the browser
driver.quit()
