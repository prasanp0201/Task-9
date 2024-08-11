from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# # Setting up the WebDriver (using Chrome here, but it can be any browser)
# options = webdriver.Chrome
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
# options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome()

try:
    # Open the webpage
    driver.get("https://www.saucedemo.com/")

    # Find the username and password fields and input the credentials
    username_field = driver.find_element(By.ID, "user-name")
    password_field = driver.find_element(By.ID, "password")

    username_field.send_keys("standard_user")
    password_field.send_keys("secret_sauce")
    password_field.send_keys(Keys.RETURN)

    # Wait for the page to load
    time.sleep(5)

    # Fetch the title of the web page
    title = driver.title

    # Fetch the current URL of the web page
    current_url = driver.current_url

    # Extract the entire contents of the webpage
    page_source = driver.page_source

    # Save the contents to a text file
    file_path = 'Webpage_task_11.txt'
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(page_source)

    # Output the results
    print(f"Title: {title}")
    print(f"Current URL: {current_url}")
    print(f"Content saved to: {file_path}")

finally:
    # Close the WebDriver
    driver.quit()