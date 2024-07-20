#Idris Awodeji
#07.20.2024

#Program 1
print('Hello world')
#prints hello world to the screen 


#Program 2
user_name = input('please enter your name:')
#asks user for their name 
print(f'Hello, {user_name}! Nice to meet you.')
#greets user with their name


#Program 3
allowed_names = ['Idris', 'Zoe']
#defines names to be greeted
user_name = input('please enter your name:')
#asks user for thier name
if user_name in allowed_names:
    print(f'Hello, {user_name}! Nice to meet you.')
else:
    print('You cannot be greeted by name.')
#greets user if their name is allowed


#Program 4
import math
radius = float(input('please enter the radius of the circle:'))
#asks user to enter radius of the circle
area = math.pi * (radius ** 2)
#computes area of the circle
print(f'The area of the circle with radius {radius} is {area: .2f}')
#prints calculated area


#Program 5
miles_driven = float(input('please enter the number of miles driven:'))
#asks user to enter the number of miles driven
gallons_used = float(input('please enter the number of gallons used:'))
#asks user to enter the number of gallons used
mpg = miles_driven/gallons_used
#calculate MPG
print(f'Your cars fuel efficiency is {mpg: .2f} miles per gallon.')


#Program 6
fahrenheit = float(input('Please enter the temperature in Fahrenheit: '))
#asks user to enter temperature in Fahrenheit
celsius = (fahrenheit - 32)*5/9
#convert fahnreheit to celsius
print(f'the temperature in celsius is {celsius: .2f} degrees.')
#prints message with converted temperature


#Program 7
def week(day):
    if day == 0:
        return 'sunday'
    elif day == 1:
        return 'monday'
    elif day == 2:
        return 'tuesday'
    elif day == 3:
        return 'wednesday'
    elif day == 4:
        return 'thursday'
    elif day == 5:
        return 'friday'
    else:
         return 'saturday'
start_day = int(input('what is the starting day mumber?:'))
#asks user what starting day number it is
length_of_stay = int(input('what is your length of stay?:'))
#asks user length of stay
return_day = (start_day + length_of_stay) % 7
#calculate return day of the week
print(f'You will return on day number {return_day}.')
#prints message with return day number
