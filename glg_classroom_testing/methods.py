from quickstart import main

courseId = '360397053056'
userId = '116109698902420819986'

def invite_student():
    service = main()
    print('starts')
    '''sending the invitation'''
    info = {"userId":"kanamalurulikitha@gmail.com", "courseId":courseId,"role":"STUDENT"}
    i = service.invitations().create(body=info).execute()
    print('sended')

def get_students_list():
    service = main()
    student = service.courses().students().list(courseId=courseId).execute()
    print(student)
    return student

def get_student():
    service = main()
    try:
        student = service.courses().students().get(courseId= courseId,userId=userId).execute()
        print(student.get('userId'))
        return student.get('userId')
    except:
        student = 1
        print(student)
        return student

def delete_student():
    service = main()
    student = service.courses().students().delete(courseId=courseId,userId=userId).execute()
    print(student)
    print('Student Removed from course')
    return student.get('userId')

if __name__ == '__main__':
    # invite_student()
    # get_students_list()
    get_student()
    #delete_student()