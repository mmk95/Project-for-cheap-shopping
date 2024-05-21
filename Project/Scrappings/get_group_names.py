from selenium import webdriver
import csv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()  
chrome_options.add_argument('--headless')     
service = Service(executable_path=r"Your_Path_Of/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

url = 'https://arfigyelo.gvh.hu'
driver.get(url)



cookie_dialog = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))
)
cookie_dialog.click()

groups = []    
for i in range(1, 7):
    xpath = f'//*[@id="main-menu"]/div/div[{i}]/div[1]/span'
    elements = driver.find_elements(By.XPATH, xpath)
    for element in elements:
            value = element.text
            groups.append(value)
driver.quit()

csv_file_path = '../Project/files/group_names.csv'
with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=';')
    for item in groups:
        csv_writer.writerow([item])

print(f"Data has been saved to {csv_file_path}")