from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import TimeoutException
import time
import os
import datetime
from webdriver_manager.chrome import ChromeDriverManager
import re

account = "UsernameYouWantToCheckFollowers"  # account from
page = "followers"  # from following or followers
page1= "following"
yourusername = "UsernameWhoLoginToCheck" #your IG username
yourpassword = "PasswordToLogin"  #your IG password


#for proxy i recommend 4G mobile proxy: http://www.virtnumber.com/mobile-proxy-4g.php
#PROXY = "http://84.52.54.2:8011" # IP:PORT or HOST:PORT
#options.add_argument('--proxy-server=%s' % PROXY)

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--user-agent="Mozilla/5.0 (iPhone; CPU iPhone OS 12_1_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/16D57"')

driver = webdriver.Chrome(ChromeDriverManager().install())


driver.get('https://www.instagram.com/accounts/login/')
sleep(3)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Accetta')]"))).click()
sleep(1)
username_input = driver.find_element_by_css_selector("input[name='username']")
password_input = driver.find_element_by_css_selector("input[name='password']")
username_input.send_keys(yourusername)
password_input.send_keys(yourpassword)
login_button = driver.find_element_by_xpath("//button[@type='submit']")
login_button.click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Non ora')]"))).click()
sleep(3)
          
driver.get('https://www.instagram.com/%s' % account)
sleep(2) 

print ("cerchiamo il numero di follow")
a= driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
b=a.text
countFollower= re.sub("[^0-9]", "",b)
print ("Numero di Follower" + countFollower)
countFollower= int(countFollower)
sleep(3)

print ("cerchiamo il numero di seguiti")
a= driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a')
b=a.text
countSeguiti= re.sub("[^0-9]", "",b)
print ("Numero di Seguiti" + countSeguiti)
countSeguiti=int(countSeguiti)
sleep(3)

driver.find_element_by_xpath('//a[contains(@href, "%s")]' % page).click()
scr2 = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
sleep(2)
text1 = scr2.text
print(text1)
x = datetime.datetime.now()
print(x)

#countFollower = 100  # number of profiles you want to get
for i in range(1,countFollower):
   scr1 = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/ul/div/li[%s]' % i)
   driver.execute_script("arguments[0].scrollIntoView();", scr1)
   sleep(1)
   text = scr1.text
   list = text.encode('utf-8').split()
   dirname = os.path.dirname(os.path.abspath(__file__))
   csvfilename = os.path.join(dirname, account + "-" + page + ".txt")
   file_exists = os.path.isfile(csvfilename)
   f = open(csvfilename,'a')
   f.write(str(list[0]) + "\r\n")
   f.close()
   print('{};{}'.format(i, list[0]))
   #print(i + ";" + list[0])
   if i == (countFollower-1):
     print(x)

listFollower = list


driver.find_element_by_xpath('//a[contains(@href, "%s")]' % page1).click()
scr2 = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
sleep(2)
text1 = scr2.text
print(text1)
x = datetime.datetime.now()
print(x)

#countSeguiti = 100  # number of profiles you want to get
for i in range(1,V):
   scr1 = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/ul/div/li[%s]' % i)
   driver.execute_script("arguments[0].scrollIntoView();", scr1)
   sleep(1)
   text = scr1.text
   list = text.encode('utf-8').split()
   dirname = os.path.dirname(os.path.abspath(__file__))
   csvfilename = os.path.join(dirname, account + "-" + page1 + ".txt")
   file_exists = os.path.isfile(csvfilename)
   f = open(csvfilename,'a')
   f.write(str(list[0]) + "\r\n")
   f.close()
   print('{};{}'.format(i, list[0]))
   #print(i + ";" + list[0])
   if i == (countSeguiti-1):
     print(x)


listFollowing = list