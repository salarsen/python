# names pt. 1

# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]
#
# def printStudents(students):
#     for value in students:
#         print value['first_name'] + " " + value['last_name']
#
# printStudents(students)

# names pt. 2
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def printPeople(people):
    for key, value in people.items():
        print key
        for index, item in enumerate(value):
            print str(index + 1) + " - " + item['first_name'] + " " + item['last_name'] + " - " + str(len(item['first_name']) + len(item['last_name']))

printPeople(users)
