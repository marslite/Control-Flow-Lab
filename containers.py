#Exercise 1
students = ['Mattia', 'Jessica', 'Keyla']

##Printing second name
print(students[len(students)-2]);
##Printing last name of the list
print(students[-1])


# Exercise 2

foods = ('banana','tuna','burger')


for key in foods:
    print(f"{key} is a good food")

# Excercise 3
#Using a for loop, print just the last two food strings from foods.
for key in foods[1:]:
    print(f"{key} is a good food")


# Exercise 4
#Create a dictionary named home_town containing the keys of city, state and population.


populus = {
    'city' : 'Tebia',
    'state' : 'Califlorida',
    'population' : 100
}


print(f'I was born in {populus["city"]}, located in {populus["state"]} and with a population of {populus["population"]} ')



#Exercise 5
#Iterate over the key: value pairs in home_town and print a string for each item, for example:

home_town = {
    'city': 'Arcadia',
    'state': 'California',
    'population' : 5800
    }

for key, value in home_town.items():
    print(f" {key} = {value}")



#Excerise 6

cohort = []
food_idx = 0
for i in enumerate(students):
    cohort.append({
        'student' : i,
        'fav_food' : foods[food_idx]
        })
    food_idx+=1
        
print(cohort)


#Exercise 7
#Using the list of students and a list comprehension, assign to a variable named awesome_students a new list containing strings similar to this:

comprehension = [' is awesome!']

awesome_students = []

for i in students:
    awesome_students.append(i + comprehension[0])


print(awesome_students)



#Excercise 8
#Use a for loop to iterate over a list comprehension that filters the foods tuple to only include food strings that contains the letter a.

for key in foods:
    if 'a' in key:
        print(key)
    

