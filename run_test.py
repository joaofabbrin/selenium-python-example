from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://www.selenium.dev/")
driver.maximize_window()

time.sleep(2)

download_link = driver.find_element(By.LINK_TEXT, "Downloads")
download_link.click()

time.sleep(2)

print("Título da página:", driver.title)

driver.quit()
