x = [ [5,2,3], [10,8,9] ] 
people = [
     {'first_name':  'Michael',
      'last_name' : 'Jordan'
     },
     {'first_name' : 'John',
      'last_name' : 'Rosales'
     }
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

# # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
inside_drawer1 = x[1]
inside_drawer1[0] = 15
print(x)

# # Change the last_name of the first student from 'Jordan' to 'Bryant'
student1 = people[0]
student1['last_name'] = 'Bryant'
print(student1)

# # In the sports_directory, change 'Messi' to 'Andres'

sports_directory['soccer'][0] = "Andres"
print(sports_directory)

# # Change the value 20 in z to 30

a = z[0] 
a['y'] = 30
print(a)




students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(list):
    for student in list:
        # print(f"first_name - {student['first_name']}, last_name - {student['last_name']}")
        for key in student:
            print(f"{key} - {student[key]}")


iterateDictionary(students)
    
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printinfo(dict):
    for key,value in dict.items():
        print(len(value),key.upper())
        for i in range(0, len(value)):
            print(value[i])
    

printinfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
