#!/usr/bin/python3.8

##############################################################################################
# Purpose of the script
##############################################################################################
# 1.Automating the E-commerce website using automation testing with python,selenium
##############################################################################################
# contents of the script:
##############################################################################################

# 1.Install the selenium

# 2.Write the python code with selenium webdriver using chrome.

# 3.Creating a pages folder having __init__.py, Checking_buttons.

# 4.In tests folder  test_amazon.py change the code and create config.txt with password in it

# 5.Toc check the functionality of the given E-commerce website. 

#################################################################################################
# Importing required modules for the Script..

import pytest
from selenium import webdriver
import time

# Storing the Driver, webpage url and username inside a dictionary
CONFIGS = {"Driver": webdriver.Chrome("/usr/lib/chromium-browser/chromedriver"),
           "URL": "http://automationpractice.com/index.php",
           "username": "kanlikitha99@gmail.com",
           }

# Create a text file with password and reading the data from the text file and storing it inside a variable
with open('password.txt', 'r') as fp:
    password = fp.read()

# Creating a class for checking the functionality.
class AmazonTest:

    #Intitalising the __init__ for the Class AmazonTest and declaring variables.
    def __init__(self):
        
        self.driver = CONFIGS["Driver"]
        self.URL = CONFIGS["URL"]
        self.user = CONFIGS["username"]
        self.password = str(password)
        self.Is_loggedin = False

    # To check Whether we are browsing the correct Page
    def getPage(self):
 
        self.driver.get(self.URL)
        self.driver.maximize_window()
        self.current_url = self.driver.current_url
        # Returns the current page
        return self.current_url

     # To Fill the username checkbox with given username
    def user_name(self):

        self.user_input = self.driver.find_element_by_id(
                            "ap_email").send_keys(self.user)

    # To click the continue button automatically
    def continue_click(self):

        self.continue_check = self.driver.find_element_by_id(
                                "continue").click()

     # To fill the password checkbox automatically
    def password_user(self):

        self.pass_input = self.driver.find_element_by_id(
                            "ap_password").send_keys(self.password)

    # Traverse through the given web page and click on the signin link
    def account_list(self):

        self.driver.get('https://www.amazon.com')
        self.nav_account_list = self.driver.find_element_by_id(
                                "nav-link-accountList").click()

    # To click the submit button automatically
    def submit_button(self):

        self.submit_button = self.driver.find_element_by_id("signInSubmit").click()
        
    # To get the colour of the required element in webpage
    def get_color(self):

        element = self.driver.find_element_by_id('auth-error-message-box')
        res = element.value_of_css_property('background-color')
        return res

    # To Validate whether the given username and password are correct or not
    def signin_user(self):

        # Calling the account_list method
        self.account_list()
        time.sleep(3)
        # Calling the user_name() method
        self.user_name()
        time.sleep(1)
        
        # Calling the continue_click() method
        self.continue_click()
        time.sleep(1)
        
        # Calling the password_user() method
        self.password_user()
        time.sleep(1)

        # Calling the submit_button() method
        self.submit_button()
        time.sleep(1)

        # trying to check whether the username is present or not
        try:

            self.nav_account_list = self.driver.find_element_by_id(
                                    "nav-your-amazon").click()
            return True

        # To overcome an Exception case
        except Exception:
            return False

        
    # To check whether the username is correct or not.
    def validate_username_failure(self):

        # Calling the account_list method
        self.account_list()
        time.sleep(3)

        # Calling the user_name() method
        self.user_name()
        time.sleep(1)

        # Calling the continue_check() method
        self.continue_click()
        time.sleep(1)

        # Calling the get_color method and storing the result in the colour variable
        colour = self.get_color()
        return colour
        
    # To check whether the upassword is correct or not.
    def validate_password_failure(self):

        # Calling the account_list method
        self.account_list()
        time.sleep(3)

        # Calling the user_name() method
        self.user_name()
        time.sleep(1)

        # Calling the continue_check() method
        self.continue_click()
        time.sleep(1)

        # Calling the password_user() method
        self.password_user()
        time.sleep(1)

        # Calling the submit_button() method
        self.submit_button()

        # Calling the get_color method and storing the result in the colour variable
        colour = self.get_color()
        return colour

    # To Check whether is forget password is working properly or not.
    def forget_password(self):

        # Calling the account_list method
        self.account_list()
        time.sleep(3)

        # Calling the user_name() method
        self.user_name()
        time.sleep(1)

        # Calling the continue_check() method
        self.continue_click()
        time.sleep(1)

        # Trying to check whether the forget password is working or not
        try:
            # Clicking on the forget password button
            forget_password_link = self.driver.find_element_by_id(
                                    "auth-fpp-link-bottom").click()

            # Calling the continue_check() method
            self.continue_click()
            time.sleep(50)

            # Clicking the submit button
            click = self.driver.find_element_by_id(
                    'cvf-submit-otp-button').click()

            # Assigning the new password 
            new_pass = 'password'

            # Entering the new password in the required field
            new_password = self.driver.find_element_by_id(
                            "ap_fpp_password").send_keys(new_pass)
            retype_password = self.driver.find_element_by_id(
                                "ap_fpp_password_check").send_keys(new_pass)

            # Calling the Continue_click() method
            self.continue_click()
            return True

        # Overcoming the Exceptional Case
        except Exception as e:
            return False

    # To check whether keep me signed in button is working properly or not.
    def keep_me_signedin(self):

        # Calling the account_list method
        self.account_list()
        time.sleep(3)

        # Calling the user_name() method
        self.user_name()
        time.sleep(1)

        # Calling the continue_check() method
        self.continue_click()
        time.sleep(1)

        # Calling the password_user() method
        self.password_user()
        time.sleep(1)
        try:
            
            # Clicking on the keepme signed button.
            check_box = self.driver.find_element_by_xpath(
                        '//*[@id="authportal-main-section"]/div[2]/div/div/div/form/div/div[2]/div/div/label/div/label/input').click()

            return True

        # Overcoming the Exception Case
        except Exception :
            return False

##########################################################################################################

#script details

# Script name               :       app.py
# Script version            :       1.0
# Prepared By               :       LIKITHA K
# Create Date               :       15-june-2021
# Last Modification Date    :       18-june-2021

##########################################################################################################
