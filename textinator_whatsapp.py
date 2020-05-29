from selenium import webdriver

driver_path = r'C:\Users\lakshya\PycharmProjects\untitled\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://web.whatsapp.com/')

name = input("Enter name: ")
first_name, last_name = name.split()
filename = input('Enter file name: ')


input("Enter 1 after scanning the code: ")


fh = open(filename)

user = driver.find_element_by_xpath('//span[@title = "{}" ]'.format(name))
user.click()

msg_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')

msg = ''
for line in fh:
    for word in line.split():
        msg = word
        msg_box.send_keys(msg)
        button = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')
        button.click()

# print(msg)




print("Sending complete")