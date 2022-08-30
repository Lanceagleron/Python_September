#LOOPS
#FOR
"""
for ___ in ___ :
    pass

first blank: iterative variable <-- will represent each single thing from the sequence we iterate over
ex: [1,2,3,4,7] iterative variable will represent each number in turn 

second blank: sequence to iterate over
"""


# for i in range(50,-1,-1):
#     if i == 10:
#         continue #will go on to the next iteration without running anymore code

#     if i == 8:
#         break #break will stop all iteration
#     print(i)
# range(start,stop,step)
# start is inclucsive and default to 0, can be left out
# stop is exclusive, will stop before this number
# step is the increment 

#for in lists
fruits = ['mango', 'banana', 'pears', 'lychee', 'dragon fruit', 'tomato']

i=0
# for each_fruit in fruits:
#     print(each_fruit) #without indices
#     print(i)
#     i+=1

# for i in range(len(fruits)):
#     print(f"{i}): {fruits[i]}") #with indices

#for in dictionaries

dog = {
    'name': 'Spot',
    'age': 3,
    'color': 'spotted',
    'favorite_food': 'cheese'
}

# for key in dog:
#     print(f"{key}: {dog[key]}")

#while loop over a dict, the iterative variable will be the keys

#list of dictionaries
dog_list = [
    {
    'name': 'Spot',
    'age': 3,
    'color': 'spotted',
    'favorite_food': 'cheese'
    },
    {
    'name': 'Fido',
    'age': 55,
    'color': 'grey/white',
    'favorite_food': 'applesauce and crickets'
    }
]

for dog in dog_list:
    print(f"{dog['name']} will print out now")
    for key in dog:
        print(f"{key}: {dog[key]}")


#WHILE
#ctrl + c = keyboard interrupt
# i = 0
# while(i<10):
#     print(i)
#     i+=1

