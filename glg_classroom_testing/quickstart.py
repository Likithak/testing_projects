from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.
#SCOPES = ['https://www.googleapis.com/auth/classroom.courses.readonly']
# SCOPES = ['https://www.googleapis.com/auth/classroom.courses']
SCOPES = ['https://www.googleapis.com/auth/classroom.rosters']

def main():
    """Shows basic usage of the Classroom API.
    Prints the names of the first 10 courses the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('classroom', 'v1', credentials=creds)
    return service

def course_list():
    service = main()
    # Call the Classroom API
    results = service.courses().list(pageSize=10).execute()
    courses = results.get('courses', [])

    if not courses:
        print('No courses found.')
    else:
        print('Courses:')
        for course in courses:
            print(course['name'])

def create_course():
    service = main()
    course = {
        'name': '10th Grade Biology',
        'section': 'Period 2',
        'descriptionHeading': 'Welcome to 10th Grade Biology',
        'description': """We'll be learning about about the
                    structure of living creatures from a
                    combination of textbooks, guest lectures,
                    and lab work. Expect to be excited!""",
        'room': '301',
        'ownerId': 'me',
        'courseState': 'PROVISIONED'
    }
    course = service.courses().create(body=course).execute()
    print('Course created: %s %s' % (course.get('name'), course.get('id')))


if __name__ == '__main__':
    course_list()
    #create_course()