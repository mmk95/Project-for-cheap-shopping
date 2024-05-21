from selenium import webdriver
import csv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

chrome_options = webdriver.ChromeOptions()  
chrome_options.add_argument('--headless')     
service = Service(executable_path=r"Your_Path_Of/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

csv_file_path = 'urls.csv'
urls = []
with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        urls.extend(row)

filtered_urls = [url for url in urls if 'zoldseg_gyumolcs' in url]

counter = 1

for url in filtered_urls:
    driver.get(url)

    try:
        cookie_dialog = WebDriverWait(driver, 3).until(
            EC.presence_of_element_located((By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"))
        )
        cookie_dialog.click()
    except TimeoutException:
        print("Cookie dialog not found or already accepted.")
        pass

    def click_button_and_wait():
        button_xpath = '//*[@id="layout-content"]/div[2]/div[2]/div[3]/button'
        try:
            button = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, button_xpath))
            )
            button.click()
            WebDriverWait(driver, 3).until(EC.invisibility_of_element_located((By.XPATH, button_xpath)))
        except Exception as e:
            print(f"Error clicking the button: {e}")

    while True:
        click_button_and_wait()
        try:
            driver.find_element(By.XPATH, '//*[@id="layout-content"]/div[2]/div[2]/div[3]/button')
        except NoSuchElementException:
            break

    xpath = '//*[@id="layout-content"]/div[2]/div[2]/div[2]'
    element = driver.find_element(By.XPATH, xpath)

    xpath_to_append_group = '//*[@id="layout-content"]/div[1]/nav/ol/li[2]/span'
    group_value = driver.find_element(By.XPATH, xpath_to_append_group)
    group = group_value.text

    xpath_to_append_categ = '//*[@id="layout-content"]/div[1]/nav/ol/li[3]/a'
    categ_value = driver.find_element(By.XPATH, xpath_to_append_categ)
    categ = categ_value.text

    xpath_to_append_name = '//*[@id="layout-content"]/div[1]/nav/ol/li[4]/span'
    name_value = driver.find_element(By.XPATH, xpath_to_append_name)
    name = name_value.text
  
    data = element.text.split('\n')
    data.append(group)
    data.append(categ)
    data.append(name)

    csv_file_name = f'fruit{counter}.csv'
    csv_file_path = f'../Project/files/Gyümölcs_termékek/{csv_file_name}'
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=';')
        row_data = []
        for item in data:
            
            if '-tól' in item:
                continue
            if 'Bevásárlólistához adom' in item:
                if row_data:
                    csv_writer.writerow(row_data)
                    row_data = []
            else:
                row_data.append(item)

        if row_data:
            csv_writer.writerow(row_data)

    print(f"Data from {url} has been saved to {csv_file_path}")

    counter += 1

driver.quit()
