from selenium import webdriver
import time
from keyboard import press

driver_path = r'C:\Users\lakshya\PycharmProjects\untitled\geckodriver.exe'
driver = webdriver.Firefox(executable_path=driver_path)
driver.get('https://www.messenger.com/')

email=input("Enter Email: ")
password=input("Enter Password: ")


driver.find_element_by_xpath("//input[@id = 'email']").send_keys(email)       #Enters username
driver.find_element_by_xpath("//input[@id = 'pass']").send_keys(password)       #Enters password

driver.find_element_by_xpath("//button[@name = 'login']").click()                      #LogIn Button

name = input("Enter name: ")
first_name, last_name = name.split()
filename = input("Enter filename: ")
input("Enter 1 after scanning the code: ")
fh = open(filename)

user=driver.find_element_by_xpath("//input[@placeholder='Search Messenger']").send_keys(name)
time.sleep(8)
driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[2]/div[3]/div/div[1]/div/div/div[1]/span[1]/div/div/div[2]/ul/li/a/div/div[2]').click()
time.sleep(8)

msg_box = driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/span/div[2]/div[2]/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div")
msg_box.click()
#msg_box1=driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/span/div[2]/div[2]/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div/div/div/div")
#time.sleep(8)

msg = ''
for line in fh:
    for word in line.split():
        msg = word
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/span/div[2]/div[2]/div[2]/div/div[4]/div/div/div[1]/div/div[2]/div').send_keys(msg)
        press('Enter')
        time.sleep(.5)
