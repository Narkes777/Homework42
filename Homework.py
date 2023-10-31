# # ---Task 1---
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Chrome(executable_path='путь_к_вашему_chromedriver.exe')

# driver.get('URL_с_курсами_валют')

# time.sleep(5)

# currency_elements = driver.find_elements(By.XPATH, 'XPATH_элементов_с_курсами')

# for element in currency_elements:
#     print(element.text)

# driver.quit()

# ---Task 2---
# driver = webdriver.Chrome(executable_path='путь_к_вашему_chromedriver.exe')

# driver.get('URL_маркетплейса')

# time.sleep(5)

# price_elements = driver.find_elements(By.XPATH, 'XPATH_элементов_с_ценами')

# for element in price_elements:
#     print(element.text)

# driver.quit()
