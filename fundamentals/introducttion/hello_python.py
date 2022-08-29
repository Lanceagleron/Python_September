print("Hello Class of september 2022")

#VARIABLES
x = 7
name_of_variable = 'in snake case'
# class name will be capitalized
GLOBAL_VAR = 'this is a global variable'
"""
js: var x = 7
"""

#DATA TYPES

#PRIMITIVE
#number
num = 7
num = 9.3

#string
string = "This is my string"
string2 = 'This is my string'
#boolean
#True of False value
bool = True
bool2 = False

# js:true||false


#COMPOSITE
#lists (known as arrays in JS)
list = [1,2,3,4,5,6,-10]
list2 = ["bob", "kyle", "susan"]
#           0       1       2       zero indexed
name = list[1]
#elements accessed by index
list[3] = 7
# print(list)
list.append(200)
print(list)
first_three = list[0:3]
last_number = list[-1:]
# print(first_three)
# print(last_number)
#list functions:
# len()
# print(len(list))
# #max() min()
# print(min(list))
# print(max(list2))
#methods of lists:
#.sort() .pop()
# list.sort(reverse=True)
# print(list)
# list2.sort(reverse=True)
# print(list2)
# list2.pop()
# print(list2)

#dictionaries (known as object in JS)
# {}
dog = {
    'name': 'Spot',
    'age': 3,
    'color': 'spotted',
    'favorite_food': 'cheese'
}
print(dog['name'])
#change the key value
dog['name'] = 'Tiger'
print(dog)
#dog['favorite_food'] breaks code, key error
print(dog.get("favorite_food",'not found'))

if "favorite_food" in dog:
    print('he has a fav')
else:
    print('he does not')

# del dog["favorite_food"]
# fav_food = dog.pop('favorite_food')
# dog.clear()
# .popitem() will remove last
print(dog)
#print(fav_food)
# StarWars = ('Luke', 'Vader', 'Ray', 'Yoda')
# StarTrek = ('Spock')
# universe = dict.fromkeys(StarWars, StarTrek)
# print(universe)


#tuples IMMUTABLE LIST
tuple = (1,2,3,4,5,6)
print(tuple[3])

#if
#else
#elif  (else if) 
# < > <= >= == != (not ==) or and 

if 'age' not in dog:
    print("Dog doesn't have an age")
elif dog['age'] > 4:
    print("Dog is older than 4")
else:
    print("dog is less than 4")