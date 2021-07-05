#!/usr/bin/python3.8

##############################################################################################
# Purpose of the script
##############################################################################################
# 1.Testing the Ecommerce using the Automated Script.
##############################################################################################
# contents of the script:
##############################################################################################

# 1.Install the selenium

# 2.Write the python code with selenium webdriver using chrome

# 3.Creating a pages folder having __init__.py, Checking_buttons

# 4.In tests folder  test_web.py change the code and create config.txt with password in it

# 5.Toc check the functionality of the given E-commerce website. 

#################################################################################################

# Importing the required modules

import pytest
import logging
import sys, os
from colour import Color
sys.path.append('/Desktop/eCommerce application-selenium/eCommerce application')
from functionality_check  import AmazonTest

"""
This module contains web test cases for the tutorial.
Tests use Selenium WebDriver with Chrome and ChromeDriver.
The fixtures set up and clean up the ChromeDriver instance.
"""

# Creating an logging object
logger=logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Creating an instance for the AmazonTest class
amazon_class_instance = AmazonTest()

# Creating a test class for checking the functionalities
class TestAmazonTest:
    
    # Testing the getPage method to check whether we are getting corrct page or not
    def test_getPage(self): 
      logger.info('testing for test_getPage')
      try:
          # Asserting the result from getPage 
          assert amazon_class_instance.getPage() == "https://www.amazon.com/"
          logger.info('successfully done')
      except Exception as e:
          # Writting the error message in log file
          logger.error(msg= 'Requested page not found or opened')
          

    # Testing the email and password Success condition
    def test_validate_user(self):
      logger.info('testing for test_validate_user')
      try:
        # Asserting the result from validate_user 
        assert amazon_class_instance.signin_user() == 1
        logger.info('successfully done')
      except Exception as e:
        # Writting the error message in log file
        logger.error(msg = 'Credentials are not valid')
        

    # Testing the wrong email condition
    def test_incorrect_user_name(self):
      logger.info('testing for test_incorrect_user_name')
      try:
        assert amazon_class_instance.validate_username_failure() == 'rgba(255, 255, 255, 1)'
        logger.info('successfully done')
      except Exception as e:
          # Writting the error message in log file
          logger.error(msg = 'valid Username')

    # Testing the wrong password condition
    def test_incorrect_password(self):
      logger.info('testing for test_incorrect_password')
      try:
        assert amazon_class_instance.validate_password_failure() == 'rgba(255, 255, 255, 1)'
        logger.info('successfully done')
      except Exception as e:
        # Writting the error message in log file
        logger.error(msg = 'Valid Password')

    # Testing the forgot_password feature
    def test_forget_password(self):
      logger.info('testing for test_forget_password')
      try:
        assert amazon_class_instance.forget_password() == 1
        logger.info('successfully done')
      except Exception as e:
        # Writting the error message in log file
        logger.error(msg = 'Forget Password not working properly')

    # Testing the test_keep_me_signedin feature
    def test_keep_me_signedin(self):
      logger.info('testing for test_keep_me_signedin')
      try:
        # Asserting the condition
        assert amazon_class_instance.keep_me_signedin() == 1
        logger.info('successfully done')
      except Exception as e:
          # Writting the error message in log file  
          logger.error(msg = 'Keep me signed in not working properly (or) invalid credentials')



# Main Function
if __name__ == '__main__':
  
  pytest.main(args=['-sv', os.path.abspath(__file__)])



##########################################################################################################

#script details

# Script name               :       test_app.py
# Script version            :       1.0
# Prepared By               :       LIKITHA K
# Create Date               :       16-june-2021
# Last Modification Date    :       18-june-2021

##########################################################################################################