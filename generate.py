from selenium import webdriver
from selenium.webdriver.support.select import Select
import sys
import os
from pathlib import Path

file = '/home/aibek/Programming/PyCharm/scripts/password/driver/info.txt'
chrome = '/home/aibek/Programming/PyCharm/scripts/password/driver/chromedriver'


class Resources:

    def __init__(self):
        # open Chrome browser
        self.driver = webdriver.Chrome(chrome)
        # password length
        self.length = 10
        # get password using selenium
        self.password = self.Generate()

    def Generate(self):
        url = 'https://passwordsgenerator.net/'
        # open url
        self.driver.get(url)

        # change password length by selecting another one
        select = Select(self.driver.find_element_by_id('pgLength'))
        select.select_by_visible_text(str(self.length))

        # click on generate password button
        self.driver.find_element_by_xpath("//div[@class='button GenerateBtn']").click()

        # copy value from input
        password = self.driver.find_element_by_xpath("//input[@id='final_pass']").get_attribute('value')

        print(password)
        return password

    # change password
    def UpdatePassword(self, url, username):
        with open(file, 'r+') as f:
            newline = []
            for s in f.readlines():
                if url in s and username in s:
                    val = s.split(' ')
                    newline.append(s.replace(val[2][:-1], self.password))
                else:
                    newline.append(s)

        with open(file, "w") as f:
            for line in newline:
                f.writelines(line)

        print('Password updated')

    # save account into file
    def AddAccount(self, url, username):
        text = url + ' ' + username + ' ' + self.password + '\n'
        f = open(file, 'a+')
        f.write(text)
        f.close()
        print('Successfully saved')
        print(self.password)
