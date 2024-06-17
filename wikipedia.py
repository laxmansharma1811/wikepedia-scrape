from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
url = driver.get("https://www.wikipedia.org/")
time.sleep(5)

search_box = driver.find_element(By.ID, "searchInput")
search_box.send_keys("Python")
time.sleep(5)
word = search_box.send_keys(Keys.ENTER)
print('******************************************')

current_url = driver.current_url

print('-----------------------------------------')

print(current_url)

driver.get(current_url)

time.sleep(5)

try:
    content_element = driver.find_element(By.CLASS_NAME, "mw-parser-output")

    all_elements = content_element.find_elements(By.XPATH, ".//*")

    for element in all_elements:
        element_text = element.text.strip()
        if element_text:
            print(element_text)

except Exception as e:
    print(f"Error finding content: {e}")

driver.quit()