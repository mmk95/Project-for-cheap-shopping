from selenium import webdriver
import csv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

chrome_options = webdriver.ChromeOptions()    
service = Service(executable_path=r"Your_Path_Of/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.maximize_window()

url = 'https://arfigyelo.gvh.hu'
driver.get(url)

cookie_dialog = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))
)
cookie_dialog.click()

with open('../Project/urls.csv', 'w', newline='') as csvfile:
    fieldnames = ['URL']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(1, 7):
        xpath = f'//*[@id="main-menu"]/div/div[{i}]/div[1]'
        
        try:
            elements = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            elements.click()
        except NoSuchElementException:
            print(f"Element {xpath} not clickable")
            continue
        
        for j in range(1, 10):
            category_xpath = f'//*[@id="main-menu"]/div/div[{i}]/div[3]/div/div/div[2]/div[1]/div[{j}]'
            
            try:                
                elements1 = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, category_xpath))
                )
                elements1.click()
            except NoSuchElementException:
                continue
            
            for k in range(3, 10):
                product_xpath = f'//*[@id="main-menu"]/div/div[{i}]/div[3]/div/div/div[2]/div[2]/div/div/div[{k}]/div'
                
                try:
                    elements2 = WebDriverWait(driver, 10).until(
                        EC.element_to_be_clickable((By.XPATH, product_xpath))
                    )
                    elements2.click()
                    current_url = driver.current_url
                    writer.writerow({current_url})
                    elements.click()
                    elements1.click()
                    
                except NoSuchElementException:
                    continue

driver.quit()
