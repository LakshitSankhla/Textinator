from selenium import webdriver
import time
from keyboard import press

driver_path = r'C:\Users\lakshya\PycharmProjects\geckodriver.exe'
driver = webdriver.Firefox(executable_path=driver_path)
driver.get('https://www.instagram.com/')
time.sleep(5)

username=input("Enter Username: ")
password=input("Enter Password: ")


driver.find_element_by_xpath("//input[@name = 'username']").send_keys(username)       #Enters username
driver.find_element_by_xpath("//input[@name = 'password']").send_keys(password)       #Enters password
driver.find_element_by_xpath("//button[@type='submit']").click()                      #LogIn Button
time.sleep(10)

driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()   #Not Now Button

driver.find_element_by_class_name("xWeGp").click()
time.sleep(5)

driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div/button').click()
name = input("Enter name: ")
first_name, last_name = name.split()
filename = input("Enter filename: ")
input("Enter 1 after scanning the code: ")
fh = open(filename)

driver.find_element_by_xpath("//input[@placeholder='Search...']").send_keys(name)
time.sleep(2)

driver.find_element_by_xpath("/html/body/div[4]/div/div[2]/div[2]/div[1]/div").click()
driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/div/button").click()
time.sleep(5)

driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").click()

msg = ''
for line in fh:
    for word in line.split():
        msg = word
        driver.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea').send_keys(msg)
        press('Enter')
        time.sleep(.5)