from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Set up the WebDriver (make sure you have the correct ChromeDriver installed)
driver = webdriver.Chrome()

# Open a website
driver.get("https://www.google.com")

# Find the search box using its name attribute value
search_box = driver.find_element(By.NAME, "q")

# Type into the search box
search_box.send_keys("Selenium WebDriver")

# Press ENTER
search_box.send_keys(Keys.RETURN)

# Wait a few seconds to see the results
import time
time.sleep(5)

# Close the browser
driver.quit()
