#!/usr/bin/python3.8

##############################################################################################
# Purpose of the script
##############################################################################################
# 1. To verify the googledrive api
##############################################################################################
# contents of the script:
##############################################################################################

# 1.Checking all the functionality of googledrive api

#################################################################################################
# Importing required modules for the Script..


import sys
sys.path.append("/home/ubuntu01/Desktop/LIKITHA_google_drive/prerequisites")
from quickstart import main
from googleapiclient.http import MediaFileUpload
from googleapiclient.errors import HttpError
import requests

# Importing main from the quickstart
service = main()

# Check whether we are using correct link or not
def status_code():
    url = 'https://drive.google.com/drive/my-drive'
    response = requests.get(url)
    return response.status_code
    
# To Create a file in googledrive.
def create_file():
    file_metadate = {"name":"test_create","description": 'application',
                        "starred": True}
    file = service.files().create(body = file_metadate, fields = 'id').execute()
    return file['id']

# To list all the files in googledrive 
def list_file():
    items = service.files().list().execute()
    lst_id = []
    lst_name = []
    files = items.get('files')
    for file in files:
        lst_id.append(file['id'])
        lst_name.append(file['name'])
    return (lst_name, lst_id)

# To get the content of a file in googledrive
def get_item(ide):
    items = service.files().get(fileId=ide).execute()
    return items

# To use the export feature in googledrive api
def export_item(ide):
    items = service.files().export(fileId=ide, mimeType='html').execute()
    return items

# To delete an item from the googledrive
def delete_item(ide):
    items = service.files().delete(fileId=ide).execute()
    return items

# To empty the trash from the googledrive 
def empty_trash():
    items = service.files().emptyTrash().execute()
    return items

# To generate_ids in googledrive 
def generate_ids():
    items = service.files().generateIds().execute()
    return items

# To copy a file from googledrive api
def copy_item(ide):
    items = service.files().copy(fileId=ide).execute()
    return items

# To update a file 
def update_item(ide):
    items = service.files().get(fileId=ide).execute()
    file_metadata = {'name': 'image.jpg'}
    media = MediaFileUpload('/home/ubuntu01/Downloads/image.jpg', mimetype='image/jpg')
    file = service.files().update(body=file_metadata,
                                        media_body=media,
                                        fileId=ide).execute()
    return True

if __name__ == "__main__":
    list_file()

##########################################################################################################

#script details

# Script name               :       common_methods.py
# Script version            :       1.0
# Prepared By               :       LIKITHA K
# Create Date               :       23-june-2021
# Last Modification Date    :       25-june-2021

##########################################################################################################
