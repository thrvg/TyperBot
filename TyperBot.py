from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Typing test URL
url = "https://10fastfingers.com/typing-test/english"

# Path to local Chromedriver
path_var = "D:\\chromedriver.exe" 
driver = webdriver.Chrome(path_var)

# Open website and wait
driver.get(url)
driver.implicitly_wait(45)

# Type
textfield = driver.find_element(By.ID, "inputfield")
while True:
    try:
        texttotype = driver.find_element(By.CLASS_NAME, "highlight").text + ' '
        textfield.send_keys(texttotype)
    except Exception as e:
        # Exception occurs if no more words left to type
        print('Over')
        break
