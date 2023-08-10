# exercise-01 Vowel or Consonant

# Write the code that:
# 1. Prompts the user to enter a letter in the alphabet:
#      Please enter a letter from the alphabet (a-z or A-Z): 
# 2. Write the code that determines whether the letter entered is a vowel
# 3. Print one of following messages (substituting the letter for x):
#      - The letter x is a vowel
#      - The letter x is a consonant

# Hints:  Use the in operator to check if a character is in another string
#         For example, if some_char in 'abc':

letter = input('Enter a letter of the alphabet ').lower()
condition = True;

while(condition != False):
    print(f'The user entered {letter}')

    if(letter == "a" or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'):
        print(f"The letter {letter} is a vowel")
        condition = False;
    
    elif(len(letter) > 1):
        for i in letter:
            if(i == "a" or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
                print(f"The letter {i} is a vowel")
                condition = False;
            else:
                print(f"The letter {i} is a consonant")
                condition = False;
    else:
        print(f"The letter {letter} is a consonant")
        condition = False;

## Completed




# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

## Completed

input2 = input("Please enter a word or phrase: ").lower();

while(input2 != 'quit'):

    if(input2):
        print(f' What you entered is {len(input2)} characters long')
        input2 = input("Please enter a word or phrase, Alternatevely enter 'quit' to Exit: ").lower();
    elif(input2 == 'quit'):
        break










# exercise-03 Calculate Dog Years

# Write the code that:
# 1. Prompts the user to enter a dog's age like this:
#      Input a dog's age: 
# 2. Calculates the equivalent dog years, where:
#      - The first two years count as 10 years each
#      - Any remaining years count as 7 years each
# 3. Prints the answer in the following format:
#      The dog's age in dog years is xx

# Hints:
# Use the int() function to convert the string returned from input() into an integer
# Start with an if that checks if the age is less than 3

#Completed

dogAge = int(input(f"Input a dog's age: "))
condeNaste = True

if(dogAge < 3):
    finalAge = dogAge * 10;
    print(f'Your dog human age is {finalAge}')
else:
    finalAge = ((dogAge-2) * 7) + 20
    print(f'Your dog human age is {finalAge}')









# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equilateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - exactly two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

#Completed

print("Enter the lenghts of three side of a trinalge")
a = input(f"a: ")
b = input(f"b: ")
c = input(f"c: ")
A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

if(a == b  and b==c and c == a):
    print(f" A triangle with sides of ${a}, #{b} & {c} is a Equilateral triangle")
elif(a != b and b!=c and c!=a):
     print(f" A triangle with sides of ${a}, #{b} & {c} is a Scalene triangle")
elif(a==b or b==c or c==a):
    print(f" A triangle with sides of ${a}, #{b} & {c} is a Isosceles triangle")



    





# exercise-05 Fibonacci sequence for first 50 terms

# Write the code that:
# 1. Calculates and prints the first 50 terms of the fibonacci sequence.
# 2. Print each term and number as follows:
#      term: 0 / number: 0
#      term: 1 / number: 1
#      term: 2 / number: 1
#      term: 3 / number: 2
#      term: 4 / number: 3
#      term: 5 / number: 5
#      etc.

# Hints:
# The next number is found by adding the two numbers before it
# Use a while loop with a looping variable, or look into Python ranges, e.g.:
#   for n in range(50):

##Completed
def fibonacci():
    x = 1
    y = 1

    for i in range(50):
        if i == 0:
            print(f"term {i} number {i}")
            continue
        if i < 3 and i != 0:
            print (f"term: {i} number {1}" ) 
        else:
            fibo =  x + y
            print(f"term: {i} number: {fibo}");
            x = y
            y = fibo


fibonacci()






# exercise-06 What's the Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

time = input("Enter the month of the year: ").lower();
day = int(input("Enter the day of the month: "))
# season = ''
winter_month = ['Jan', 'Feb', 'Mar']
spring_month = ['Apr', ' May', 'Jun']
summer_month = ['Jul', 'Aug', 'Sep']
fall_month = ['Oct', 'Nov', 'Dec']

if time in ('jan', 'feb', 'mar'):
    season = 'Winter'
elif time in ('apr', 'may', 'jun'):
    season = 'Spring'
elif time in ('jul', 'may', 'sep'):
    season = 'Summer'
elif time in ('oct', 'nov', 'dec'):
    season = 'Fall'


if time == 'dec' and day > 20:
    season = 'Winter'
elif time == 'mar' and day > 20:
    season = 'Spring'
elif time == 'jun' and day > 20:
    season = 'Spring'
elif time =='jun' and day > 21:
    season = 'Summer'
elif time == 'sep' and day > 22:
    season ='Fall'

print(f"{day} / {time} : {season}")






# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
#   if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.



