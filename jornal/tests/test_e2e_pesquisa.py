from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import sys

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://127.0.0.1:8000/")

try:
    WebDriverWait(driver, 5).until (
        EC.presence_of_all_elements_located((By.ID, "openSearchButton"))
    )
    print("\nElemento encontrado")

except TimeoutException:
    print("\nElemento não encontrado\n")
    sys.exit(1)

open_search = driver.find_element(By.ID, "openSearchButton")
open_search.click()

seach_input = driver.find_element(By.ID, "searchInput")
seach_input.clear()
seach_input.send_keys("CCJ" + Keys.ENTER)

noticia_link = driver.find_element(By.PARTIAL_LINK_TEXT, "CCJ")
noticia_link.click()

try:
    WebDriverWait(driver, 5).until (
        EC.url_contains("noticia/CCJ")
    )
    print("\nUrl correta")

except TimeoutError:
    print("\nUrl incorreta\n")
    sys.exit(1)

print("\nTeste concluido com exito\n")

driver.quit