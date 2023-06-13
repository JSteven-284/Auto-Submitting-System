import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from ctypes import windll
from selenium.common.exceptions import NoAlertPresentException
import traceback
import ddddocr

def getInfoList():
    # Set Environment
    browser = webdriver.Chrome(executable_path = "C:\Program Files\Google\Chrome\Application\chromedriver.exe")
    chromedriver = "C:\Program Files (x86)\Google\Chrome\Application"
    os.environ["webdriver.ie.driver"] = chromedriver
    
    driver=webdriver.Chrome()
    driver.get('https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx') 
    driver.maximize_window()
    # alert
    # try:
    #     alert1 = driver.switch_to.alert 
    # except NoAlertPresentException as e:
    #     print("no alert")
    #     traceback.print_exc()
    # else:
    #     at_text1 = alert1.text
    #     print("at_text:" + at_text1)

    time.sleep(1)
    
    username = "username" # your own username
    password = "password" # your own password
        
    usernameBar = driver.find_element(By.XPATH, '//*[(@id = "email")]')
    usernameBar.click()
    usernameBar.clear()
    usernameBar.send_keys(username)
    
    passwordBar = driver.find_element(By.XPATH, '//*[(@id = "pwd")]')
    passwordBar.click()
    passwordBar.clear()
    passwordBar.send_keys(password)

    # verification code
    if os.path.exists("imgcode.png"):
        os.remove("imgcode.png")
    code = driver.find_element(By.XPATH, '//*[(@id = "code")]')
    img = driver.find_element(By.XPATH, '//*[(@id = "imgCode")]')
    img.screenshot("imgcode.png")
    time.sleep(1)

    ocr = ddddocr.DdddOcr()
    with open("imgcode.png", "rb") as fp:
        image = fp.read()
    catch = ocr.classification(image)
    code.send_keys(catch)
    time.sleep(1)

    # login
    login = driver.find_element(By.XPATH, '//*[(@id = "denglu")]')
    login.click()

    time.sleep(1)

    # getInfo
    shiwen = driver.find_element(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "son1", " " ))]//a[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]')
    shiwen.click()
    time.sleep(1)

    xiexue = driver.find_element(By.XPATH, '//*[(@id = "right1")]//a[(((count(preceding-sibling::*) + 1) = 22) and parent::*)]')
    xiexue.click()
    time.sleep(1)

    ip1 = driver.find_element(By.XPATH, '//span[(((count(preceding-sibling::*) + 1) = 1) and parent::*)]//a')
    ip2 = driver.find_element(By.XPATH, '//span[(((count(preceding-sibling::*) + 1) = 2) and parent::*)]//a')
    exactTime = driver.find_element(By.XPATH, '//span[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]//a')
    attackMethod = driver.find_element(By.XPATH, '//span[(((count(preceding-sibling::*) + 1) = 6) and parent::*)]//a')
    
    infoList = [ip1.text, ip2.text, exactTime.text, attackMethod.text]
    print(infoList)
    # screenshots
    folderPath = "D:\common\Current\ASS_test\img"
    del_files(folderPath)

    driver.get_screenshot_as_file("D:\common\Current\ASS_test\img\图片一.png")
    driver.find_element(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "son1", " " ))]//a[(((count(preceding-sibling::*) + 1) = 3) and parent::*)]').click()
    driver.get_screenshot_as_file("D:\common\Current\ASS_test\img\图片二.png")
    driver.find_element(By.XPATH, '//*[contains(concat( " ", @class, " " ), concat( " ", "son1", " " ))]//a[(((count(preceding-sibling::*) + 1) = 5) and parent::*)]').click()
    driver.get_screenshot_as_file("D:\common\Current\ASS_test\img\图片三.png")
    
    driver.quit()
    return infoList

def del_files(folder_path):

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        
        # Check if it is a file and delete it
        if os.path.isfile(file_path):
            os.remove(file_path)
