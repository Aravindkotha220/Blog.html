from collections import Counter

# 1.Create a function that takes two numbers as arguments and returns their sum.

def add (num1,num2):
    return (num1+num2)
print(add(10,20))

#2. Write a function that takes an integer minutes and converts it to seconds.    
def minutes_to_seconds(minutes):
 return minutes*60
print(minutes_to_seconds(10))

#3. Create a function that takes a number as an argument, increments the number by +1 and returns the result.

def increment (number):
    return (number+1)
print (increment(10))

# 4.Create a function that takes the age in years and returns the age in days.

def age_in_days(years):
 return years*365
print(age_in_days(26))

# 5.sbi Create a function that takes voltage and current and returns the calculated power.

def calcuatepower(voltage,current):
    return voltage*current
print(calcuatepower(10,240))

#6. Write a function that returns the string "something" joined with a space " " and the given argument a.

def addsomthing(a):
 return "somthing"+ " "+a  
print(addsomthing("girish"))
print(addsomthing("Aravind"))

#7. Create a function that takes two arguments. Both arguments are integers, a and b. Return true if one of them is 10 or if their sum is 10.

def checkten(a,b):
    return a==10,b==10,(a+b)==10
print(checkten(10,5))
print(checkten(5,5))
print(checkten(3,5))

# 8.Create a function that takes two strings as arguments and returns either true or false depending on whether the total number of characters in the first string is equal to the total number of characters in the second string.
def equal_string_length(str1,str2):
    return len(str1)==len(str2)
print(equal_string_length("hello","world"))
print(equal_string_length("Aravind","gagan"))

#9. Create a function that takes a name and returns a greeting in the form of a string. Don't use a normal function, use an arrow function.
def greet(name):
    return f"Hello, {name} Welcome"
print(greet("Aravind"))

# 10.Create a function that takes an array of 10 numbers (between 0 and 9) and returns a string of those numbers formatted as a phone number (e.g. (555) 555-5555).
def phonenumber(numbers):
    string=""
    for i in numbers:
        num=str(i)
        string=string+num
    return string

numbers=[9,6,4,0,6,5,7,4,1,3]
print(phonenumber(numbers))

#11. Create a function that returns an array of strings sorted by length in ascending order.

def sort_by_length(strings):
    return sorted(strings, key=len)
letters="a","ccc","bb","eeee"
words = "apple", "banana", "kiwi", "cherry", "blueberry"
print(sort_by_length(letters))
print(sort_by_length(words)) 
 

#12. Create a function that takes an array of arrays with numbers. Return a new (single) array with the largest numbers of each.

def largest_numbers(arrays):
    return [max(sub_array) for sub_array in arrays if sub_array]
nested_arrays = [[3, 5, 9], [10, 7, 20], [8, 4, 6]]
print(largest_numbers(nested_arrays))

# 13.Create a function that takes an array of numbers and returns the second largest number.
def second_largest(numbers):
    numbers.sort(reverse=True) 
    return numbers[1] 
    
numbers = [10, 20, 4, 45, 50, 99]
print(second_largest(numbers)) 

# 14.Create a function that takes an array of items, removes all duplicate items and returns a new array in the same sequential order as the old array (minus duplicates).
def remove_duplicates(arr):
    seen = set()
    result = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result

items = [1, 2, 2, 3, 4, 4, 5, 1, 6]
print(remove_duplicates(items))

# 15.Create a function that takes an array of integers as an argument and returns a unique number from that array. All numbers except unique ones have the same number of occurrences in the array.

def find_unique_number(arr):
    counter = Counter(arr) 
    unique_numbers = [num for num, freq in counter.items() if freq == 1] 
    return unique_numbers

numbers = [11, 4, 4, 4, 4, 4, 8, 8, 8, 8, 6, 5, 6]
print(find_unique_number(numbers)) 

#16. Create a function that takes two strings as arguments and returns the number of times the first string (the single character) is found in the second string.
def count_char_occurs(char, text):
    if len(char) != 1:
        raise ValueError("First argument must be a single character")
    return text.count(char)

print(count_char_occurs('a', 'banana'))  
print(count_char_occurs('i', 'banana'))  

# 17.Create a function that takes a string and returns the number (count) of vowels contained within it.
def count_Vowels(string):
    count = 0
    for i in string:
        if i in ['a','e','i','o','u','A','E','I','O','U']:
            count += 1       
    return count
text = "Hello, how many vowels are in this sentence?"
print(count_Vowels(text))

#18. Given a string, create a function to reverse the case. All lower-cased letters should be upper-cased, and vice versa.
str = 'Happy Birthday'

def reverseCase(str):
    newstr = ''
    for i in str:
        if i==i.upper():
            newstr += (i.lower())
        else:
            newstr += (i.upper())
    return newstr

print(reverseCase(str))
     

#  19. Take one integer n, loop till n and pass each value to a function, create a function that takes one integer parameter, and multiply with 2 in every integer.
n = 5
def multFun(n):
    for i in range(1,n+1):
       print(i*2)
multFun(n)		
# 		

#  20. Create Function that will take one parameter and return type of the data.

def return_Datatype(data):
    return type(data)
print(return_Datatype(10.5))
print(return_Datatype(10))
print(return_Datatype("data"))	

#  21. Program to find greatest of three numbers(using ternary operator).
def greatest_in_threeNumbers(num1,num2,num3):
    return num1 if num1 > num2 and num1 > num2 else num2 if num2 > num3 else num3

print(greatest_in_threeNumbers(4,8,2))
		
#  22 . C Program to find factorial of number.
def factorial_num(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact

print(factorial_num(5)) 
		
#  23. C Program to arrange numbers in ascending order Sort the Array using loop only(you can not use predefined function).


#  24. Print Patter using loop.

def pattern(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()

pattern(5)


#  25. C Program to Calculate the Power of a Number(using loop only).
def power_Of_Num(a,b):
    result = 1
    for i in range(b):
        result *= a
    return result
print(power_Of_Num(5,3))

#  26. Program to Check Whether a Number is Prime or Not

# 		

#  27. Program to find LCM of two numbers using while loop



#  28. Program to Display Characters from A to Z Using Loop with count.
# count = 0
# for i in range(33, 65):
#     count += 1 
#     print(chr(i),count)

# print("Total characters displayed:", count)
count = 0
for i in range(65, 91):
    count += 1 
    print(chr(i),count)

print("Total characters displayed:", count) 

# 29. Program to find a missing number Using loop only(you can not use predefined function)
list =[1,3,4,5]
max = 5
for i in range(1, max + 1):
    if i  in list:
        pass
    else:
        print(i ,"is missing")

# 30. Program to count vowels and consonants in a given String.

char = "i am Aravind"
char = char.replace(' ','')
print(char)
vowelCount = 0
consonants = 0
for ch in char:
    if ch in ['a','e','i','o','u']:
        vowelCount += 1
    elif char.isalpha() :
        consonants +=1
      
print(vowelCount,consonants)

# 31. program to insert  the elements of an array for specific index.

list1 = [1,2,3,4,5,7,8,9,10]
list1.insert(5,6)
print(list1)


# 32. Reverse a number using while Loop
num = 123
def reverse(num):
    temp = num
    sum = 0
    while temp != 0:
        rem = temp % 10
        sum = sum * 10 + rem
        temp = temp // 10
    return sum    
    
print(reverse(num))

# 33. Count occurrence of number:

arr = [1,6,3,1,1,9,3,7,8,9,10,5,9,7,2,]
num = 7
count = 0
for i in arr:
    if num == i:
        count += 1
print(count)  

