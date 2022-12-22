from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


#this is where i open a new window
driver = webdriver.Chrome()
#this is where i open facebook
driver.get ('https://www.facebook.com/')
# this is where i start entering my username and password.
driver.find_element(By.ID,"email").send_keys(usernam)
driver.find_element(By.ID,"pass").send_keys(password)
driver.find_element(By.NAME,"email").click() # I click login button
# login process done I am now on facebook
time.sleep(1)
# i start navigating to message and click on the friend i wanna messsage
mesgAdd='https://www.facebook.com/messages/t/'
mesgLink=mesgAdd+frndId
driver.get(mesgLink)
time.sleep (1)
#This is Where I clicked the Send Message '
driver.find_element(By.PATH,('//div[@class="_1mf _1mj"]')).send_keys(message, Keys.ENTER)



asdjknsajdnasjldlsdknfjkds
sdjflndsljkfnkldfjklds
lkjsdnflkjsdlkfndskljj
