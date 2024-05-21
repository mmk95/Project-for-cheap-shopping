from selenium import webdriver
import csv
import os 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()  
#chrome_options.add_argument('--headless')     
service = Service(executable_path=r"Your_Path_Of/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

url = 'https://arfigyelo.gvh.hu'
driver.get(url)



cookie_dialog = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))
)
cookie_dialog.click()

csv_file_path = '../Project/files/category_name.csv'
if os.path.exists(csv_file_path):
    os.remove(csv_file_path)
categories = []    
for i in range(1, 7):
    groups = []
    xpath = f'//*[@id="main-menu"]/div/div[{i}]/div[1]'    
    elements = driver.find_element(By.XPATH, xpath)
    data = elements.text.split('\n')
    actions = ActionChains(driver)
    actions.move_to_element(elements).perform()
    for j in range(1,10):
        category_xpath=f'//*[@id="main-menu"]/div/div[{i}]/div[3]/div/div/div[2]/div[1]/div[{j}]/div'
        categories = driver.find_elements(By.XPATH, category_xpath)
        for element in categories:
            value = element.text
            groups.append(value)

    with open(csv_file_path, 'a', newline='', encoding='utf-8') as csv_file:  # Open in append mode
        csv_writer = csv.writer(csv_file, delimiter=';')
        for item in groups:
            csv_writer.writerow([item]+data)
driver.quit()
