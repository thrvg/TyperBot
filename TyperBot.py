from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
url = "https://10fastfingers.com/typing-test/english"
path_var = "D:\\chromedriver.exe"
driver = webdriver.Chrome(path_var)
driver.get(url)
driver.implicitly_wait(45)
textfield = driver.find_element(By.ID, "inputfield")
while True:
    try:
        texttotype = driver.find_element(By.CLASS_NAME, "highlight").text + ' '
        textfield.send_keys(texttotype)
    except Exception as e:
        print('Over')
        break
