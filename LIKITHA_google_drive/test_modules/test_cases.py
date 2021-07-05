#!/usr/bin/python3.8

##############################################################################################
# Purpose of the script
##############################################################################################
# 1. To write the testcases for googledrive api
##############################################################################################
# contents of the script:
##############################################################################################

# 1.Checking all the functionality of googledrive api

#################################################################################################
# Importing required modules for the Script.

import logging
import py
import pytest
import sys, os
from googleapiclient.errors import HttpError

sys.path.append("/home/ubuntu01/Desktop/LIKITHA_google_drive/common_modules")
from checking_methods import (get_item, delete_item, generate_ids, create_file,
                                list_file, empty_trash, copy_item, status_code)

class TestForGoogledrive:

    """This class is used for testing the googledrive api by testing
    various options given in googledrive api"""

    logger = logging.getLogger(__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_get_item_status(self, input_ide):

        """Checks whether the get_item is responding with correct
        status code or not. If not responding correctly catching the
        Exception and printing in log file"""

        try:
            # Checking for the status code and asserting it to expected value
            assert status_code() == 200
        # Checking for the Exceptions
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_get_length_check(self, input_ide):

        """To check the length of file in googledrive api and if file not
        present catching the Exception and printing in log file"""

        
        try:
            res = get_item(input_ide)
            # Checking for the length of file  and asserting it to expected value
            assert len(res) != 0
        # Checking for the Exceptions
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_get_name_check(self, input_ide):

        """To check whether we are getting the correct file name or not
        if not catching the Exception and printing in log file"""
        
        try:
            res = get_item(input_ide)
            # Checking for the name of file  and asserting it to the expected name
            assert res["name"] == "images.jpg"
        # Checking for the Exceptions
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_get_type_check(self, input_ide):

        """To check the type of data returned by the get_item method
        is as expected or not. If not catching the Exception and
        printing in log file"""

        try:
            res = get_item(input_ide)
            # Checking for the name of file  and asserting it to the expected type
            assert type(res) == dict
        # Checking for the Exceptions
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_get_kind_check(self, input_ide):

        """To check whether a particular key is present in the data
        returned from the get_item method. If not catching the
        Exception and printing in log file"""

        try:
            res = get_item(input_ide)
            # Checking for the key in the file and checking whether the key is present or not
            assert "kind" in res.keys()
        # Checking for the Exceptions
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_list_len_check(self):

        """To check whether the length of the data is greater than zero.
        If the Exception occurs catching and printing in log file"""

        try:
            res = list_file()
            # Checking for the length of file  and asserting it to expected value
            assert len(res) != 0
        # Checking for the Exceptions
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_list_type_check(self):

        """To check the type of the type of data returned from the
        list_file method is correct or not. If not catching the exception
        and printing it in the log file."""

        try:
            res = list_file()
            # Checking for the type of data  and asserting it to expected value
            assert type(res) == tuple
        # Checking for the Exceptions
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_list_type_ide_check(self):

        """To check the type of the type of data returned from the
        list_file method is correct or not. If not catching the exception
        and printing it in the log file."""

        try:
            res = list_file()
            # Checking for the type of data and asserting it to expected value
            assert type(res[0]) == list
        # Checking for the Exceptions
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_list_type_name_check(self):

        """To check the type of the type of data returned from the
        list_file method is correct or not. If not catching the exception
        and printing it in the log file."""

        try:
            res = list_file()
            # Checking for the type of data  and asserting it to expected value
            assert type(res[1]) == list
        # Checking for the Exceptions
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_emptytrash_len_check(self):

        """To check the length of emptyTrash feature is as expected or not.
        If not catching the Exception and printing in log file"""

        try:
            res = empty_trash()
            # Checking for the length and asserting it to expected value
            assert len(res) == 0
        # Checking for the Exceptions
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_emptytrash_type_check(self):

        """To check the type of the data returned from the emptyTrash function
        is as expected or not If not catching the Exception and
        printing in log file"""

        try:
            res = empty_trash()
            # Checking for the type of data  and asserting it to expected value
            assert type(res) == str
        # Checking for the Exception
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_generate_ids_type_check(self):

        """To check whether the generate_ids function is returning data
        as per expecttion or not. If not catching the Exception and
        printing in log file"""

        try:
            res = generate_ids()
            # Checking for the type of data  and asserting it to expected value
            assert type(res) == dict
        # Checking for the Exception
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_generate_type_ids_len_check(self):

        """To check whether generate_ids returns same number of
        ids everytime or not. If not catching the Exception and
        printing in log file"""

        try:
            res = generate_ids()
            # Checking for the length of data  and asserting it to expected value
            assert len(res) > 0
        # Checking for the Exception
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_create_file_len_check(self):

        """To check whether the file is created or not in googledrive api.
        If not catching the Exception and printing in log file"""

        try:
            res = create_file()
            # Checking for the length of data  and asserting it to expected value
            assert len(res) != 0
        # Checking for the Exception
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_create_file_type_check(self):

        """To check whether the file is created or not in googledrive api is of
        expected type or not. If not catching the Exception
        and printing in log file"""

        try:
            res = create_file()
            # Checking for the type of data  and asserting it to expected value
            assert type(res) == str
        # Checking for the Exception
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_copy_items_count_check(self, input_ide):

        '''To check whether the file is copied in the googledrive or not.
        If not catching the Exception and printing in log file'''

        try:
            res = copy_item(input_ide)["name"]
            data_list = list_file()[0]
            # Checking for the count of data  and asserting it to expected value
            assert data_list.count(res) > 1
        # Checking for the Exception
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_copy_items_inlist_check(self, input_ide):

        '''To check whether the name of copied file is present or not in 
        googledrive api. If not catching the Exception and printing in log file'''

        try:
            res = copy_item(input_ide)["name"]
            data_list = list_file()[0]
            # Checking for the name of file in list_file() output and asserting it to expected value
            assert res in data_list
        # Checking for the Exception
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_delete_status(self, input_ide):

        '''To check the functionality of the delete method in googledrive api.
        If it is not working properly storing the error in log file'''

        try:
            res = delete_item(input_ide)
            # Checking for the type of data  and asserting it to expected value
            assert res == None
        # Checking for the Exception
        except Exception as e:
            self.logger.error(type(e).__name__)

##################################################################################
# Negative test cases
    logger.info('Execution of negative test cases')
##################################################################################

    # @pytest.mark.skip(reason="performing unittest")
    def test_get_length_check_negative(self, input_ide):

        """To check the length of file in googledrive api and if file is
        present and  catching the Exception and printing in log file"""

        try:
            res = get_item(input_ide)
            # Checking for the length of file  and asserting it to expected value
            assert len(res) == 0
        # Checking for the Exceptions
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_get_name_check_negative(self, input_ide):

        """To check whether we are getting the correct file name or not
        if yes catching the Exception and printing in log file"""

        try:
            res = get_item(input_ide)
            # Checking for the name of file  and asserting it to the expected name
            assert res["name"] != "images.jpeg"
        # Checking for the Exceptions
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_get_type_check_negative(self, input_ide):

        """To check the type of data returned by the get_item method
        is as expected or not. If not catching the Exception and
        printing in log file"""

        try:
            res = get_item(input_ide)
            # Checking for the name of file  and asserting it to the expected type
            assert type(res) != dict
        # Checking for the Exceptions
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_get_kind_check_negative(self, input_ide):

        """To check whether a particular key is present in the data
        returned from the get_item method. If not catching the
        Exception and printing in log file"""

        try:
            res = get_item(input_ide)
            # Checking for the key in the file and checking whether the key is present or not
            assert "kind" not in res.keys()
        # Checking for the Exceptions
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_list_len_check_negative(self):

        """To check whether the length of the data is greater than zero.
        If the Exception occurs catching and printing in log file"""

        try:
            res = list_file()
            # Checking for the length of file  and asserting it to expected value
            assert len(res) <= 0
        # Checking for the Exceptions
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_list_type_check_negative(self):

        """To check the type of the type of data returned from the
        list_file method is correct or not. If not catching the exception
        and printing it in the log file."""

        try:
            res = list_file()
            # Checking for the type of data  and asserting it to expected value
            assert type(res) != tuple
        # Checking for the Exceptions
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_list_type_ide_check_negative(self):

        """To check the type of the type of data returned from the
        list_file method is correct or not. If not catching the exception
        and printing it in the log file."""

        try:
            res = list_file()
            # Checking for the type of data and asserting it to expected value
            assert type(res[0]) != list
        # Checking for the Exceptions
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_list_type_name_check_negative(self):

        """To check the type of the type of data returned from the
        list_file method is correct or not. If not catching the exception
        and printing it in the log file."""

        try:
            res = list_file()
            # Checking for the type of data  and asserting it to expected value
            assert type(res[1]) != list
        # Checking for the Exceptions
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_emptytrash_len_check_negative(self):

        """To check the length of emptyTrash feature is as expected or not.
        If not catching the Exception and printing in log file"""

        try:
            res = empty_trash()
            # Checking for the length and asserting it to expected value
            assert len(res) != 0
        # Checking for the Exceptions
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_emptytrash_type_check_negative(self):

        """To check the type of the data returned from the emptyTrash function
        is as expected or not If not catching the Exception and
        printing in log file"""

        try:
            res = empty_trash()
            # Checking for the type of data  and asserting it to expected value
            assert type(res) != str
        # Checking for the Exception
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_generate_ids_type_check_negative(self):

        """To check whether the generate_ids function is returning data
        as per expecttion or not. If not catching the Exception and
        printing in log file"""

        try:
            res = generate_ids()
            # Checking for the type of data  and asserting it to expected value
            assert type(res) != dict
        # Checking for the Exception
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_generate_type_ids_len_check_negative(self):

        """To check whether generate_ids returns same number of
        ids everytime or not. If not catching the Exception and
        printing in log file"""

        try:
            res = generate_ids()
            # Checking for the length of data  and asserting it to expected value
            assert len(res) != 10
        # Checking for the Exception
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_create_file_len_check_negative(self):

        """To check whether the file is created or not in googledrive api.
        If not catching the Exception and printing in log file"""

        try:
            res = create_file()
            # Checking for the length of data  and asserting it to expected value
            assert len(res) == 0
        # Checking for the Exception
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_create_file_type_check_negative(self):

        """To check whether the file is created or not in googledrive api is of
        expected type or not. If not catching the Exception
        and printing in log file"""

        try:
            res = create_file()
            # Checking for the type of data  and asserting it to expected value
            assert type(res) != str
        # Checking for the Exception
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_copy_items_count_check_negative(self, input_ide):

        '''To check whether the file is copied in the googledrive or not.
        If not catching the Exception and printing in log file'''

        try:
            res = copy_item(input_ide)["name"]
            data_list = list_file()[0]
            # Checking for the count of data  and asserting it to expected value
            assert data_list.count(res) <= 1
        # Checking for the Exception
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_copy_items_inlist_check_negative(self, input_ide):

        '''To check whether the name of copied file is present or not in 
        googledrive api. If not catching the Exception and printing in log file'''

        try:
            res = copy_item(input_ide)["name"]
            data_list = list_file()[0]
            # Checking for the name of file in list_file() output and asserting it to expected value
            assert res not in data_list
        # Checking for the Exception
        except Exception as e:
            self.logger.error(type(e).__name__)

    # @pytest.mark.skip(reason="performing unittest")
    def test_delete_status_negative(self, input_ide):

        '''To check the functionality of the delete method in googledrive api.
        If it is not working properly storing the error in log file'''

        try:
            res = delete_item(input_ide)
            # Checking for the type of data  and asserting it to expected value
            assert res != None
        # Checking for the Exception
        except Exception as e:
            self.logger.error(type(e).__name__)
    

if __name__ == "__main__":

    pytest.main(args=["-sv", os.path.abspath(__file__)])



##########################################################################################################

#script details

# Script name               :       test_cases.py
# Script version            :       1.0
# Prepared By               :       LIKITHA K
# Create Date               :       24-june-2021
# Last Modification Date    :       27-june-2021

##########################################################################################################
