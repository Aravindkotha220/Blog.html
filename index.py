# Create a function that takes two numbers as arguments and returns their sum.
def add (num1,num2):
    return (num1+num2)
print(add(10,20))

# Write a function that takes an integer minutes and converts it to seconds.    
def minutes_to_seconds(minutes):
 return minutes*60
print(minutes_to_seconds(10))

# Create a function that takes a number as an argument, increments the number by +1 and returns the result.

def increment (numbers):
    return (numbers+1)
print (increment(10))

# Create a function that takes the age in years and returns the age in days.

def age_in_days(years):
 return years*365
print(age_in_days(26))

# sbi Create a function that takes voltage and current and returns the calculated power.

def calcuatepower(voltage,current):
    return voltage*current
print(calcuatepower(10,240))

# Write a function that returns the string "something" joined with a space " " and the given argument a.

def addsomthing(a):
 return "somthing"+ " "+a  
print(addsomthing("girish"))
print(addsomthing("Aravind"))

# Create a function that takes two arguments. Both arguments are integers, a and b. Return true if one of them is 10 or if their sum is 10.

def checkten(a,b):
    return a==10,b==10,(a+b)==10
print(checkten(10,5))
print(checkten(5,5))
print(checkten(3,5))

# Create a function that takes two strings as arguments and returns either true or false depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.
def equal_string_length(str1,str2):
    return len(str1)==len(str2)
print(equal_string_length("hello","world"))
print(equal_string_length("Aravind","gagan"))

# Create a function that takes a name and returns a greeting in the form of a string. Don't use a normal function, use an arrow function.
def greet(name):
    return f"Hello, {name} Welcome"
print(greet("Aravind"))

# Create a function that takes an array of 10 numbers (between 0 and 9) and returns a string of those numbers formatted as a phone number (e.g. (555) 555-5555).
def phonenumber(numbers):
    string=""
    for i in numbers:
        num=str(i)
        string=string+num
    return string

numbers=[9,6,4,0,6,5,7,4,1,3]
print(phonenumber(numbers))

# Create a function that returns an array of strings sorted by length in ascending order.
# def sort_by_length(strings):
#     return sorted(strings,key=len)
# letters="a","ccc","bb","eeee"
# print (sort_by_length(letters))

def sort_by_length(strings):
    return sorted(strings, key=len)
letters="a","ccc","bb","eeee"
words = "apple", "banana", "kiwi", "cherry", "blueberry"
print(sort_by_length(letters))
print(sort_by_length(words)) 
 

# Create a function that takes an array of arrays with numbers. Return a new (single) array with the largest numbers of each.

def largest_numbers(arrays):
    return [max(sub_array) for sub_array in arrays if sub_array]
nested_arrays = [[3, 5, 9], [10, 7, 20], [8, 4, 6]]
print(largest_numbers(nested_arrays))
