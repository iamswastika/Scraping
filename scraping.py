from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# import cv2
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time     

# options = Options()
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
# driver = webdriver.Chrome(PATH, service = Service(ChromeDriverManager().install()), options = options)
# url = "https://www.techwithtim.net"
# driver.get(url)

driver.get("https://orteil.dashnet.org/cookieclicker/")
driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigcookie")
cookie_count = driver.find_element_by_id("cookies")
items = [driver.find_element_by_id("productPrice" +str(i)) for i in range(1, -1, -1)]

actions = ActionChains(driver)
actions.click(cookie)
