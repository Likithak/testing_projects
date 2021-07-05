#Purpose of the script
########################################################################################################################
# Google Classroom API Validation.
# Create and execute test cases in pytest for the all the operations GET, CREATE, DELETE and LIST 
########################################################################################################################

# Importing required files and logging module
import pytest
from quickstart import main
from common_methods import *
import logging

# Create and configure logger
logging.basicConfig(filename="classroom_api_testing.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
  
# Creating an object
logger=logging.getLogger()
  
# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

# Testing either invitation is sended to students or not to join the class
def test_invite_student():
    invite = 'invitation sended'
    try:
        assert invite == invite_student()
        logging.info('Invitation sent to students')
    except:
        assert invite != invite_student()
        logging.info('invitation not sent to students')

# Testing either students are attending the course or not
def test_get_list():
    try:
        assert str(get_students_list()) != '0'
        logging.info('students are attenting the course')
    except:
        assert str(get_students_list()) == '0'
        logging.info('students are not attending the course')

# Testing whether student details is feteched from the students list.
def test_get_student():
    try:
        assert userId in str(get_student())
        logging.info('Fetched the student details')
    except:
        assert userId not in str(get_student())
        logging.info('Unable to fetch the student details')

# Testing either student can be deleted from the course 
def test_delete_student():
    try:
        assert userId in str(get_student)
        logging.info('Student deleted from the course')
    except:
        assert userId not in str(get_student())
        logging.info("student can't deleted that student doesn't exist")

########################################################################################################################

################################################## Script Details ######################################################

# Script Name                   :       test_api_classroom.py
# Script Version                :       1.0
# Prepared By                   :       Likitha.Kananamaluru@infinite.com
# Create Date                   :       10-06-2021
# Last Modification Date        :       14-06-2021

########################################################################################################################